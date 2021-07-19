var text = document.getElementById('text')
// получить элемент по его Id
text.title = "Хочу новый текст";
console.log(text.title);
console.log(text.id);

text.style.color = "blue";
text.style.backgroundColor = "red";

text.innerHTML = "New<br>string";

document.getElementById('text').style.color = "white";

var spans = document.getElementsByTagName('span');

for(var i = 0 ; i < spans.length; i++) {
    console.log(spans[i].innerHTML);
}

var spans = document.getElementsByClassName('simple-text');

for(var i = 0 ; i < spans.length; i++) {
    console.log(spans[i].innerHTML);
}