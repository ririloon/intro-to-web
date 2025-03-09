function parseJSON(jsonStr) {
    try {
        let parsedData = JSON.parse(jsonStr);
        console.log(parsedData);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

parseJSON('{"name": "Alice", "age": 25}');
//parseJSON('{name: "Alice", age: 25}');