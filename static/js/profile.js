let edit_btn = document.getElementById("edit_btn")
let edit_profile_div = document.querySelector(".edit_profile_div")
let form = edit_profile_div.querySelector("form")
let update_btn = document.getElementById("update_btn")
let alert_msg = document.getElementById('msg')

edit_btn.addEventListener('click', function () {
    localStorage.setItem("form_display", 'block')
})

update_btn.addEventListener('click', function(){
    if (alert_msg){
        localStorage.setItem("form_display", 'none')
    }
})

setInterval(() => {
    edit_profile_div.style.display = localStorage.form_display
}, 1);

// form.addEventListener("submit", e => {
//     e.preventDefault()
// })