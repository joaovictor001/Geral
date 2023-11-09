const removeProductButtons = document.getElementsByClassName("remove")
for (var i = 0; i < removeProductButtons.length; i++) {
  removeProductButtons[i].addEventListener("click", function(event){
    event.target.parentElement.parentElement.parentElement.remove()
  })
}