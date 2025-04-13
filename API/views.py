from django.shortcuts import render

from API.models import IntelForScienceWorks
from API.utils import q_search



def word_search(request):
    query = request.GET.get('q')

    worksquery = q_search(query)
    
    context = {
        'information':  worksquery,
    }

    return render(request, "index.html", context)

def index(request):

    information = IntelForScienceWorks.objects.all()

    context = {
        'information':  information,
    }

    return render(request, "index.html", context)

