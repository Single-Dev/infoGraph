let msg = document.getElementById("msg")
let make_msg_none = document.getElementById("make_msg_none")

function noneFun() {
    msg.classList.add("d-none")

}

if(make_msg_none){
    make_msg_none.addEventListener("click", noneFun)
}