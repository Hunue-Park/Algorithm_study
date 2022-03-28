# 전화번호 중, 한 번호가 다른 번호의 접두어 인 경우가 있는지 확인. 

def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    
    return True

print(solution(["6", "12", "6789"]))