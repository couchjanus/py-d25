# 11.file.truncate.py

# file.truncate ([размер])
# Усекает размер файла. 

# Если указан необязательный аргумент размера, 
# файл усекается до (максимально) этого размера.

# Open a file
fooh = "foo.txt"

fo = open(fooh, "r+")

str = fo.read()
print ("Before : ", str)

fo.truncate(300)
fo.close()

fo = open(fooh, "r+")
str = fo.read()
print ("After : ", str)

fo.close()