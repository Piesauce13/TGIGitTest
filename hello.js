console.log("Hello everyone!");

// Variable Declarations
var username = "Pissoth";
let studentName = "Lakshmi";

// Multiple Assignments
let x = (y = z = 10);
let [a,b,c] = [1,2,"hello"];

// Reassignment
let my_variable = 10;
my_variable = "Hello";
my_variable = 3.14;

// Const Declaration
const pi = '3.14159';
const maxSize = 100;

// Delete Variable by Setting to Null
my_variable = null;

// // If condition
// if (a > b) {
//     console.log("a is greater than b");
// } else if (a == b) {
//     console.log("a is equal to b");
// } else {
//     console.log("a is less than b");
// }

// let userInput = prompt("Please enter your number:");

// if (userInput < 0) {
//     console.log("You entered a negative number.");
// } else if (userInput == 0) {
//     console.log("You entered zero.");
// } else {
//     console.log("You entered a positive number.");
// }

const fruits = ["apple", "banana", "cherry"];

for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

var count = 1;

do {
    console.log('"Count: " + count');
    let count = count + 1;
} while (count <= 5);