# reorder data in log files

import heapq
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

#Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
q = []

# for i in range(len(logs)):
#     for j in range(len(logs[i])):
#         if logs[i][j-1] 이 숫자이고 logs[i][j] 가 문자라면:
#             이후 문자열의 아스키 코드순서대로 정렬해서 힙큐에 집어넣음
#         elif logs[i][j-1] 이 숫자이고 logs[i][j] 가 숫자라면:
#             이후 문자열의 아스키 코드 순서대로 정렬해서 힙큐에 집어넣음

# print(q)

# # 그냥 정렬해서 각각 다른 리스트에 넣어놓고 해당 리스트 두개를 합치면 됨. 