from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from lxml import etree


# Create your views here.
xml = etree.parse('app/cursos.xml')

def home(request):
    cursos = xml.xpath('//curso')
    info = dict()
    for c in cursos:
        info[c.find('guid').text] = c.find('nome').text
    ti = "Nomes dos cursos da UA:"
    tparams={
        'cursos': info,
        'frase': ti,
    }
    return render(request,"cursos.html",tparams)

def curso(request):
    guid = request.GET.get('guid')
    c = xml.find("//curso[guid = '{}']".format(guid)) #vai buscar o curso
    info = dict()

    info['Nome'] = c.find('nome').text
    info['Codigo'] = c.find('codigo').text
    info['Grau'] = c.find('grau').text
    info['Departamentos'] = []
    for ellen in c.xpath(".//departamentos//departamento"): #vai buscar a lista dos departamentos
        info['Departamentos'].append(ellen.text)
    info['Areascientificas'] = []
    for ellen in c.xpath('.//areascientificas//areacientifica'): #vai buscar a lista das areacientificas
        info['Areascientificas'].append(ellen.text)
    info['Local'] = c.find('local').text

    tparams={
        'curso': info,
        'nome': info.get('nome'),
    }
    return render(request,'cursoDetail.html',tparams)

def cursospordepart(request):
    depart = request.GET.get("depart")
    cursos = xml.xpath("//curso[departamentos//departamento = '{}']".format(depart))
    info = dict()
    for c in cursos:
        info[c.find("guid").text] = c.find("nome").text
    tparans = {
        "cursos": info,
        "titulo": "Lista dos cursos para o "+depart+":",
    }
    return render(request,"cursos.html",tparans);

