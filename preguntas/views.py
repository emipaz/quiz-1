from django.http import JsonResponse

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
