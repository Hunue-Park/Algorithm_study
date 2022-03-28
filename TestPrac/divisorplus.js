// left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
const left = 1;
const right = 1;

function solution(left, right) {
    var answer = 0;


    function divisor(number) {
        if (number === 1) {
            return true;
        }
        let isOdd = false;
        let counts = 2; // 1과 자기자신을 이미 포함한 상태에서 출발
        for (let i = 2; i < number; i++) {
            if (number % i === 0) {
                counts += 1;
                continue;
            }
        }
        if (counts % 2 === 0) {
            isOdd = false;
            return isOdd;
        } else if (counts % 2 != 0) {
            isOdd = true;
            return isOdd;
        }
    }

    for (let i = left; i < right + 1; i++) {
        if (divisor(i)) {
            answer -= i;
            continue;
        } else if (!divisor(i)) {
            answer += i;
            continue;
        }
    }


    return answer;
}

console.log(solution(left, right));