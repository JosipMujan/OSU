word_count = {}

fhand = open("song.txt")

for line in fhand:

    line = line.rstrip()
    words = line.split()

    for word in words:
        word = word.lower()

        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

fhand.close()

once_words = []
for word in word_count:
    if word_count[word] == 1:
        once_words.append(word)

print(f"Number of words taht appear only once: {len(once_words)}\n {once_words}")
