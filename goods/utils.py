from tkinter import Entry
from django.db.models import Q
from goods.models import Products
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


# query este string introdus in campul search
# advanced search goods by name,description
def q_search(query):
    # verifica produsele dupa ID
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("rank")

    # verifica produsele dupa cuvinte cheie
    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    # return Products.objects.filter(q_objects)
