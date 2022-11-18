let edit_btn = document.getElementById("edit_btn")
let edit_profile_div = document.querySelector(".edit_profile_div")
let form = edit_profile_div.querySelector("form")
let update_btn = document.getElementById("update_btn")

edit_btn.addEventListener('click', function () {
    edit_profile_div.style.display = "block"
})

// form.addEventListener("submit", e => {
//     e.preventDefault()
// })