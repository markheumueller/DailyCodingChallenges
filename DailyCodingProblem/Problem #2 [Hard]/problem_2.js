const productExceptSelf = (numbers) => {
    const result = numbers.slice().map(() => null);
    numbers.forEach((_, i) => {
        result[i] = numbers.reduce((c, n) => c * n) / numbers[i];
    });

    return result;
};

const productExceptSelfWithoutDivision = (numbers) => {
    const result = numbers.slice().map(() => null);
    numbers.forEach((_, i) => {
        result[i] = numbers.reduce((c, n, idx) => idx === i ? c : c * n);
    });

    return result;
};

console.log(productExceptSelf([1, 2, 3]));
console.log(productExceptSelf([1, 2, 3, 4, 5]));

console.log(productExceptSelfWithoutDivision([1, 2, 3]));
console.log(productExceptSelfWithoutDivision([1, 2, 3, 4, 5]));
