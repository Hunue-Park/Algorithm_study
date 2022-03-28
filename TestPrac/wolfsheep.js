const info = [0,1,0,1,1,0,1,0,0,1,0];
const edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]];

function solution(info, edges) {
    let answer = 1;
    const length = info.length;
    const graph = Array.from({length}, () => []);
    
    const dfs = (current, nextNodes) => {
        let [currentNode, sheep, wolves] = current;
        const newNextNodes = [...nextNodes];
        const index = newNextNodes.indexOf(currentNode);
        
        sheep += !info[currentNode];
        wolves += info[currentNode];
        answer = Math.max(answer, sheep);
        
        if(sheep === wolves){
            return;
        }
        
        if(graph[currentNode].length){
            newNextNodes.push(...graph[currentNode]);
        }
        newNextNodes.splice(index, 1); // current 를 빼는것뿐s
        
        for(const nextNode of newNextNodes){   
            dfs([nextNode, sheep, wolves], newNextNodes);
        }
    }
    
    for(let i = 0; i < edges.length; i++){
        const [from, to] = edges[i];
        
        graph[from].push(to);
    }
    
    dfs([0, 0, 0], [0]);
    
    return answer;
}

solution(info, edges);