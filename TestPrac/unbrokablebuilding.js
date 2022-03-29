const board = [[1,2,3],[4,5,6],[7,8,9]];
const skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]; // [type, r1, c1, r2, c2, degree]
// type 1 이면 공격, 2이면 회복


function solution(board, skill) {
    const prefixSum = Array.from(
        { length: board.length + 1 },
        (_) => new Array(board[0].length + 1).fill(0)
    );

    skill.forEach((el) => {
        const [type, r1, c1, r2, c2, degree] = el;
        const sum = type === 1 ?
            -degree :
            degree;
        prefixSum[r1][c1] += sum;
        prefixSum[r2 + 1][c2 + 1] += sum;
        prefixSum[r1][c2 + 1] -= sum;
        prefixSum[r2 + 1][c1] -= sum;
    });
    console.log(prefixSum, "더하기전 값 적용만")
    for (let r = 0; r < prefixSum.length; r++) {
        for (let c = 1; c < prefixSum[0].length; c++) {
            prefixSum[r][c] += prefixSum[r][c - 1];
        }
    }
    console.log(prefixSum, "아래 위 합 적용")
    for (let r = 1; r < prefixSum.length; r++) {
        for (let c = 0; c < prefixSum[0].length; c++) {
            prefixSum[r][c] += prefixSum[r - 1][c];
        }
    }
    console.log(prefixSum, "왼쪽 오른쪽 합 적용")
    prefixSum.forEach((row, rdx) => {
        row.forEach((col, cdx) => {
            if (board[rdx] && board[rdx][cdx]) {
                board[rdx][cdx] += col;
            }
        });
    });


    return board.reduce((result, row) =>
        result + row.reduce((result, current) =>
            current > 0 ?
                result + 1 :
                result
            , 0)
        , 0);
}

console.log(solution(board, skill));

