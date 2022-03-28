function solution(numbers) {

    function combination(arr, selectNum) {
        const result = [];
        if (selectNum === 1) return arr.map((v) => [v]);
        arr.forEach((v, idx, arr) => {
          const fixed = v;
          const restArr = arr.slice(idx + 1);
          const combinationArr = combination(restArr, selectNum - 1);
          const combineFix = combinationArr.map((v) => [fixed, ...v]);
          result.push(...combineFix);
        });
        return result;
    }
    
    
    function makeResult(arr) {
        let result = combination(arr, 2);
        var answer = [];
        for (let i = 0; i < result.length; i++) {
            answer.push(result[i][0] + result[i][1])
        }

        return answer
    }

    const answer_list = makeResult(numbers);
    const set = new Set(answer_list);
    const uniqueArr = [...set]
    uniqueArr.sort(function(a, b) {
        if( a > b ) return 1;
        if( a === b ) return 0;
        if(a < b) return -1;
    });
    return uniqueArr;
}

let numbers = [2, 1, 3, 4, 1];

console.log(solution(numbers));


