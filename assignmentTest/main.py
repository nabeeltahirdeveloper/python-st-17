def words():
    file = open("assignmentTest\story.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for w in words:
        if w =="the" or w =="The":
            count += 1
    print(count)
    file.close()

words()


