def wordcount(input_filename):
    word_count = {}
    file = open(input_filename)
    for line in file:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            #print word
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1 
    
    for word, count in word_count.items():
        print "%s: %d" %(word, count)

wordcount("test.txt")
