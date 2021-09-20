function cadastrarProduto() {
  var name = $("#name").val()
  var email= $("#picture").val()
  var address= $("#barCod").val()

var settings = {
   "url": "http://localhost:5000/cadastrar",
   "method": "POST",
   "timeout": 0,
   "headers": {
     "Content-Type": "application/x-www-form-urlencoded"
    },
   "data": {
     "name": name,
     "picture": picture,
     "barCod": barCod
   }
 }
 $.ajax(settings).done(function (response) {
   console.log(response)
 }
}
//FAZER FUNÇÃO DOS BOTÕES, EU ACHO QUE TA ERRADO
// function cadastro(){
//  window.location.replace("/")
// }
// function pesquisar(){
//  window.location.replace("/telaPesquisa")
// }
// function pesquisa(){
//   var name= $("#name").val()
//
//   window.location.replace("/busca?name=" + name)
// }
//
// function PesquisaEditar(){
//   window.location.replace("/editar")
// }
// function PesquisarParaDeletar(){
//   window.location.replace("/telaDelete")
// }
// function deletar(){
//   var name= $("#name").val()
//   window.location.replace("/info_delete?name=" + name)
// }

function edit(){
  var name= $("#name").val()
  var picture= $("#picture").val()
  var barCod= $("#barCod").val()


  var settings = {
    "url": "http://localhost:5000/edit",
    "method": "PUT",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    "data": {
      "name": name,
      "picture": picture,
      "barCod": barCod
    }
  };

  $.ajax(settings).done(function (response) {
    if (response==200) {
        window.location.replace("/busca?name=" + name)
    }
    else {
      alert("alguma coisa deu errado!!")
    }
  })
}
function deletar(){
  var name= $("#name").val()
  var picture= $("#picture").val()
  var barCod= $("#barCod").val()


  var settings = {
    "url": "http://localhost:5000/deletar",
    "method": "DELETE",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    "data": {
      "name": name,
      "picture": picture,
      "barCod": barCod,

    }
  };
  $.ajax(settings).done(function (response) {
    if (response==200) {
        window.location.replace("/")
    }
    else {
      alert("alguma coisa deu errado!!")
    }
  })
}
