let array1 = [3, 1, 4, 2];
let array2 = [4, 5, 3, 6];
let intersection = [];
for (let i = 0; i < array1.length; i++) {
    if (array2.includes(array1[i]) && !intersection.includes(array1[i])) {
        intersection.push(array1[i]);
    }
}
console.log("Intersection:", intersection);
