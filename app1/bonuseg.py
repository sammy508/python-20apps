content =[ 'it will be written in file one', 'It will be written in file B', 'It was written in file C']

file_name = ['bfile1.txt', 'bfile2.txt', 'bfile3.txt']

for  i in range (len(content)):
    file = open(file_name[i], 'w')
    data = file.writelines(content[i])
    file.close()
    
for i in range(len(file_name)):
    filenam = file_name[0]
    fileOp = open(filenam, 'r')
    data = file.readlines(int(content[i]))
    file.close()
    

    
