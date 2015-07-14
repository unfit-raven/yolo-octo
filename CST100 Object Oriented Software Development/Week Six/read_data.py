# For loop to read contents of a file
# qbfile = open("qbdata.txt", "r")
#
# for aline in qbfile:
# values = aline.split()
#     print(values[2], values[0], values[1], 'had a completion rating of', values[9], 'and a QB rating of', values[10])
#
# qbfile.close()

# print()

# While loop to read the contents of a file, and print output to another file
infile = open("qbdata.txt", "r")
outfile = open("qbcompletionrating.txt", "w")

line = infile.readline()
while line:
    values = line.split()
    data_line = values[2] + " " + values[0] + " " + values[1] + " had a completion rating of " \
               + values[9] + " and a QB rating of " + values[10]
    outfile.write(data_line + '\n')
    line = infile.readline()

infile.close()
outfile.close()