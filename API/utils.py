from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
)
from API.models import IntelForScienceWorks


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return IntelForScienceWorks.objects.all().filter(id=int(query))
    
    vector = SearchVector("title", "annotation", "key_words", "OECD")
    query = SearchQuery(query)

    result = (
        IntelForScienceWorks.objects.all().annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    return result