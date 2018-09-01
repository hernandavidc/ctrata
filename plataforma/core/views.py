from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import json

from .models import Pregunta, Caso

@method_decorator(login_required, name="dispatch")
class CasosListView(ListView):
    model = Caso
    template_name = "core/caso_list.html"

class HomePageView(TemplateView):
    contexto = {'title':"Home"}
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

class MapPageView(TemplateView):
    contexto = {'title':'Mapa de calor'}
    template_name = "core/map.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

def AntecedentesApiGet(request, cc):
    client = Cloudant(
        '0fe5f2c7-b763-4636-a768-6eb9ed79b1c6-bluemix', 
        'd5fb4bdd9bdeb36d09224085e367317c4013b9ec5e65f8889efdc40621bbc9c8', 
        url='https://0fe5f2c7-b763-4636-a768-6eb9ed79b1c6-bluemix:d5fb4bdd9bdeb36d09224085e367317c4013b9ec5e65f8889efdc40621bbc9c8@0fe5f2c7-b763-4636-a768-6eb9ed79b1c6-bluemix.cloudant.com', 
        connect=True
        )
    client.connect()
    db = client['ctrata']
    document = db["perfiles"]
    r = str(cc) in document
    client.disconnect()
    return HttpResponse(r)

@csrf_exempt
def PerfilVictimaApiPost(request):    
    if(request.method == "POST"):
        client = Cloudant(
        '0fe5f2c7-b763-4636-a768-6eb9ed79b1c6-bluemix', 
        'd5fb4bdd9bdeb36d09224085e367317c4013b9ec5e65f8889efdc40621bbc9c8', 
        url='https://0fe5f2c7-b763-4636-a768-6eb9ed79b1c6-bluemix:d5fb4bdd9bdeb36d09224085e367317c4013b9ec5e65f8889efdc40621bbc9c8@0fe5f2c7-b763-4636-a768-6eb9ed79b1c6-bluemix.cloudant.com', 
        connect=True
        )
        client.connect()
        db = client['ctrata']
        received_json_data = json.loads(request.body.decode("utf-8"))
        document = db["perfiles"]
        cc = list(received_json_data.keys())[0]
        if cc in document:
            actual = document[cc]
            size = len(actual)
            actual[str(size+1)] = received_json_data[cc]
            document.save()
        else:
            document[cc] = {'1':received_json_data[cc]}
            document.save()
        client.disconnect()
    return HttpResponse('ok')

def PregApiList(request, motivo):
    pregsReturn = get_list_or_404(Pregunta, motivo=motivo)
    json_responser = {'data':[]}
    for preg in pregsReturn:
        json_responser['data'].append({'key':preg.cont,'id':preg.id,'answers':[1,2,3,4,5]})

    return JsonResponse(json_responser)
#class SampleView(TemplateView):
#    template_name = "core/sample.html"

