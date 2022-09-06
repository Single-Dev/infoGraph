let icon = document.getElementById('menu')
let close = document.getElementById('close')
let sideBar = document.querySelector('.side-bar')



icon.addEventListener('click', ()=>{
    sideBar.style.left= "0px"
    sideBar.style.height = body.height
})

close.addEventListener('click', ()=>{
    sideBar.style.left = "-250px"
})