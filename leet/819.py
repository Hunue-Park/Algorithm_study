# most common word

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
changed = paragraph.replace(",", "")
more_changed = changed.replace(".", "")
new_paragraph = more_changed.lower()

str_list = list(new_paragraph.split())

histogram = {}

for word in str_list:
    histogram[word] = histogram.get(word, 0) + 1

for i in range(len(banned)):
    target_word = banned[i]
    del histogram[target_word]


print(f'"{max(histogram,key=histogram.get)}"')
