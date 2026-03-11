ham_total_words = 0
ham_msg_count = 0
spam_total_words = 0
spam_msg_count = 0
spam_with_exclamation = 0

fhand = open("SMSSpamCollection.txt")

for line in fhand:
    line = line.rstrip()
    if not line:
        continue

    words = line.split()
    label = words[0]

    msg_content_words = words[1:]
    num_words = len(msg_content_words)

    if label == "ham":
        ham_total_words += num_words
        ham_msg_count += 1
    
    elif label == "spam":
        spam_total_words += num_words
        spam_msg_count += 1

        if line.endswith("!"):
            spam_with_exclamation += 1

fhand.close()

if ham_msg_count > 0:
    avg_ham = ham_total_words / ham_msg_count
    print(f"Average number of words in harmful messages: {avg_ham}")
if spam_msg_count > 0:
    avg_spam = spam_total_words / spam_msg_count
    print(f"Average number of words in spam messages: {avg_spam}")
    print(f"Number of spam SMS that start with !: {spam_with_exclamation}")
