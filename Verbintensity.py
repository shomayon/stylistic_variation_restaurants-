file = open("C:\\Users\\shide\\Desktop\\Independent study\\data.txt")
counter = 1
stronger = {}
strongerverb = []
secondverb = []
term = "[stronger-than]" #Look for stronger-than
for line in file:  #Skip the 13First line
    if counter < 13:
        counter = counter + 1
        continue
    else:

     words = line.split()  #split sentence
    if term in words:  #if exists then add the first word
     strongerverb.append(line.split(None, 1)[0]) # add only first word
     secondverb.append(line.split()[2])  #add second verb

capacity = len(strongerverb)

index = 0
while index!=capacity:
    line = strongerverb[index]
    for word in line.split():
        print(word)
        index = index+1
#print("First verb:",firstverb)
#print("Second verb:",secondverb)
for i in range(len(strongerverb)):
    stronger[strongerverb[i]] = secondverb[i]
    print(stronger)