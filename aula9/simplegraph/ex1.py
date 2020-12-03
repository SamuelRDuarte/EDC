from simplegraph import SimpleGraph

def menu():
    print("")
    print("*** MENU ***")
    print("1. Listar Triplos")
    print("2. Listar Filmes")
    print("3. Realizador de um filme")
    print("4. Atores de um filme")
    print("5. Filmes de um realizador")
    print("---------------------")
    print("0. Sair")
    print("---------------------")
    return int(input("Opcao: "))

def listgraph():
    print("Listar Triplos")
    _graph.printAllTriples()

def listfilms():
    print("Listar Filmes")
    lista = _graph2.query([("?id","directed_by","?pessoa"),
                            ("?id","name","?film")])
    res = set()
    for f in lista:
        res.add(f["film"])

    print(sorted(res))

def getrealizador():
    rel = input("Filme: ")
    lista = _graph.query([("?film", "name", rel),
                          ("?film", "directed_by", "?rez"),
                          ("?rez", "name", "?nome")])
    print(lista[0]["nome"])

def getautores():
    rel = input("Filme: ")
    lista = _graph.query([("?film", "name", rel),
                          ("?film", "starring", "?aut"),
                          ("?aut", "name", "?nome")])
    res = set()
    for aut in lista:
        res.add(aut["nome"])
    print(sorted(res))

def getfilmsbyrealizador():
    rez = input("Realizador: ")
    lista = _graph.query([("?idRez", "name", rez),
                          ("?film", "directed_by", "?idRez"),
                          ("?film", "name", "?nome")])

    res = set()
    for f in lista:
        res.add(f["nome"])
    print(sorted(res))

def loadgraph():
    print("Carregar Grafo")
    _graph2.load("movies.csv") #ficheiro mais pequeno para a fazer pesquisas simples
    _graph.load("movies.org.csv") #ficheiro com mais info, para pesquisas mais complexas

def run(op):
    _funcs[op-1]()

if __name__ == "__main__":
    _funcs = (listgraph,listfilms,getrealizador,getautores, getfilmsbyrealizador)
    _graph2 = SimpleGraph()
    _graph = SimpleGraph()
    loadgraph()
    while(True):
        op = menu()
        if op == 0:
            break
        run(op)