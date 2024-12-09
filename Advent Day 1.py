
def main():
    test()

def test():
    listLeft = []
    listRight= []
    distanceBetween = 0

    input_file = open("input.txt")
    for x in input_file:
        listLeft.append(int(x[:5]))
        listRight.append(int(x[8:13]))

    listLeft.sort()
    listRight.sort()
    
    for x in range(len(listLeft)):
        distanceBetween += abs(listLeft[x] - listRight[x])

    print(distanceBetween)

    #Part 2
    similarityScore = 0
    
    for x in range(len(listLeft)):
        testValue = listLeft[x]

        for y in range(len(listRight)):
            if listRight[y] == testValue:
                similarityScore += listRight[y]
    
    print(similarityScore)


if __name__ == "__main__":
    main()
