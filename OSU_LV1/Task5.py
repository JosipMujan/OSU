ham_total_words = 0
ham_msg_count = 0
spam_total_words = 0
spam_msg_count = 0
spam_with_exclamation = 0

try:
    
    fhand = open("SMSSpamCollection.txt", encoding='utf-8')
    
    for line in fhand:
        line = line.rstrip()
        if not line:
            continue
            
        # Prva riječ je oznaka (ham/spam), ostalo je sadržaj poruke
        words = line.split()
        label = words[0]

        msg_content_words = words[1:]
        num_words = len(msg_content_words)
        
        if label == 'ham':
            ham_total_words += num_words
            ham_msg_count += 1
            
        elif label == 'spam':
            spam_total_words += num_words
            spam_msg_count += 1
            
            if line.endswith('!'):
                spam_with_exclamation += 1
                
    fhand.close()

    if ham_msg_count > 0:
        avg_ham = ham_total_words / ham_msg_count
        print(f"Prosječan broj riječi u ham porukama: {avg_ham:.2f}")
    
    if spam_msg_count > 0:
        avg_spam = spam_total_words / spam_msg_count
        print(f"Prosječan broj riječi u spam porukama: {avg_spam:.2f}")

    print(f"Broj spam poruka koje završavaju uskličnikom: {spam_with_exclamation}")

except FileNotFoundError:
    print("Pogreška: Datoteka SMSSpamCollection.txt nije pronađena.")