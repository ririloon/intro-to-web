if (true) {
    var varVariable = "I'm declared with var";
}
console.log(varVariable);

let letVariable;
if (true) {
    letVariable = "I'm declared with let";
}
console.log(letVariable);

const constVariable = "I'm declared globally";

if (true) {
    console.log(constVariable);
}

console.log(constVariable)