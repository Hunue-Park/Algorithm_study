const a = [0,3,3,0,7,2,0,2,2,0];


function solution (a) {
    let answer = 0;
    const counts = a.reduce((acc, cur) => {
      acc[cur] ? acc[cur][1]++ : acc[cur] = [cur, 1];
      return acc;
    }, []).filter(el => el).sort((a, b) => b[1]-a[1]);
    console.log(counts) // counts 는 각 원소가 몇번씩 사용됬는지 확인. 
    for(let i = 0; i < counts.length; i++) {
      if(answer >= counts[i][1]) continue;
      
      let count = 0; // 매번 초기화 해주는 count. 
      // 이전 카운트의 값들은 answer에 담아놓으면서 최대값으로 갱신해나간다. 
      
      for(let j = 0; j < a.length; j++) {
        if(a[j+1] === undefined) continue;
        if(a[j] === a[j+1]) continue;
        if(a[j] !== counts[i][0] && a[j+1] !== counts[i][0]) continue;
        
        count++;
        j++; // 조건을 통과했을 경우에만 j + 1해주면서 두칸씩 증가하지 않아도 된다.
      }
      
      answer = Math.max(answer, count);
    }
    
    return answer * 2;
  }

console.log(solution(a));