i = open("books.txt", "r") #to read the input file books.txt
o = open("farheen01.txt", "w") # to create a file in which output will be stored

for line in i:
    datalist = line.strip().split("\t")
    BookID, title, authors, average_rating, isbn, isbn13, language_code,  num_pages, ratings_count, text_reviews_count = datalist
    o.write(title + "\t" + authors + "\n")
    #for loop to read through the datalist and get required elements from datalist

i.close()
o.close()

#to close the read and write operations




