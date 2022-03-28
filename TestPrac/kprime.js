// 0P0처럼 소수 양쪽에 0이 있는 경우
// P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
// 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
// P처럼 소수 양쪽에 아무것도 없는 경우
// 1 ≤ n ≤ 1,000,000
// 3 ≤ k ≤ 10

const n = 524287;
const k = 2;

function solution(n, k) {
  function primeCheck(num) {
    if (num === "1") return false;
    if (num === "") return false;
    if (num === "2") {
      return true;
    }

    for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
      if (num % i === 0) {
        // 한 번이라도 나누어 졌으니 소수가 아니므로 return false
        return false;
      }
    }
    // 나눠진 수가 없다면 해당 수는 소수이므로 return true
    return true;
  }

  let answer = 0;
  let cvrtNumber = n.toString(k).split("0");
  for (let i = 0; i < cvrtNumber.length; i++) {
    if (primeCheck(cvrtNumber[i]) === true) {
      answer++;
    }
  }

  return answer;
}

console.log(solution(n, k));
