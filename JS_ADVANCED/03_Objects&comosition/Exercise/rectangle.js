function rectangle (width,height,color){
    const colorCapitalized = color.charAt(0).toUpperCase() + color.slice(1)
    let obj = {
        width:width,
        height:height,
        color:colorCapitalized,
        calcArea:function (){return width*height}
    }

    return obj
}

let rect = rectangle(4, 5, 'red');
console.log(rect.width);
console.log(rect.height);
console.log(rect.color);
console.log(rect.calcArea());
