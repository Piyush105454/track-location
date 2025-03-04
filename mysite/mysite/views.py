from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail

@csrf_exempt
def save_location(request):
    if request.method == "POST":
        data = json.loads(request.body)
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        # Generate Google Maps link
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

        # Email content
        subject = "Live Location Update"
        message = f"User's Location:\nLatitude: {latitude}\nLongitude: {longitude}\n\nView on Google Maps: {google_maps_link}"

        send_mail(subject, message, "your-email@gmail.com", ["your-email@gmail.com"])

        return JsonResponse({"message": "Location received and email sent"})
    return JsonResponse({"error": "Invalid request"}, status=400)

