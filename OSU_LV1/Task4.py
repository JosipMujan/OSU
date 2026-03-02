word_counts = {}
fhand = open(r'C:\Users\mujan\OneDrive\Desktop\Osnove strojnog učenja\LV1 Uvod u programski jezik Python-20260225\song.txt')
    
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

print(f"Broj riječi koje se pojavljuju samo jednom: {len(once_words)}\n {once_words}")
