const n = 5;
const info = [2,1,1,1,0,0,0,0,0,0,0]

function solution (n, info) {
    let difMax = 0;
    let infoR = new Array(11).fill(0);

    // board 는 infoR 을 채우기 위함.
    const arrow = (scoreP, scoreR, count, index, board) => {
        if (n < count) return;
        // 다 채웠다면
        if (index > 10) {
            let dif = scoreR - scoreP;
            if (dif > difMax) {
                board[10] = n - count;
                difMax = dif;
                infoR = board;
            }
            return;
        }
        // 아직 다 안쐈다면
        if (n > count) {
            let board2 = [...board];
            // +1 만큼 더 쏴야 이길 수 있다.
            board2[10 - index] = info[10 - index] + 1;
            arrow(scoreP, scoreR + index, count + info[10 - index] + 1, index + 1, board2);
        }
        // peach 의 점수를 채우는 재귀도 진행시켜야 함. board에다가 채움.
        if (info[10 - index] > 0) {
            arrow(scoreP + index, scoreR, count, index + 1, board)
        } else {
            arrow(scoreP, scoreR, count, index + 1, board)
        }
    }
    arrow(0, 0, 0, 0, infoR);

    if (difMax <= 0) return [-1];
    else return infoR;
}

solution(n, info);