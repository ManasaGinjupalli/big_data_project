s = open("02.txt","r") # To read the file created from sortshuffle
r = open("03.txt", "w") # To generate a file and write output into it

thisKey = ""
thisValue = 0.0
av =0

for line in s:
  data = line.strip().split('\t')
  author, average_rating = data

  if author != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(av/thisValue)+'\n')

    # start over when changing keys
    thisKey = average_rating
    thisValue = 0.0
    av =0.0
  
  # apply the aggregation function
  thisValue += 1
  av += float(thisValue)

# output the final entry when done
r.write(thisKey + '\t' + str(av/thisValue)+'\n')

s.close()
r.close()