# 09.tell.test.py
# После того как вы вызвали метод read() на файловом объекте, 
# если вы повторно вызовете read(), то увидите лишь пустую строку. 
# Это происходит потому, что после первого прочтения 
# указатель находится в конце файла. 
# Для того чтобы узнать позицию указателя можно использовать метод tell().

# Метод tell() сообщает текущую позицию в файле; 
# следующее чтение или запись будет происходить с таким количеством байтов от начала файла.

# Метод seek (offset [, from]) изменяет текущую позицию файла. 
# Аргумент смещения указывает количество байтов для перемещения. 
# Аргумент from указывает ссылочную позицию, из которой должны быть перемещены байты.

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10)
print ("Again read String is : ", str)
# Close opend file
fo.close()

# Read String is :  Python is
# Current file position :  10
# Again read String is :  Python is
