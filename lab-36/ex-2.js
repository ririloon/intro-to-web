let message = "Hello from global";

function helloGlobal() {
    console.log(message);
}

function helloLocal() {
    localMessage = "Hello from local";
    console.log(localMessage);
}

helloGlobal();
console.log(message);

helloLocal();
console.log(localMessage);
