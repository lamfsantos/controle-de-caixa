from models import produto
from repositories import produto as repo

def cadastrar(produto: Produto):
    try:
        repo.insert(produto)
        return "Produto cadastrado com sucesso"
    except Exception as e:
        print(e)
        return "Algo deu errado"

def busca(name: str):
    produto = repo.find(name)

    if (produto == []):
        return None

    produto = parse_produto(produto[0])

    return produto

def parse_produto(produto: list):
    return_list = []
    dict = {}

    dict["name"] = produto[1]
    dict["foto"] = produto[2]
    dict["barCod"] = produto[3]

    return_list.append(dict)

    return return_list

def editar(produto: Produto):
    repo.edit(produto)
    return 200

def deletar(produto: Produto):
    repo.deletar(produto)
    return 200
