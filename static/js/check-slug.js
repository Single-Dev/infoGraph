let slug_input = document.getElementById("slug")
let res_msg = document.getElementById("res_msg")

const api_url = "/api/charts/";


async function getapi(url) {

    // Storing response

    const response = await fetch(url);
    // const response = await fetch(fun => setInterval(() => (fun()), 2));
    //                 const response = await  fetch(url => setInterval( () => {
    //                  url()                    
    // }, 1));
    // await new Promise(resolve => setTimeout(() => resolve(first()), 2000));


    // Storing data in form of JSON
    var data = await response.json();
    if (response) {
        hideloader();
    }
    show(data)
}
getapi(api_url)

console.log(slug_input.value);

function hideloader() {
}

function show(data) {
    console.log(data);
    for (let chart of data) {
        setInterval(() => {
            if(slug_input.value != ""){
                if(slug_input.value == chart.slug){
                    alert("Bu slug band")
                    slug_input.value += "894545"
                }
            }
        }, 1);
    }
}