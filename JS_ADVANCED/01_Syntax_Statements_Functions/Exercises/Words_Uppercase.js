function solve(string){
    let output='';
    let regex = /\w+/g;
    let matches = string.match(regex)
    let counter = 0
    for (const match of matches) {
        counter+=1
        let last = matches.length === counter ? '':', '
            output+=match.toUpperCase() + last
    }
    console.log(output)
}

solve('Hi, how are you?')
solve('hello')