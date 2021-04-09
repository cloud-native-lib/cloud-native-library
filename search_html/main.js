var books = [];
var titles = [];


var request = new XMLHttpRequest()
request.responseType = 'json'

request.open('GET', "http://127.0.0.1:5000/api/listbook", true)

request.onload = function(){
    var data = request.response;
    if (request.status >= 200 && request.status < 400){
        data.forEach((titre) => {
           books.push(titre)
        })
        for (var book = 0; book < books.length; book++){
            titles.push(books[book]['titre'])
        };   
    }
    
}

request.send()

const app = document.getElementById("root");
const container = document.createElement("div");
container.setAttribute("id", "container");
app.appendChild(container);


function addElement (title) {

    document.body.onload = addElement;
    var newP = document.createElement("p");
    newP.setAttribute("class", "title")
    var newContent = document.createTextNode(title);
    newP.appendChild(newContent);

    var rootDiv = document.getElementById("root");
    rootDiv.appendChild(newP);
}


function removeElement (elementClass) {
    var elements = document.getElementsByClassName(elementClass);
    console.log(elements)
    for (var element = elements.length-1; element >= 0; --element){
        elements.item(element).remove();
    }
    
}

const input = document.querySelector('input');
input.addEventListener('input', updateValue);

function updateValue(e) {
    removeElement("title")
    console.log(e.target.value)
    for (var title = 0; title < titles.length; title++){
        if (titles[title].startsWith(e.target.value) && e.target.value != ""){
            addElement(titles[title])
        }
    }
}



