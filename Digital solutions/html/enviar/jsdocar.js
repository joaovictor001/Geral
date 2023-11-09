const removeProductButtons = document.getElementsByClassName("remove")
for (var i = 0; i < removeProductButtons.length; i++) {
  addToCartButtons[i].addEventListener("click", function(){
    console.log("clicou")
  })
}


const produto_car = document.getElementsByClassName("produto_car")
for(var i = 0; i <produto_car.length; i++){
  console.log(produto_car[i])
  const preco = produto_car[i].getElementsByClassName("preco")[0].innerText.replace("R$", "").replace(",", ".")
  const quantidade_pdt = produto_car[i].getElementsByClassName("product-qtd-input")
}
const produto_car = document.getElementsByClassName("produto_car")
totalAmount = 0

for (var i = 0; i < cartProducts.length; i++) {
  const productPrice = cartProducts[i].getElementsByClassName("preco")[0].innerText.replace("R$", "").replace(",", ".")
  const productQuantity = cartProducts[i].getElementsByClassName("product-qtd-input")[0].value

  totalAmount += productPrice * productQuantity
}