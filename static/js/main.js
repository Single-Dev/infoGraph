let msg = document.getElementById("msg")
let make_msg_none = document.getElementById("make_msg_none")

let doclochref = document.getElementById("doclochref")
doclochref.innerHTML = `${document.location.host}/chart/`

function noneFun() {
    msg.classList.add("d-none")

}

if(make_msg_none){
    make_msg_none.addEventListener("click", noneFun)
}