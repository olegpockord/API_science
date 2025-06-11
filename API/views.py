from django.shortcuts import render

from API.models import IntelForScienceWorks
from API.utils import q_search



def word_search(request):
    query = request.GET.get('q')
    order_by = request.GET.get('order_by')
    
    if not query:
        return index(request)

    worksquery = q_search(query)

    if order_by and order_by != "default":
        worksquery = worksquery.order_by(order_by)

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