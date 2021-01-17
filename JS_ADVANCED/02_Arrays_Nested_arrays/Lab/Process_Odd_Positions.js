function oddDoubleReversed(array) {
    return array.filter((a, i) => i % 2 !== 0)
        .map(x => x * 2)
        .reverse()
        .join(' ');
}


oddDoubleReversed([10, 15, 20, 25]);
oddDoubleReversed([3, 0, 10, 4, 7, 3]);
