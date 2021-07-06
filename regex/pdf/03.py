import sys
import os
import re

invoice = {
    'in_numb': '',
    'in_date': '',
    'bill_info': '',
    'ship_info': '',
    'email': '',
    'product_description': '',
    'product_name': '',
    'product_qty': 0,
    'product_price': 0,
    'product_tax': 0,
    'product_subtotal': 0,
    'product_ship': 0,
    'product_total': 0,
    'product_note': '',

}

def main():
    # Check and retrieve command-line arguments

    # if len(sys.argv) != 3:
        
    #     print ("Use <script name>.py <input file> <output file>, please!")
    #     sys.exit(1)   # Return a non-zero value to indicate abnormal termination
    
    # fileIn  = sys.argv[1]
    # fileOut = sys.argv[2]

    # # Verify source file
    # if not os.path.isfile(fileIn):
    #     print("error: {} does not exist".format(fileIn))
    #     sys.exit(1)

    # # Verify destination file
    # if os.path.isfile(fileOut):
    #     print("{} exists. Override (y/n)?".format(fileOut))
    #     reply = input().strip().lower()
    #     if reply[0] != 'y':
    #        sys.exit(1)

    
    # Соответствие началу строки
    # Первый аргумент re.match() является регулярным выражением, 
    # вторая строка , чтобы соответствовать:

    # INV-0014

    pattern = r"INV-0014"
    string = "Invoice Number INV-0014"

    match = re.match(pattern, string)
    print(match)

    # print(match.group())
    
    # переменная шаблона представляет собой строку с префиксом r, 
    # что указывает на то, что строка - строка символов.

    # Сырые строковый литерал имеет несколько иного синтаксис, а именно обратный слэш \ в сырых строковых литералов означает «только обратной косой черты», и нет никакой необходимости удвоения люфтов, чтобы избежать «экранирующих последовательностей», такие как символ новой строки ( \n ), вкладки ( \t ), забой ( \ ), формы-каналы ( \r ), и так далее. В обычных строковых литералах каждый обратный слеш должен быть удвоен, чтобы его не принимали за начало escape-последовательности.

    # Следовательно, r"\n" является строкой из 2 -х символов: \ и n . Regex модель также использовать обратную косую черту, например, \d относится к любому цифровому символу. Мы можем избежать того, чтобы удвоить наши избежать строки ( "\\d" ) с использованием сырых строк ( r"\d" ).

    # Например:

    string = "\\tINV-0014" # here the backslash is escaped, so there's no tab, just '\' and 't'
    pattern = "\\tINV"   # this will match \t (escaping the backslash) followed by INV
    
    # print(re.match(pattern, string).group())   # no match
    print(re.match(pattern, "\tINV").group())  # matches '\tINV'

    pattern = r"\\tINV"  
    print(re.match(pattern, string).group())   # matches '\\tINV' 

    # Сопоставление выполняется только с начала строки. 
    # чтобы соответствие выполнялось в любом месте, используйте re.search:

    match = re.match(r"(123)", "a123zzb")
    print(match is None)
    # Out: True

    match = re.search(r"(123)", "a123zzb")

    print(match.group())
    # Out: '123' 
    
    # поиск
    pattern = r"(your base)"
    sentence = "All your base are belong to us."

    match = re.search(pattern, sentence)
    print(match.group(1))
    # Out: 'your base'

    match = re.search(r"(belong.*)", sentence)
    print(match.group(1))
    # Out: 'belong to us.' 

    # Поиск осуществляется в любом месте строки, в отличие от re.match. 
    # Вы можете также использовать re.findall.

    # Поиск в начале строки (используйте ^ ),

    match = re.search(r"^123", "123zzb")
    print(match.group(0))
    # Out: '123'

    match = re.search(r"^123", "a123zzb")
    print(match is None)
    # Out: True 
    
    # Поиск в конце строки (используйте $ ),

    match = re.search(r"123$", "zzb123")
    print(match.group(0))
    # Out: '123'

    match = re.search(r"123$", "123zzb")
    print(match is None)
    # Out: True 
    
    # оба (использовать оба ^ и $ ):

    match = re.search(r"^123$", "123")
    print(match.group(0))
    # Out: '123' 
    
    # Группировка осуществляется с помощью скобок. 
    # group() возвращает строку, образованную из согласующих скобок подгрупп.

    print(match.group()) # Group without argument returns the entire match found
    # Out: '123'
    
    print(match.group(0)) # Specifying 0 gives the same result as specifying no argument
    # Out: '123' 
    
    # Аргументы group() для извлечения конкретной подгруппы.

    # Если есть единственный аргумент, результат - единственная строка; 
    # если имеется несколько аргументов, результатом является кортеж с одним элементом на аргумент.

    # Вызов groups() возвращает список кортежей, содержащих подгруппу.

    sentence = "This is a phone number 038-123-456-9910"
    pattern = r".*(phone).*?([\d-]+)"

    match = re.match(pattern, sentence)

    print(match.groups())   # The entire match as a list of tuples of the paranthesized subgroups
    # Out: ('phone', '038-123-456-9910')

    print(match.group())        # The entire match as a string
    # Out: 'This is a phone number 038-123-456-9910'

    print(match.group(0))       # The entire match as a string
    # Out: 'This is a phone number 038-123-456-9910'

    print(match.group(1))       # The first parenthesized subgroup.
    # Out: 'phone'

    print(match.group(2))       # The second parenthesized subgroup.
    # Out: '672-123-456-9910'

    print(match.group(1, 2))    # Multiple arguments give us a tuple.
    # Out: ('phone', '038-123-456-9910') 

    # result = re.search("INV-([0-9]+)", line)

    # Process the file line-by-line
    
    # with open(fileIn, 'r') as fpIn:
    #     for line in fpIn:
    #         line = line.rstrip()   # Strip trailing spaces and newline

    #         # INV-0014
    #         result = re.search("INV-([0-9]+)", line)
    #         if result: 
    #             in_numb = result.group(1)
    #             print(f"in_numb : {in_numb}\n")
    #             invoice['in_numb'] = in_numb

    # print(f"Invoice : {invoice}\n")
    # with open(fileOut, 'w') as fpOut:
    #     fpOut.write(f"{invoice}\n")

main()

