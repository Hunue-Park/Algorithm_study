# 2019 KAKAO BLIND 기출

# 닉네임을 변경할때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다. 

# 모든 유저는 유저아이디로 구분한다. uid

# 채팅방에서 닉네임을 변경하는방법은 두가지 뿐. 
#     채팅방을 나간 후 새로운 닉네임으로 다시 들어간다.
#     채팅방에서 닉네임을 변경한다. 

from functools import partialmethod


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
        "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", 
#         "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

uid_nickname = {}

# print(record[1].split())   ['Enter', 'uid4567', 'Prodo']

# a = record[1].split()
# print(a[1])      uid4567

for i in range(len(record)):
    cmdline = record[i].split()
    if cmdline[0] != "Leave":
        uid_nickname[cmdline[1]] = cmdline[2]

result = []

for i in range(len(record)):
    parsing = record[i].split()
    if parsing[0] == "Enter":
        name = uid_nickname[parsing[1]]
        result.append(f"{name}님이 들어왔습니다.")
    elif parsing[0] == "Leave":
        name = uid_nickname[parsing[1]]
        result.append(f"{name}님이 나갔습니다.")
    else:
        continue
print(result)
    


