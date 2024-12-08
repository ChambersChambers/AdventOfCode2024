
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


if __name__ == "__main__":
    main()
