from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

# Create your views here.

def json(modeladmin, request, queryset):
    json = []
    for q in queryset:
        json.append({
            'pregunta': q.pregunta,
            'respuestas': list(q.respuestas.all().values_list('respuesta', flat=True))
        })
    return JsonResponse(json, safe=False)

json.short_description = "Exportar selección a JSON"

class PruebaView(View):
    template_name="templates/prueba.html"

    def get(self,request,*args,**kwargs):

        p=request
        context={"p":""}
        return  render(p,self.template_name,context)

    def post (self,request,*args,**kwargs):
        import json
        p = request
        #print(p.__dict__.keys(),sep="\n")
        #print(p.read().decode())
        res = dict(p.POST)
        print(res)
        context = {"p": "Chau"}
        return render(p, self.template_name, context)
