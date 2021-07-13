try:
   file = open('input-file', 'r')
# Поймать несколько исключений в одном блоке Except
# except (Exception1, Exception2) as e:
#    pass

# Обработка нескольких исключений одним блоком Except
# способ размещения всех исключений, которые могут возникать в виде кортежа.

except (IOError, EOFError) as e:
    print("Testing multiple exceptions. {}".format(e.args[-1]))

except FileNotFoundError as e:
   print("File does not exist", e)
# способ разрешить любое произвольное исключение
except Exception as ex:
   print('любое произвольное исключение', ex)
   raise ex

# обработка каждого исключения в выделенном блоке Except. 
except EOFError as ex:
   print("Caught the EOF error.")
   raise ex
except IOError as e:
   print("Caught the I/O error.")
   raise e

# IOError - происходит при ошибках файловой системы, например, если файл не открывается.
# ImportError - Если модуль Python не может быть загружен или не найден.
# ValueError - происходит, если функция получает аргумент правильного типа, но не подходящего значения.
# KeyboardInterrupt - когда пользователь вводит ключ прерывания (т.е. Control-C или Del в консоли)
# EOFError - Возникает, если входные функции (input() / raw_input()) попадают в условие конца файла (EOF), но без чтения каких-либо данных.

# Примеры наиболее распространенных исключений
# except IOError:
# print('Error occurred while opening the file.')

# except ValueError:
# print('Non-numeric input detected.')

# except ImportError:
# print('Unable to locate the module.')

# except EOFError:
# print('Identified EOF error.')

# except KeyboardInterrupt:
# print('Wrong keyboard input.')

# except:
# print('An error occurred.')