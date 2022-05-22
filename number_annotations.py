filename = raw_input("Enter fasta filename to add unique number to beginning of each annotation line:\n")
outname = raw_input("What would you like to name your numbered output file?\n")

with open(filename,'r') as file_raw:
    file = file_raw.read()

output = open(outname,'w')

counter = 0
for c in file:
    output.write(c)
    if c == '>':
        output.write(str(counter))
        counter += 1

output.close()
