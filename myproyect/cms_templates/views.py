from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def inicio(request):
    if request.method == "GET":
        if request.user.is_authenticated():
            response = "<h4> Welcome " + request.user.username
            response += "<a href ='/logout'>Logout</a></h4>"
        else:
            response = "Loggeate : " + "<a href = '/login'>Login</a>"
    else:
        response = "404 NOT FOUND"
    return HttpResponse(response)

def identificador(request,identificador):
    if request.user.is_authenticated():
        response = "Hola " + request.user.username
    else:
        response =  "Loggeate : " + "<a href = '/login'>Login</a>"
    if request.method == "GET":
        try:
            pages = Pages.objects.get(id=int(identificador))
            response += "La pagina : " + str(pages.page)+"<br>"
        except Pages.DoesNotExist:
            response += "Page not found"
    else:
        response +=  "Method Error"
    return HttpResponse(response)

def recurso(request, name):
    if request.method == "GET":
        try:
            pages = Pages.objects.get(name = name)
            response = str(pages.page)+"<br>"
        except Pages.DoesNotExist:
            response = "Error, no existe esta pagina"
    elif request.method == "PUT":
        if request.user.is_authenticated() == True:
            try:
                pages = Pages.objects.get(name = name)
                response = "Pagina en la base de datos"
            except Pages.DoesNotExist:
                pagina = request.body
                newpage = Pages(name = name , page = pagina)
                newpage.save()
                response = "Pagina inclida en la base de datos"
        else:
            response = "Tienes que loggearte : "+ "<a href='/login'>Login</a>"
    else:
        response = "Error, metodo no encontrado"
    return HttpResponse(response)

def mostrar(request):
    if request.user.is_authenticated():
        persona = request.user.username
        response = "Hola " + request.user.username
    else:
        response = "Loggeate : <a href ='/login'>Login</a>"
    try:
        respuesta = "<h3> Paginas almacenadas en la base de datos : </h3><br>"
        Lista_pages = Pages.objects.all()
        for page in Lista_pages:
            respuesta += "<li><a href = '/"+ str(page.id)+"'>" +str(page.name) + "</a>"
    except Pages.DoesNotExist:
        respuesta = "No hay paginas almacenadas"
    template = get_template('plantilla.html')
    return HttpResponse(template.render(Context({'login':request.user.username,'contenido':respuesta })))

def annotated_identificador(request,identificador):
    if request.user.is_authenticated():
        respuesta = "Eres " + request.user.username + ". " + '<a href="/logout">Logout</a>'
    else:
        respuesta = '<p>Haz <a href="/login">login</a></p>'
    if request.method == "GET":
        try:
            pages = Pages.objects.get(id=int(identificador))
            pagina = "<p>" +str(pages.page) + "</p>"
        except Pages.DoesNotExist:
            pagina = "<h4><p>Error. No hay pagina para el identificador introducido</p></h4>"
        else:
            pagina = "<h4><p>Error. Mediante un identificador solo se puede hacer GET de dicha pagina.</p></h4>"

    template = get_template('plantilla.html')
    return HttpResponse(template.render(Context({'login': respuesta, 'pagina': pagina})))


def annotated_recurso(request, recurso):

    if request.method == "GET":
        try:
            pages = Pages.objects.get(name=recurso)
            pagina = "<p>" +str(pages.page) + "</p>"
        except Pages.DoesNotExist:
            pagina = "<h4><p>Error. No hay pagina para el recurso introducido.</p></h4>"
    elif request.method == "PUT":
        if request.user.is_authenticated() == True:
            try:
                pages = Pages.objects.get(name=recurso)
                pagina = "<p>La pagina que usted quiere incluir ya esta en la lista de paginas. Compruebe antes.</p>"
            except Pages.DoesNotExist:
                cuerpo = request.body
                nueva = Pages(name=recurso, page=cuerpo)
                nueva.save()
                pagina = "<p>La pagina ha sido incluida.</p>"
        elif request.user.is_authenticated() == False:
            pagina = "Haz <a href='/login'>login</a> <p>Usted debe estar autentificado para dicha peticion.</p>"
    else:
        pagina = "<p>Ha ocurrido algun error. Solo se puede realizar GET o PUT.</p>"
    template = get_template('plantilla.html')
    return HttpResponse(template.render(Context({'pagina': pagina})))
