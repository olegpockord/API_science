from django.shortcuts import render

from API.models import IntelForScienceWorks



def index(request):

    information = IntelForScienceWorks.objects.all()

    context = {
        'information':  information,
    }


    return render(request, "index.html", context)