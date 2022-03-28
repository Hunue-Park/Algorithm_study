function solution(a) {
    var size = a.length;
    var left = new Array(size);
    var right = new Array(size);

    left[0] = a[0];
    right[size - 1] = a[size - 1];
    console.log(left, "이전 left")
    for (let i = 1; i < size; i++) {
        left[i] = Math.min(left[i - 1], a[i]);
    }
    for (let i = size - 2; i >= 0; i--) {
        right[i] = Math.min(right[i + 1], a[i]);
    }
    console.log(left, "이후 left")
    const map = new Map();
    for (let i = 0; i < size; i++) {
        map.set(left[i]);
        map.set(right[i]);
    }
    console.log(map, '맵은 또 뭐야')
//     Array 와는 다르게 Set 은 같은 value 를 2번 포함할 수 없음
//  따라서 Set 에 이미 존재하는 값을 추가하려고 하면 아무 일도 없음 
// 이걸로 중복제거를 생각하네.... 레전드네. 
    var answer = map.size;
    return answer;
}

console.log(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]));