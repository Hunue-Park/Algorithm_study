// 당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
// 만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
// 그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤, 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.

const arr = [
  [1, 1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 1, 1, 1, 1],
  [0, 1, 0, 0, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 1],
  [0, 0, 0, 0, 1, 1, 1, 1],
];

function solution(arr) {


  var answer = [];
   // 전체 0, 1 개수 구하기. 
   let totNum = (arr.length) ** 2
   
    // arr 에 들어있는 1의 개수 구하기. 
    let newArr = arr.join().split(',');
    let numArr = newArr.map(Number);
    const reducer = (accumulator, curr) => accumulator + curr;
    let oneNum = numArr.reduce(reducer);
    let zeroNum = totNum - oneNum;

    function squareSum(xStart, yStart, cols) {
      let localSum = 0;
      for (let i = xStart; i < (xStart + cols); i++ ) {
        for (let j = yStart; j < (yStart + cols); j++ ) {
          localSum += arr[i][j];
        }
      }

      return localSum;
    }


    function dfs(xStart, yStart, cols) {
      
      // s 영역안의 값이 같으면 개수를 바꾸고 dfs 리턴
      if (squareSum(xStart, yStart, cols) === 0) {
        zeroNum = zeroNum - (cols ** 2) + 1;
        return;
      } else if (squareSum(xStart, yStart, cols) === (cols ** 2)) {
        oneNum = oneNum - (cols ** 2) + 1;
        return;
      } else if (cols / 2 === 1) {
        return;  // 종료조건, 더이상 쪼개지않고 0,1 개수도 변화시키지 않음. 
      }

      
      //s 영역안의 값이 같지 않을때 4개로 쪼개고 dfs 들어감
      dfs(xStart, yStart, cols / 2);
      dfs(xStart + cols / 2, yStart, cols / 2);
      dfs(xStart, yStart + cols / 2, cols / 2 );
      dfs(xStart + cols / 2, yStart + cols / 2, cols / 2);
    }

    dfs(0, 0, arr.length);


    answer.push(zeroNum);
    answer.push(oneNum);
  
  return answer;
}

console.log(solution(arr))
