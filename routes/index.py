from flask import Blueprint
from flask import render_template


index_blueprint = Blueprint("index", __name__, static_folder="../static", template_folder="../templates", static_url_path="/static/index")

@index_blueprint.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@index_blueprint.route("/cadastrar", methods=['POST'])
def cadastrar():
    form = dict(request.form)
    produto = Produto(form["name"], form["picture"], form["barCod"])
    response = service.cadastrar(produto)
    return response



@index_blueprint.route("/pesquisar", methods=['GET'])
def find():
    return render_template("telaPesquisa.html")

@index_blueprint.route("/PesquisaEditar", methods=['GET'])
def PesquisaEditar():
    name= request.args.get('name')
    produto = service.busca(name)

    if pessoa == None:
        return "Não encontrado", 404

    return render_template("infofProduto.html", pessoa = pessoa[0]), 200
# Essa Parte eu não consegui fazer pq mudei algumas coisas, não tem mais 3 telas de pesquisa, agora são três botões con funções 
# que levam pras telas de editar ou deletar e ate a propria pesquisa que mostra as informações cadastradas no banco
# @index_blueprint.route("/editar", methods=['GET'])
# def pesq():
#     return render_template("edit.html")
#
# @index_blueprint.route("/info", methods=['GET'])
# def info():
#     name= request.args.get('name')
#     pessoa = service.busca(name)
#     return render_template("infosedit.html", pessoa = pessoa[0])
#
# @index_blueprint.route("/deletar", methods=['GET'])
# def deletar():
#     return render_template("exclui.html")
#
# @index_blueprint.route("/infoedit", methods=['GET'])
# def find_edit():
#     name= request.args.get('name')
#     pessoa = service.busca(name)
#     return render_template("infosedit.html", pessoa = pessoa[0])
#
# @index_blueprint.route("/edit", methods=['PUT'])
# def edit():
#     form = dict(request.form)
#     pessoa = Pessoa(form["name"], form["email"], form["address"], form["city"], form["state"], form["cep"])
#
#     response = service.edit(pessoa)
#     return str(response)
#
# @index_blueprint.route("/delete", methods=['GET'])
# def delete():
#     return render_template("delete.html")
#
# @index_blueprint.route("/info_delete", methods=['GET'])
# def info_delete():
#     name= request.args.get('name')
#     pessoa = service.busca(name)
#     return render_template("info_delete.html", pessoa = pessoa[0])
#
# @index_blueprint.route("/deletar", methods=['DELETE'])
# def delete_final():
#     form = dict(request.form)
#     pessoa = Pessoa(form["name"], form["email"], form["address"], form["city"], form["state"], form["cep"])
#
#     response = service.deletar(pessoa)
#     return str(response)
