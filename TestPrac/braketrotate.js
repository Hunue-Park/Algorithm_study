const bras = "([{)}]"
// const bras = "}]()[{";

function solution(s) {
  let localBras = s;

  const pair = { "}": "{", "]": "[", ")": "(" };

  const isValid = (arr) => {
    const stack = [];
    for (let i = 0; i < arr.length; i++) {
      const c = arr[i];
      // ( { [ 얘네들은 value가 없어서 undefined 가 나올테니 push 한다. 
      if (pair[c] === undefined) stack.push(c);
      else {
        if (stack[stack.length - 1] !== pair[c]) {
          // 바로 마지막으로 스택에 들어간게 짝이 맞는 친구가 아니라면 
          // 유효한 괄호열이 아닌것 
          return false;
        }
        stack.pop();
      }
    }
    if (stack.length) return false;
    return true;
  };

  function shiftBra(s) {
    let arr = [...s];
    let firstBra = arr.shift();
    arr.push(firstBra);
    return arr;
  }

  var answer = 0;

  for (let i = 0; i < s.length; i++) {
    let newArr = shiftBra(localBras);
    if (isValid(newArr)) {
      answer += 1;
    }
    localBras = newArr;
  }

  return answer;
}

console.log(solution(bras));
