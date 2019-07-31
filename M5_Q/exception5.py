try:
    with open("data.txt") as f:
        linecount = 0
        wordcount = 0
        lst = []
        lines = f.readlines()
        for line in lines:
            linecount +=1
            words = line.split()
            for word in words:
                lst.append(word)
                wordcount +=1
        print(linecount)
        print(wordcount)

        print(lst)
            
except Exception as e:
    print(f"File not found please check path {e}")
