// import * as data from './json/data.json';
function greeter(person) {
    return "Hello, " + person;
}
var user = "CHLIEB User. Footnote";
//document.body.innerHTML = greeter(user);
//let myHeading = document.querySelector('h6');
//myHeading.textContent = 'foot!';
//var elem = document.createElement('div');
//import data from './json/data.json';
//const word = (<any>data).test;
//console.log(word);
var div = document.createElement('div');
div.textContent = "Dynamically created footer";
div.setAttribute('class', 'baking');
document.body.appendChild(div);
