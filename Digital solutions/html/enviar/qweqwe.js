if (document.readyState ="loading"){
  document.addEventListener("DOMContentLoaded", ready)
} else {
  ready()
}

function ready(){
  const removeProductButtons = document.getElementsByClassName("remove")
  for (var i = 0; i < removeProductButtons.length; i++) {
    removeProductButtons[i].addEventListener("click", removerProduto)
  }

    const input_qtd = document.getElementsByClassName("product-qtd-input")
    for(var i = 0; i < input_qtd.length; i++){
      input_qtd[i].addEventListener("change", Total_update)
  }
  //adicionar produtos no carrinho
  const addToCartButton = document.getElementsByClassName("botao_para_adicionar");
  for (var i = 0; i < addToCartButton.length; i++){
  addToCartButton[i].addEventListener('click', Adicionar_ao_carrinho);
  }
}


function Adicionar_ao_carrinho(event){
  const button = event.target
  const infos_produto = button.parentElement.parentElement
  const produto_imagem = infos_produto.getElementsByClassName("Imagem_doce")[0].src
  const produto_nome = infos_produto.getElementsByClassName("titulo_doce")[0].innerText
  const produto_preco = infos_produto.getElementsByClassName("price")[0].innerText.replace("R$", "").replace(",", ".").replace("/unidade", "").replace("/porção", "")
  console.log(produto_nome)
  
  let novoProdutoCarrinho = document.createElement("tr")
  novoProdutoCarrinho.classList.add("produto_car")
  novoProdutoCarrinho.innerHTML=
  `
                <td>
                  <div class="product">
                    <img src="${produto_imagem}" alt="" />
                    <div class="info">
                      <div class="name">${produto_nome}</div>
                      <div class="category">Categoria</div>
                    </div>
                  </div>
                  <td>
                    <span class="preco">${produto_preco}/span>
                  </td>
                  <td>
                      <input type="number" value="1" min="0" class="product-qtd-input">
                    </td>   
                </td>
                <td>R$243</td>
                <td>
                  <button class="remove"><i class="bx bx-x"></i></button>
                </td>
  `;
  const tabelaCarrinho = document.querySelector("table tbody");
  tabelaCarrinho.appendChild(novoProdutoCarrinho);
}




  



 
  


function removerProduto(event){
  event.target.parentElement.parentElement.parentElement.remove()
  Total_update()
}

function Total_update(){
  let total = 0
  const produto_car = document.getElementsByClassName("produto_car")
  for(var i = 0; i <produto_car.length; i++){
    console.log(produto_car[i])
    const preco = produto_car[i].getElementsByClassName("preco")[0].innerText.replace("R$", "").replace(",", ".").replace(" ", "")
    const quantidade_pdt = produto_car[i].getElementsByClassName("product-qtd-input")[0].value
    console.log(quantidade_pdt)
    total = total+(preco*quantidade_pdt)
  }
  console.log(total)
}
