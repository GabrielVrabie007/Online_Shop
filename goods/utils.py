from django.db.models import Q
from goods.models import Products


# query este string introdus in campul search
def q_search(query):
    # verifica produsele dupa ID
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # verifica produsele dupa cuvinte cheie
    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()
    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)
    return Products.objects.filter(q_objects)
