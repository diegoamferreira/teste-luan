//array
//const pessoa = {nome:"Dimitri", sobrenome:"Teixeira", idade:30} //objeto
//pessoa.nome;                                                   //objeto
//const pessoa = ["Dimitri", "Teixeira", 30]; //matriz
//pessoa[0];//matriz
//alert(pessoa[pessoa.length -1]); #mostra o ultimo do array
//pessoa.push("Brasileiro"); #acrescenta na array
//pessoa.unshift("Brasileiro"); #acrescenta na array no valor 0
//pessoa.delete[0]; #deleta mas deixa vazio o lugar
//pessoa.pop(); # tira a ultimo da array
//pessoa.shift(); # tira a primeiro da array
//pessoa.splice(1, 0,"Item adicionado 1", "item adicionado 2"); #posição que vc quer colocar, quantos itens vão ser deletados, valores a serem adicionado na matriz
//const pessoaSlice = pessoa.slice(2); #pega os dois ultimos, se fosse (2,4), pegaria o pegaria do 2 ao 4 , nada antees e depois
//const lista1 = ["arroz", "feijão","batata"]:
//const lista2 = ["rabanete", "cove","sal"]:
//const superLista = liasta1.concat(lista2); #transforma 2 listas em 1
//sort = em ordem alfabetica

//Array.isArray(pessoa): #devolve true pq pessoa é uma array



var hora = new Date().getHours();

if (hora < 12){
    alert('Bom dia');
   }else if (hora < 18) {
    alert('Boa tarde');
   } else{
   alert('Boa noite');
   }

alert('olá');
document.getElementById("texto").innerHTML="MEU TEXTO <b>JS</b>!";

const carro = {  //objeto
    marca:"ford",
    modelo:"ka",
    ano:2005,
    placa:"ABC-1234",
    buzina: function() {alert('bi')} ,//metodo,propriedade com uma função dentro
    completo: function() {
        return"A marca é" + this.marca + " e o modelo é: " +this.modelo
    }
};
console.log(carro.completo());

function eventoClick (){
//    window.confirm("Confirma aqui");
Swal.fire({
  title: 'Do you want to do this?',
  text: "You won't be able to revert this!",
  type: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Yes, Do this!',
  cancelButtonText: 'No'
}).then((result) => {
  if (result.value) {
    Swal.fire(
      'Done!',
      'This has been done.',
      'success'
    )
    document.body.style.backgroundColor = "purple";
  }
})

    if (confirm("Branco ou Vermelho")) {
    document.body.style.backgroundColor = "white" ;
}   else {
    document.body.style.backgroundColor = "red";

}
//    alert('Acionou um evento de click ');
}
function mudaCor(){
    document.body.style.backgroundColor = "yellow";
    console.log ("teste");
}

function viraVermelho() {
    let div = document.getElementById("teste");
    div.style.backgroundColor = "pink";
}
function viraPreto() {
    let div = document.getElementById("teste");
    div.style.backgroundColor = "green";
}

function viraTeste1() {
    let p = document.getElementById("teste1");
    p.append('O maouse moveu<br>');
}
//function limpaTexto() {
//    document.getElementById("campoTexto").value = " ";
//}
//function verificar(){
//    let nome = document.getElementById("nome").value;
//
//    if (nome == ""|| nome == null){
//        let p = document.getElementById("teste");
//        p.innerHTML = "O campo não pode ser vazio";
//        p.style.color = "red";
//    }else{
//        let p = document.getElementById("teste");
//        p.innerHTML = "Voce preencheu";
//        p.style.color = "green";
//    }
//########################################################
class Carro{
    constructor(valor1,valor2,valor3){
        this.marca=valor1;
        this.modelo=valor2;
        this.ano=valor3;
    }
    buzina(){
        return this.modelo + " buzinou"
    }
}
const uno = new Carro("Fiat","Uno", 2001);
const gol = new Carro("Volkswagen","Gol", 2013);

console.log(uno.buzina());
console.log(gol);

function buscarCEP(){
    let input = document.getElementById('cep').value;

    const ajax = new XMLHttpRequest();
    ajax.open('GET', 'https://viacep.com.br/ws/' + input +'/json/');
    ajax.send();

    ajax.onload = function(){

        let obj = JSON.parse(this.responseText);

        let logradouro = obj.logradouro;
        let cidade = obj.localidade;
        let estado = obj.uf;

        document.getElementById('cep1').innerHTML = "Logradouro:" + logradouro +
        "<br> Cidade: "+cidade + "<br> Estado:" + estado;
    }
}