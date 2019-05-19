// import * as data from './json/data.json';

declare module namespace {

    export interface Ingredient {
        water: string;
        salt: string;
        flour: string;
    }

    export interface Recipe {
        name: string;
        date: string;
        ingredients: Ingredient[];
    }

    export interface Bakings {
        aa: string;
        a: string;
        c: string;
        e: string;
    }

    export interface RootObject {
        test: string;
        recipes: Recipe[];
        boolean: boolean;
        color: string;
        null?: any;
        number: number;
        f: string;
        bakings: Bakings;
        string: string;
    }

}

function greeter(person) {
    return "Hello, " + person;
}

let user = "CHLIEB User. Footnote";

//document.body.innerHTML = greeter(user);

//let myHeading = document.querySelector('h6');
//myHeading.textContent = 'foot!';

var elem = document.createElement('div');

//import data from './json/data.json';

//const word = (<any>data).test;

//console.log(word);

