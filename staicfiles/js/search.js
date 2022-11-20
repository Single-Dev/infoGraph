let users_count_div = document.getElementById("users_count_div")
let charts_count_div = document.getElementById("charts_count_div")
let users_div = document.querySelector(".users_div")
let chart_div = document.querySelector('.chart_div')


users_count_div.addEventListener('click', function (){
    users_div.style.display = "block"
    chart_div.style.display ="none"
    users_count_div.classList.add("activate_1")
    charts_count_div.classList.remove('activate_1')
}
 )

charts_count_div.addEventListener('click', function(){
    users_div.style.display = "none"
    chart_div.style.display ="block"
    users_count_div.classList.remove("activate_1")
    charts_count_div.classList.add('activate_1')
})