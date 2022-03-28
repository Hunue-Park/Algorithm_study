from collections import deque

def solution(record):
    # stack part
    stack = []
    total_profit = 0
    for elements in record:
        sub = elements.split(' ')
        if sub[0] == 'P':
            for _ in range(int(sub[2])):
                stack.append(sub[1])
        elif sub[0] == 'S':
            for _ in range(int(sub[2])):
                print(stack)
                price = int(stack.pop())
                total_profit += price
    a = total_profit
    # queue part
    q = deque()
    total_profit_q = 0
    for elements in record:
        sub = elements.split(' ')
        if sub[0] == 'P':
            for _ in range(int(sub[2])):
                q.append(sub[1])
        elif sub[0] == 'S':
            for _ in range(int(sub[2])):
                price = int(q.popleft())
                total_profit_q += price
    b = total_profit_q
                
                
                
    answer = [b, a]
    return answer

record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]
print(solution(record))