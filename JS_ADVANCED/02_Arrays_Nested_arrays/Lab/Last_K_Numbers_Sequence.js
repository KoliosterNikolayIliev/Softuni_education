function generateSeq(n, k) {
    let outputArr = [1];
    function lastSumK(arr, k) {
        k = arr.length>k ? k : arr.length;
        let sum = 0;
        for(let i = 1; i<=k; i++){
            sum += arr[arr.length-i];
        }
        return sum;
    }
    for(let i = 1; i<n; i++){
        outputArr[i] = lastSumK(outputArr, k);
    }
    return outputArr;

}

generateSeq(6,3)
generateSeq(8,2)