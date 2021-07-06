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

    # pattern = r"INV-0014"
    # string = "Invoice Number INV-0014"

    # Экранирование специальных символов
    
    # Специальные символы (например, класса символов скобки [ ]) не соответствуют буквально:

    match = re.search(r'[b]', 'a[b]c')
    print(match.group())
    # Out: 'b' 
    
    # Специальные символы могут быть сопоставлены буквально:

    match = re.search(r'\[b\]', 'a[b]c')
    print(match.group())
    # Out: '[b]' 
    
    # re.escape() функция может использоваться , чтобы сделать это для вас:

    print(re.escape('a[b]c'))
    # Out: 'a\\[b\\]c'
    
    match = re.search(re.escape('a[b]c'), 'a[b]c')
    print(match.group())
    # Out: 'a[b]c' 
    
    # re.escape() функция экранирует все специальные символы
    # это полезно, если вы составляете регулярное выражение на основе пользовательского ввода:

    username = 'A.C.'  # suppose this came from the user
    print(re.findall(r'Hi {}!'.format(username), 'Hi A.C.! Hi ABCD!'))
    # Out: ['Hi A.C.!', 'Hi ABCD!']
    
    print(re.findall(r'Hi {}!'.format(re.escape(username)), 'Hi A.C.! Hi ABCD!'))
    # Out: ['Hi A.C.!'] 

    line = 'Subtotal $84.00'
    result = re.search("Subtotal \$(\d+\.\d+)", line)
    if result:
        product_subtotal = result.group(1)
        print(f"product_subtotal : {product_subtotal}\n")

    # the date in the format: 4/7/2021
    line =  '4/7/2021'
    result = re.search("([0-9]+\/[0-9]+\/[0-9]{4})", line)
    if result:
        in_date = result.group(1)
        print(f"Date : {in_date}\n")

    line =  'bla@bla.bla'
    result = re.search("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", line)
            
    if result:
        email = result.group(1)
        print(f"Email : {email}\n")


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

