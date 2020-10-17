from lxml import etree
from pathlib import Path


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


def printXML(elemento, info=''):
    if len(elemento.getchildren()) != 0:
        elem_info = info + " " + str(elemento.tag) + ":"
        print(elem_info)
        for e in elemento:
            printXML(e, info + "\t")
    else:
        elem_info = info + " " + str(elemento.tag) + " - " + str(elemento.text)
        print(elem_info)  # print element


def main():
    while (1):
        print('\n*** MENU ***"')
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
                print("\n")
                printXML(root)
            else:
                print("Ficheiro errado")
        if escolha == 0:
            exit()


if __name__ == '__main__':
    main()
