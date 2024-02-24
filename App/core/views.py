# views.py
from django.shortcuts import render
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def hone(request):
    return render(request, 'hone.html')


def home(request):
    if request.method == 'POST':
        # Process the form submission here
        # For demonstration purposes, let's assume we have processed the form data

        # Redirect to homepage with a success message
        return redirect('home')  # Redirect to the same view (homepage)
    return render(request, 'home.html')
