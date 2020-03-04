unsorted = open("01.txt", "r") #To read the output file generated by mapper code
sorted = open("02.txt", "w") #To write the output into generated 02.txt file

dataList = unsorted.readlines()
dataList.sort()
#To sort the data generated
for line in dataList:
    print (line)
    sorted.write(line)

unsorted.close()
sorted.close()
#To close read and write operations