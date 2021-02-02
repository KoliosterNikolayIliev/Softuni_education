function encodeAndDecodeMessages() {
    document.getElementById('main').addEventListener('click', convert);
    let string = document.getElementsByTagName('textarea')[0];
    let stringDecode = document.getElementsByTagName('textarea')[1];
    let asciiEncode;

    function convert(event) {
        if (string.value.length > 0) {
            asciiEncode = string.value.split('');
        }
        if (event.target.innerHTML === 'Encode and send it') {
            asciiEncode.forEach((item, index, array) => array[index] = String.fromCharCode(item.charCodeAt(0) + 1));
            stringDecode.value = asciiEncode.join('');
            string.value = '';

        }
        if (event.target.innerHTML === 'Decode and read it') {
            asciiEncode.forEach((item, index, array) => array[index] = String.fromCharCode(item.charCodeAt(0) - 1));
            stringDecode.value = asciiEncode.join('');
        }
    }

}


encodeAndDecodeMessages();