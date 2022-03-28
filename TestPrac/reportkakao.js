const id_list = ["con", "ryan", "muzi", "frodo", "apeach", "neo"];
const report = ["ryan con", "ryan con", "ryan con", "ryan con", "muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"];
const k = 2;

function solution(id_list, report, k) {
    const answer = new Array(id_list.length).fill(0);
    const reportList = {} //
    
    
    id_list.map((user)=>{
        reportList[user] = [] //key로 userid를 value로 빈 배열을 가지는 객체
    })
    
    report.map((reportCall)=>{
        const [user_id, report_id] = reportCall.split(' ')
        if(!reportList[report_id].includes(user_id)){
            reportList[report_id].push(user_id)
        }        
    })

    
    for(const key in reportList){
        if(reportList[key].length >= k){ //이용정지 유저
            reportList[key].map((user)=>{
                answer[id_list.indexOf(user)] += 1
            })
        }
    }
    return answer;
}

console.log(solution(id_list, report, k));