myFileNumberArray = open("Untitled 12.txt").readlines()
for item in myFileNumberArray:
    rest = item.split(" ", 1)[0]
    rest2 = rest.split(",", 1)[0]
    print rest2