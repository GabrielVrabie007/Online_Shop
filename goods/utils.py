from tkinter import Entry
from django.db.models import Q
from goods.models import Products
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
)
from django.contrib.postgres.search import SearchHeadline


# query este string introdus in campul search
# advanced search goods by name,description
def q_search(query):
    # verifica produsele dupa ID
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        )
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        )
    )
    return result


# verifica produsele dupa cuvinte cheie
# keywords = [word for word in query.split() if len(word) > 2]

# q_objects = Q()
# for token in keywords:
#     q_objects |= Q(description__icontains=token)
#     q_objects |= Q(name__icontains=token)
# return Products.objects.filter(q_objects)
