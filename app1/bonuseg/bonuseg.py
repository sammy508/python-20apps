content =[ 'it will be written in file one', 'It will be written in file B', 'It was written in file C']

file_name = ['bfile1.txt', 'bfile2.txt', 'bfile3.txt']

# for  i in range (len(content)):
#     file = open(file_name[i], 'w')
#     data = file.writelines(content[i])
#     file.close()
    
# for i in range(len(file_name)):
#     filenam = file_name[0]
#     fileOp = open(filenam, 'r')
#     data = file.readlines(int(content[i]))
#     file.close()
    


# instead we also can use zip function
# Have to fix? 
#  heres  a error on that particular line (file = open(file_name, 'r')
#            ^^^^^^^^^^^^^^^^^^^^)

for index, filename in  zip(content, file_name):
    file = open(file_name, 'w')
    data = file.writelines(content)
    file.close()


# here by this approach we can modify the item if the list
# filename_replace = [filename.replace('b','bon') for filename in file_name]
# print(filename_replace)

# output:
#     ['bonfile1.txt', 'bonfile2.txt', 'bonfile3.txt']

    
