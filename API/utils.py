from django.db.models import Value, TextField
from django.db.models.functions import Cast
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
)
from django.contrib.postgres.search import SearchHeadline, SearchQuery, TrigramSimilarity
from API.models import IntelForScienceWorks


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return IntelForScienceWorks.objects.all().filter(id=int(query))
    
    query_for_trig = query

    vector = SearchVector("title", weight='A') + SearchVector("key_words", weight='B') + SearchVector("OECD", weight='C') + SearchVector("annotation", weight='C')
    query = SearchQuery(query, search_type='phrase')
 

    result = (
            IntelForScienceWorks.objects.all().annotate(rank=SearchRank(vector, query))
            .filter(rank__gte=0.05)
            .order_by("-rank")
        )

    if result:
        result = result
    else:
        result = IntelForScienceWorks.objects.all().annotate(similarity = TrigramSimilarity(Cast('title', TextField()), 
                 Value(query_for_trig)) +
                 TrigramSimilarity(Cast('annotation', TextField()), 
                 Value(query_for_trig))
                 ).filter(similarity__gte=0.1).order_by('-similarity')

    result = result.annotate(
        headline=SearchHeadline(
        ("title"),
        query,
        start_sel='<span style="font-weight: bolder;">',
        stop_sel="</span>",
        )
    )

    return result