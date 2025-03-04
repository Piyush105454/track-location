from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail

# For GET request: display the HTML page
def home(request):
    return render(request, 'home.html')

# For POST request: save location and send email
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

        send_mail(subject, message, "swapeatmail@gmail.com", ["piyushmodi812@gmail.com"])

        return JsonResponse({"message": "Location received and email sent"})
    
    return JsonResponse({"error": "Invalid request"}, status=400)
