from .models import Link
# TODO ESTO ESUN DICCIONARIO DE CONTEXTO
def ctx_dict(request):
     ctx = {}
     links = Link.objects.all()
     for link in links:
          ctx[link.key] = link.url
     return ctx