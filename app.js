"use strict";
// import * as data from './json/data.json';
exports.__esModule = true;
function greeter(person) {
    return "Hello, " + person;
}
var user = "CHLIEB User";
document.body.innerHTML = greeter(user);
var data_json_1 = require("./json/data.json");
var word = data_json_1["default"].test;
console.log(word);
