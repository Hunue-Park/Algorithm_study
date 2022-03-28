# 장르별 가장 많이 재생된 노래 목록! 장르별 두개씩만
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

from collections import defaultdict
from operator import itemgetter

def solution(genres, plays):
    genre_play_dict = defaultdict(lambda: 0)
    for genre, play in zip(genres, plays):
        genre_play_dict[genre] += play
    
    genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), 
                key=itemgetter(1), reverse=True)]
    
    final_dict = defaultdict(lambda: [])
    for i, genre_play_tuple in enumerate(zip(genres, plays)):
        final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))

    
    answer = []
    for genre in genre_rank:
        one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
        if len(one_genre_list) > 1:
            answer.append(one_genre_list[0][1])
            answer.append(one_genre_list[1][1])
        else:
            answer.append(one_genre_list[0][1])
            
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],
        [500, 600, 150, 800, 2500]))


