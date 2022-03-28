// 특정 숫자를 골랐을때 자신보다 작은 숫자가 왼쪽 아니면 오른쪽 둘중 한쪽에만 있어야 함. 


const a = [-16,27,65,-2,58,-92,-71,-68,-61,-33];
// const a = [9,-1,-5];

function solution(a) {

    function toLeft(arr, index) {
        let startValue = arr[index];
        let findFlag = false;
        if (index == 0) {
            return false;
        }
        let sliceArr = arr.slice(0, index);
        let minValue = Math.min(...sliceArr);
        if (minValue < startValue) {
            findFlag = true;
        }
        
        return findFlag;
    }

    function toRight(arr, index) {
        let startValue = arr[index];
        let findFlag = false;
        if (index == 0) {
            return false;
        }
        let sliceArr = arr.slice(index + 1, arr.length + 1);
        let minValue = Math.min(...sliceArr); // nan 나온다. array 넣는데 에러인듯. 
        if (minValue < startValue) {
            findFlag = true;
        }
        
        return findFlag;
    }

    let findCount = 0;

    for (let i = 0; i < a.length; i++) {
        if (toLeft(a, i) && toRight(a, i)) {
            continue;
        } else {
            findCount += 1;
            continue;
        }
    }


    return findCount;
}

console.log(solution(a));