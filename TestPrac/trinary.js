function solution(n){
    return parseInt(n.toString(3).split("").reverse().join(''), 3)
}

var n = 125;


console.log(solution(n));