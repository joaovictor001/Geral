const removeProductButtons = document.getElementsByClassName("remove")
for (var i = 0; i < removeProductButtons.length; i++) {
  addToCartButtons[i].addEventListener("click", function(){
    console.log("clicou")
  })
}

let total = 0
const produto_car = document.getElementsByClassName("produto_car")
for(var i = 0; i <produto_car.length; i++){
  console.log(produto_car[i])
  const preco = produto_car[i].getElementsByClassName("produto_car")[0].innerText.replace("R$", "").replace(",", ".")
  const quantidade_pdt = produto_car[i].getElementsByClassName("product-qtd-input").value
  total = total+(preco*quantidade_pdt)
}
console.log(total)
