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

let user = "CHLIEB User";

document.body.innerHTML = greeter(user);

//import data from './json/data.json';

//const word = (<any>data).test;

//console.log(word);

