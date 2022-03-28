import heapq

def Solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    while i < len(jobs):
        for j in jobs:
            # j[0]은 시작시간
            if start < j[0] <= now:
                # 종료시간이 가장 먼저 끝나는 순서대로 heap에 집어넣는다.
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]  #current[0] = j[1] = 종료시간
            answer += (now - current[1])
            i += 1
        else:
            now += 1  
            # +1 씩 올려가며 카운팅 어차피 heap에 아무것도 안들어가면
            # 다시 여기로 와서 now + 1할테니까
    return int(answer / len(jobs))    