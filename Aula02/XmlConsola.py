from lxml import etree
from pathlib import  Path

def readXNL():
    file = Path(input("Nome do ficheiro XML: "))
    if file.is_file() and file.suffix == '.xml':
        info = etree.parse(file.name)
        nome = info.find('nome')
        print(nome.text)
        # root = info.getroot()
        # print(etree.tostring(root, pretty_print=True).decode())
        # printXML(root)
    else:
        print("Ficheiro errado")

def validateXml():
    xml = Path(input("Nome do ficheiro XML: "))
    xsd = Path(input("Nome do ficheiro XSD: "))
    if xml.is_file() and xml.suffix == '.xml' and xsd.is_file() and xsd.suffix == '.xsd':
        xml_info = etree.parse(xml.name)
        xsd_root = etree.parse(xsd.name)
        schema = etree.XMLSchema(xsd_root)
        print(schema.validate(xml_info))
    else:
        print("Ficheiro errado")

def printXML(elem,text = ''):
    # elem_contents = elem_contents.replace("{}", "").replace("\n", "")
    if len(elem.getchildren()) != 0:  # if they exist, print children
        elem_contents = text + " " + str(elem.tag)
        print(elem_contents)  # print element
        for e in elem:
            printXML(e, text + "\t")
    else:
        elem_contents = text + " " + str(elem.tag) + ": " + str(elem.text)
        print(elem_contents)  # print element



def main():
    while(1):
        print('*** MENU ***"')
        print("1. Leitura Doc XML")
        print("2. Validar Doc XML")
        print("3. Mostrar Doc XML")
        print("0. Sair")

        escolha = int(input("Escolha:"))

        if escolha == 1:
            readXNL()
        if escolha == 2:
            validateXml()
        if escolha == 3:
            file = Path(input("Nome do ficheiro XML: "))
            if file.is_file() and file.suffix == '.xml':
                info = etree.parse(file.name)
                nome = info.find('nome')
                # print(nome.text)
                root = info.getroot()
                # print(etree.tostring(root, pretty_print=True).decode())
                printXML(root)
            else:
                print("Ficheiro errado")
        if escolha == 0:
            exit()

if __name__ == '__main__':
    main()


