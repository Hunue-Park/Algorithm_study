// a의 길이는 2 이상 300,000 이하입니다.
// a의 모든 수는 각각 -1,000,000 이상 1,000,000 이하입니다.
// a[i]는 i번 정점의 가중치를 의미합니다.

const a = [-5, 0, 2, 1, 2];
const edges = [
  [0, 1],
  [3, 4],
  [2, 3],
  [0, 3],
];

function solution(a, edges) {
  const reducer = (accumulator, curr) => accumulator + curr;
  function isPossible(arr) {
    if (arr.reduce(reducer) === 0) {
      return true;
    } else {
      return false;
    }
  }

  if (isPossible(a) === false) {
      return -1;
  }

  // 여기서 a는 각 노드의 값을 담고 있는 배열이다.
  // 즉 노드 개수만큼의 배열을 만들고 이를 그래프 형태로 활용할 것이다.
  const tree = new Array(a.length).fill().map((_) => []);

  for (const [u, v] of edges) {
    tree[u].push(v);
    tree[v].push(u);
  }

  // 0은 시작노드, -1은 부모노드이다.
  // 위에서와 동일하게 0이 루트이므로 이 경우 부모노드는 -1이다.
  const stack = [[0, -1]];
  // 첫 방문 여부는 모두 false로 초기화한다.
  const visit = new Array(a.length).fill(false);

  let sum = 0n;  //BigInt
  while (stack.length) {
    const [start, parent] = stack.pop();

    // 이미 방문했던 노드를 다시 만나는 시점이 결국
    // 더 이상 내려갈 곳이 없는 노드를 마주한 경우이다.
    if (visit[start]) {
      /* --- 리프노드 영역 --- */
      sum += BigInt(Math.abs(a[start]));
      a[parent] += a[start];
      continue;
    }

    // 위 조건에 걸리지 않는다면 현재 start 노드는
    // 처음 방문하는 노드가 된다.
    // 따라서 해당 노드를 다시 stack에 넣어주고
    // 방문여부를 true 로 변경한다.
    stack.push([start, parent]);
    visit[start] = true;

    // 위 DFS 함수에서 자신을 호출하는 영역과 유사하다.
    // 대신 별도의 visit 배열을 통해 방문여부를 체크한다.
    for (const next of tree[start]) {
      if (!visit[next]) {
        stack.push([next, start]);
      }
    }
  }

  return a[0] ? -1 : sum;
}

console.log(solution(a, edges));
