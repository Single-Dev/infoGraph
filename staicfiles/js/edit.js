let modal = document.getElementById("modal")
let open_modal = document.getElementById("open_modal")
let close_icon = document.querySelector('.icon')

open_modal.addEventListener('click', function(){
    modal.style.display = "block"
})

close_icon.addEventListener('click', function(){
    modal.style.display = "none"
})