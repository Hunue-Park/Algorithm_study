// 특정배열에서 특정 원소가 몇번 사용되었는지 뽑아내주는 함수.
const counts = a.reduce((acc, cur) => {
    acc[cur] ? acc[cur][1]++ : acc[cur] = [cur, 1];
    return acc;
  }, []).filter(el => el).sort((a, b) => b[1]-a[1]);



// 두 배열에서 내적을 구해주는 함수.
const innerproducts = a.reduce((acc, _, i) => acc += a[i] * b[i], 0);


// 배열의 합
const reducer = (accumulator, curr) => accumulator + curr;
console.log(arr.reduce(reducer));