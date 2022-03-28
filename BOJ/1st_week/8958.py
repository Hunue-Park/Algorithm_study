# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
# 문자열은 O와 X만으로 이루어져 있다.
#T = int(input())
T = 1
#OX 문자열을 해당하는 점수로 변환시켜 리스트에 집어넣는 함수
def cvrt_nums(a,b):
    #OX 리스트의 인덱스를 읽어들임. 1~b 까지. 여기서 b를 변수로 준 이유는 들어오는 배열마다 길이가 다르기 때문. 혹은 시작점과 끝점을 지정.
    for i in range(1,b):
        
        #i 번째 값이 O일때 그 전값과 비교하여 O 이면 점수를 1점 올린다. 
        if OXs[i] == 'O' and OXs[i-1] == 'O':
            cnt = 1
            #1점 올린 점수는 그 이전의 점수에 더해서 계속해서 더해지도록함 ex) 1 + 2, 1 + 2 + 3... 
            cnt = cnt + cnvt_nums[i-1]
            #외부 리스트에서 값을 받아와야 초기화 되지 않는다. 
            cnvt_nums.append(cnt)
            #연속된 O 구간이 끝날때까지 반복한 다음 최종 점수를 cnvt_num 리스트에 집어넣는다. 그러면 원래 배열의 'O'에 해당하는 자리의 점수가 집어넣어진다.
        #i 번째 값이 0일때, 그 전값과 비교하여 X 이면 그냥 1점을 cnvt_num 리스트에 집어넣는다.
        elif OXs[i] == 'O' and OXs[i-1] == 'X':
            
            cnt = 1
            cnvt_nums.append(cnt)
        #i 번째 값이 X 일때 해당하는 점수는 0점이므로 이를 cnvt_num 리스트에 집어넣는다. 
        elif OXs[i] == 'X':
            cnt = 0
            cnvt_nums.append(cnt)


        
          


for _ in range(T):
    OXs = list(input())
    cnvt_nums = []
    b = len(OXs)
    
    #맨처음 OX 배열의 값이 O 인 경우와 X 인경우를 나누는 이유는 [i-1] 을 추적하는 함수이므로 
    #시작이 X 로시작되면 이후의 모든 값을 계속해서 0점으로 초기화하기때문.
    if OXs[0] == 'O':
        cnvt_nums.insert(0,1)
        cvrt_nums(1,b)
    elif OXs[0] == 'X':
        cnvt_nums.insert(0,0)
        cvrt_nums(1,b)
    #최종적으로 cnvt_nums에 모여진 숫자들을 다 더하면 해당 OX 배열의 점수가 된다. 
    print(sum(cnvt_nums))

        
    
