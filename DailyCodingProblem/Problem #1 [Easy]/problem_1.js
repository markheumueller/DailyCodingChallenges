const addUpToK = (numbers, k) => {
    return numbers.some((n, i, a) => {
        const otherNumbers = a.slice();
        otherNumbers.splice(i, 1);

        return otherNumbers.indexOf(k - n) !== -1;
    });
}

const tests = [
    {
        numbers: [10, 15, 3, 7],
        k: 17,
        shouldEqual: true
    },
    {
        numbers: [10, 15, 3, 7],
        k: 25,
        shouldEqual: true
    },
    {
        numbers: [1, 1],
        k: 3,
        shouldEqual: false
    },
]

tests.forEach(t => {
    console.log(
        `numbers [${t.numbers.join(', ')}] and K = ${t.k}`,
        'solved:',
        t.shouldEqual === addUpToK(t.numbers, t.k)
    );
});
