from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido.")

def about(request):
    return HttpResponse("Acerda de")