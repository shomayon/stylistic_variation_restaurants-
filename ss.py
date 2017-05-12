file = open("C:\\Users\\shide\\Desktop\\Independent study\\verbocean\\test.txt")
QuizList = []
for line in file:
    QuizList.append(line.split(None, 1)[0])

  #  QuizList.append(line)
capacity = len(QuizList)
#capacity = capacity-1
index = 0
while index!=capacity:
    line = QuizList[index]
    for word in line.split():
        print(word)
        index = index+1
