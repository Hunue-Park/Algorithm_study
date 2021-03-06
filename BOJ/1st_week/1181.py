# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
# 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
import sys


N = int(sys.stdin.readline())
words = []
for _ in range(N):
    #strip 은 뒤에 따라오는 '\n'을 제거하기 위함, 들어오는 단어들을 리스트에 넣어준다.
    words.append(sys.stdin.readline().strip())

#출력할때 길이순으로 정렬해서 출력.

words_2 = set(words)

new_words = list(words_2)
new_words.sort()
new_words.sort(key=len)

print("\n".join(new_words))
