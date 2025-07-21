from django.views.generic import ListView

from API.models import IntelForScienceWorks
from common.mixins import SearchMixin





class SearchView(ListView, SearchMixin):

    template_name = 'index.html'
    context_object_name = "information"

    def get_queryset(self):
        query = self.request.GET.get('q')
        query.strip()
        order_by = self.request.GET.get('order_by')


        worksquery = self.q_search(query)

        if order_by and order_by != "default":
            worksquery = worksquery.order_by(order_by)

        return worksquery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "search"
        return context

class IndexView(ListView):
    model = IntelForScienceWorks

    template_name = 'index.html'
    context_object_name = "information"

    def get_queryset(self):
        order_by = self.request.GET.get('order_by')

        information = IntelForScienceWorks.objects.all()

        if order_by and order_by != "default":
            information = information.order_by(order_by)

        return information

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All"
        return context
    

# def word_search(request):
#     query = request.GET.get('q')
#     order_by = request.GET.get('order_by')
    
#     query.strip()

#     # if not query:
#     #     return index(request)

#     worksquery = q_search(query)

#     if order_by and order_by != "default":
#         worksquery = worksquery.order_by(order_by)

    
#     context = {
#         'information':  worksquery,
#         'page_title': "search",
#     }

#     return render(request, "index.html", context)

# def index(request):

#     order_by = request.GET.get('order_by')

#     information = IntelForScienceWorks.objects.all()

#     if order_by and order_by != "default":
#         information = information.order_by(order_by)


#     context = {
#         'information':  information,
#         'page_title': "All",
#     }

#     return render(request, "index.html", context)