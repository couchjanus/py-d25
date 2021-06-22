# 16.mkdir.test.py

import os
# Все файлы содержатся в разных каталогах, и у Python нет проблем с этим. Модуль os имеет несколько методов, которые помогут вам создавать, удалять и изменять каталоги.

# Метод mkdir ()
# Вы можете использовать метод mkdir () модуля os для создания каталогов в текущем каталоге. Вы должны предоставить аргумент этому методу, который содержит имя каталога, который будет создан.
# os.mkdir() в Python используется для создания каталога с именем path с указанным числовым режимом. Этот метод FileExistsError если каталог для создания уже существует.

# Syntax: os.mkdir(path, mode = 0o777, *, dir_fd = None)
# Parameter:
# path: A path-like object representing a file system path. A path-like object is either a string or bytes object representing a path.
# mode (optional): A Integer value representing mode of the directory to be created. If this parameter is omitted then default value Oo777 is used.
# dir_fd (optional): A file descriptor referring to a directory. The default value of this parameter is None.
# If the specified path is absolute then dir_fd is ignored.

# Note: The ‘*’ in parameter list indicates that all following parameters (Here in our case ‘dir_fd’) are keyword-only parameters and they can be provided using their name, not as positional parameter.

# Return Type: This method does not return any value.

# Create a directory "test"
if not os.path.exists('test'):
	os.mkdir("test")

# Метод chdir ()
# Вы можете использовать метод chdir (), чтобы изменить текущий каталог. Метод chdir () принимает аргумент, который является именем каталога, который вы хотите сделать текущим каталогом.

# Changing a directory to "../"
os.chdir("../")

print('CWD: ', os.getcwd())

os.chdir("./files")

print('CWD: ', os.getcwd())

for name in os.listdir(os.getcwd()):
   path = os.path.join(os.getcwd(), name)
   if os.path.isdir(path):
       print(path)

# Метод rmdir ()
# Метод rmdir () удаляет каталог, который передается в качестве аргумента в методе.

# Перед удалением каталога все содержимое в нем должно быть удалено.
if not os.path.exists('tmp'):
	os.mkdir("tmp")
	os.mkdir("tmp/test")
# This would  remove "./tmp/test"  directory.
else:
	os.rmdir("./tmp/test")
	os.rmdir("./tmp")

for name in os.listdir(os.getcwd()):
   path = os.path.join(os.getcwd(), name)
   if os.path.isdir(path):
       print(path)
