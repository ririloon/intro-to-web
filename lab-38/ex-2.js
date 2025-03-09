let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
    let num = numbers[i];

    console.log("Current number:", num);
    if (num % 2 === 0) {
        sum += num;
        console.log("Added to sum, current sum:", sum);
    }
}

console.log("Total sum of even numbers:", sum);
