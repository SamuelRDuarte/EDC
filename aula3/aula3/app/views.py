import urllib

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from lxml import etree

# Create your views here.
xml = etree.parse('app/cursos.xml')
url = "http://acesso.ua.pt/xml/curso.v5.asp?i="


def print_elems(elem, text="", result=""):
    elem_contents = text + str(elem) + " " + str(elem.attrib) + " " + str(elem.text)
    elem_contents = elem_contents.replace("{}", "").replace("\n","")
    result += elem_contents             # print element
    if len(elem.getchildren()) != 0:    # if they exist, print children
        for e in elem:
            return result + print_elems(e, text + "\t")
    return result


def home(request):
    cursos = xml.xpath('//curso')
    info = dict()
    for c in cursos:
        info[c.find('guid').text] = c.find('nome').text
    tparams = {
        'cursos': info,
        'frase': "Nomes dos cursos da UA:",
    }
    return render(request, "cursos.html", tparams)


def curso(request):
    guid = request.GET.get('guid')
    c = xml.find("//curso[guid = '{}']".format(guid))  # vai buscar o curso
    info = dict()

    info['Nome'] = c.find('nome').text
    info['Codigo'] = c.find('codigo').text
    info['Grau'] = c.find('grau').text
    info['Departamentos'] = []
    for ellen in c.xpath(".//departamentos//departamento"):  # vai buscar a lista dos departamentos
        info['Departamentos'].append(ellen.text)
    info['Areascientificas'] = []
    for ellen in c.xpath('.//areascientificas//areacientifica'):  # vai buscar a lista das areacientificas
        info['Areascientificas'].append(ellen.text)
    info['Local'] = c.find('local').text

    tparams = {
        'curso': info,
        'guid': c.find('guid').text,
    }
    return render(request, 'cursoDetail.html', tparams)


def cursodetails(request):
    guid = request.GET.get('guid')
    response = urllib.request.urlopen(url + guid).read()
    root = etree.fromstring(response)
    nome = root.find('nome').text

    xslt_file = etree.parse('app/cursos.xsl')
    transform = etree.XSLT(xslt_file)
    html = transform(root)
    tparams = {
        'teste': html,
        'titulo': nome,
    }
    return render(request, "cursoFullDetail.html", tparams)


def cursospordepart(request):
    depart = request.GET.get("depart")
    cursos = xml.xpath("//curso[departamentos//departamento = '{}']".format(depart))
    info = dict()
    for c in cursos:
        info[c.find("guid").text] = c.find("nome").text
    tparans = {
        "cursos": info,
        "frase": "Lista dos cursos para o " + depart + ":",
    }
    return render(request, "cursos.html", tparans);


def cursosporgrau(request):
    grau = request.GET.get("grau")
    cursos = xml.xpath("//curso[grau = '{}']".format(grau))
    info = dict()
    for c in cursos:
        info[c.find("guid").text] = c.find("nome").text
    tparans = {
        "cursos": info,
        "frase": "Lista dos cursos que tem " + grau + ":",
    }
    return render(request, "cursos.html", tparans);


def cursosporareacientifica(request):
    area = request.GET.get("area")
    cursos = xml.xpath("//curso[areascientificas//areacientifica = '{}']".format(area))
    info = dict()
    for c in cursos:
        info[c.find("guid").text] = c.find("nome").text
    tparans = {
        "cursos": info,
        "frase": "Lista dos cursos que faz parte da area " + area + ":",
    }
    return render(request, "cursos.html", tparans);


def cursosporlocal(request):
    local = request.GET.get("local")
    cursos = xml.xpath("//curso[local = '{}']".format(local))
    info = dict()
    for c in cursos:
        info[c.find("guid").text] = c.find("nome").text
    tparans = {
        "cursos": info,
        "frase": "Lista dos cursos que estão no " + local + ":",
    }
    return render(request, "cursos.html", tparans);


def departamentos(request):
    depart = xml.xpath("//curso//departamentos//departamento")
    info = list({d.text for d in depart})

    tparams = {
        "departamentos": info,
    }
    return render(request, "departamentos.html", tparams)


def areascientificas(request):
    area = xml.xpath("//curso//areascientificas//areacientifica")
    info = list({a.text for a in area})

    tparams = {
        "areas": info,
    }
    return render(request, "areascientificas.html", tparams)


def locais(request):
    places = xml.xpath("//curso//local")
    info = list({p.text for p in places})

    tparams = {
        "locais": info,
    }
    return render(request, "locais.html", tparams)
