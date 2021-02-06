function solve() {
    let counter = 1;

    return function fibKur() {
        const g = 1.618034;
        let fibNum = Math.floor(((g ** counter) - (1 - g) ** counter) / Math.sqrt(5));
        counter++;
        return fibNum
    };
}

const fBkur = solve();

for (let i = 0; i < 50; i++) {
    console.log(fBkur());
}

