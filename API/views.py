from django.shortcuts import render

from API.models import AuthorNames, IntelForScienceWorks, TypesOfWork



def index(request):

    information = IntelForScienceWorks.objects.all()
    authors = AuthorNames.objects.all()
    types = TypesOfWork.objects.all()


    context = {
        'information':  information,
        'authors': authors,
        'TypesOfWork': types,
    }



    return render(request, "index.html", context)