function findLargest(...numbers) {
    let largest = Math.max(...numbers);
    console.log(`The largest number is ${largest}.`);
}

findLargest(5, -3, 16);
findLargest(-3, -5, -22.5);