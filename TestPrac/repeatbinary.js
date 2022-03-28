// x의 모든 0을 제거합니다.
// x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.

// 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.

function solution(s) {
    let delCount = 0;
    let totCount = 0;

    function binaryTrans(str) {
        let newStr = str.replace(/0/g,'');
        let c = newStr.length;
        let a = str.length;
        delCount += a - c;
        let newBinary = c.toString(2);
        return newBinary;
    }

    function recur(str) {
        if (str === '1') {
            return;
        }

        totCount += 1;

        return recur(binaryTrans(str));
    }


    recur(s);
    var answer = [];
    answer.push(totCount);
    answer.push(delCount);
    return answer;
}

let strings = '110010101001'

console.log(solution(strings));