const cards = [[10, 5, 15], [8, 9, 13], [10, 10, 10]]


function solution(cards) {

    function isChangable(arr1, arr2) {
        let min1 = Math.min(...arr1);
        let min2 = Math.min(...arr2);
        let index1 = arr1.indexOf(min1);
        let index2 = arr2.indexOf(min2);
        // 둘다 같은 색을 원하는 경우 교환 불가능
        if (index1 === index2) {
            return false;
        }
        // 원하는 색은 다르지만 교환했을때 이득이 없다면 교환 불가능.
        if (((arr1[index2] - 1) <= min1) || (arr2[index1] - 1 <= min2)) {
            return false;
        }

        return true;
    }

    console.log(isChangable(cards[0], cards[2]));




    var answer = -1;
    return answer;
}

solution(cards);