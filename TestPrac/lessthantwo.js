const numbers = [10,12,9,15,3,100000];

function solution(numbers) {

    let answer = [];
    for (let i = 0; i < numbers.length; i++) {
        let current = numbers[i];
        if (current % 2 === 0) {
            answer.push(current + 1);
        } else {
            // 홀수면 싹다 11111 이라 0이 안나올 수도 잇으니까
            current = '0' + current.toString(2);
            let totalLength = current.length;
            for (let j = totalLength - 1; j >= 0; j--) {
                if (+current[j] === 0) {
                    answer.push(
                        parseInt(
                            current.substring(0, j) + '10' + current.substring(j + 2, totalLength), 2
                        ) // 01을 제거하고 10 으로 바꾼다. 
                    );
                 break;   
                }
            }
        }
    }
    return answer;
}

console.log(solution(numbers));