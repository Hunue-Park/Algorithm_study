function solution(a, b) {
    var answer = 0;

    for (let i = 0; i < a.length; i++) {
        answer += a[i] * b[i];
        console.log(answer)
    }
    
    return answer;
}

let a = [1, 2, 3, 4];
let b = [2, 3, 4, 5];

console.log(solution(a, b));