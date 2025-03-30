from django.shortcuts import render

def home(request):
    print("worked")
    return render(request, "index.html")