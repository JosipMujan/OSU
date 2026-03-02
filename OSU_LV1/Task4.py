word_counts = {}
fhand = open("song.txt", encoding="utf-8")
for line in fhand:
       
    line = line.rstrip()
    words = line.split()
      
    for word in words:   
         word = word.lower()
            
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1
                
fhand.close()

once_words = []
for word in word_counts:
    if word_counts[word] == 1:
        once_words.append(word)

print(f"Words that appear only once: {len(once_words)}\n {once_words}")
