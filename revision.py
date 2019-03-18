# def add_one(x, y):
#     print("python rocks")
#     return "python sux"
#
# print(add_one(3, 2))

fh = open("simple.txt", "r")
# lines_of_text = ["a line of text", "another line of text", "a third line"]
# fh.writelines(lines_of_text)

# fh.readline()


writeText = []
for line in fh.readlines():
    line = line.strip() #returns a string
    # '3 ' -> '3'
    line = line.split(' ')
    # '3 2 1' -> ['3', '2', '1']
    line = [int(e) for e in line if e != '']
    # ['3', '2', '1'] -> [3, 2, 1]
    line.append((line[0] ** 2 + line[1] ** 2)**0.5)
    # [3, 2, 1] -> [3, 2, 1, 20]

    line = [str(e) for e in line]
    # [3, 2, 1, 20] -> ["3", "2", "1", "20"]
    line = " ".join(line)
    # ["3", "2", "1", "20"] -> "3 2 1 20"
    line += "\n"
    print(line)
    writeText.append(line)

fh.close()

fh = open("simple.txt", "w")

fh.writelines(writeText)

fh.close()
