def get_word_stats(my_text):
    my_text = my_text.lower()
    all_words = my_text.split()
    counts = {}

    for w in all_words:
 
        w = w.strip(".,") 
        if w in counts:
            counts[w] = counts[w] + 1
        else:
            counts[w] = 1
            
    print("Словник усіх слів:")
    print(counts)
    
    top_words = []
    for key in counts:
        if counts[key] > 3:
            top_words.append(key)
            
    print("Слова, яких більше ніж 3:")
    print(top_words)

input_data = "apple banana apple kiwi apple banana apple orange kiwi apple banana kiwi apple kiwi orange banana"
get_word_stats(input_data)
