from simplegraph import SimpleGraph
from inferencerule import KnownRule

def menu():
    print("")
    print("*** MENU ***")
    print("1. ex1")
    print("2. Print ex1")
    print("3. ex2")
    print("---------------------")
    print("0. Sair")
    print("---------------------")
    return int(input("Opcao: "))

def ex1():
    print("infer known people from Winoma Ryder")
    rule = KnownRule()
    _graph.applyinference(rule)
    #printEx1()
    print("---------DONE------")

def printEx1():
    lista = _graph.query([('Winona Ryder', 'knows', '?person')])
    #print(lista)
    for f in lista:
        print("Winoma Ryder --> %s" % (f['person']))

def ex2():
    _graph.saveTriples("winona.csv", ('Winona Ryder', 'knows', None))
    print("---------DONE------")

def loadgraph():
    print("Carregar Grafo")
    _graph.load("celebrities.csv") 

def run(op):
    _funcs[op-1]()

if __name__ == "__main__":
    _funcs = (ex1,printEx1,ex2)
    _graph = SimpleGraph()
    loadgraph()
    while(True):
        op = menu()
        if op == 0:
            break
        run(op)