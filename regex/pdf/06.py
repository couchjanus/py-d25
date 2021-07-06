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

def find_following_line(file, pattern, slise):
    lines = [] # make an empty list
    with open(file) as f:
        for line in f:
            
            line = line.rstrip()   # Strip trailing spaces and newline
            lines.append(line)
        
    for i, line in enumerate(lines):
        if re.search(pattern, line):
            return lines[i+slise[0]:i+slise[1]]

def main():
    # Check and retrieve command-line arguments

    if len(sys.argv) != 3:
        
        print ("Use <script name>.py <input file> <output file>, please!")
        sys.exit(1)   # Return a non-zero value to indicate abnormal termination
    
    fileIn  = sys.argv[1]
    fileOut = sys.argv[2]

    # Verify source file
    if not os.path.isfile(fileIn):
        print("error: {} does not exist".format(fileIn))
        sys.exit(1)

    # Verify destination file
    if os.path.isfile(fileOut):
        print("{} exists. Override (y/n)?".format(fileOut))
        reply = input().strip().lower()
        if reply[0] != 'y':
           sys.exit(1)

    lines = [] # make an empty list
    # lines = find_following_line(fileIn)
    lines = find_following_line(fileIn, "Billing Information Shipping Information", (1,5))

    print(lines)

    print('bill_info ', lines[0:2])
    invoice['bill_info'] = lines[0:2]
    print('ship_info ', lines[2:4])
    invoice['ship_info'] = lines[2:4]

    # Price

    lines = find_following_line(fileIn, "Price", (1,3))

    print(lines)
    
    invoice['product_description'] = lines[0:1]
    unit = ''.join(lines[1:2])
    print(unit)
    result = re.search("\$(\d+\.\d+)", unit)
    if result: 
        product_price = result.group(1)
        print(f"product_price : {product_price}\n")
        invoice['product_price'] = product_price

    result = re.search("(\d+)", unit)
    if result: 
        product_qty = result.group(1)
        print(f"product_qty : {product_qty}\n")
        invoice['product_qty'] = product_qty

    result = re.search("([a-zA-Z :_.-]+)", unit)
    if result: 
        product_name = result.group(1)
        print(f"product_name : {product_name}\n")
        invoice['product_name'] = product_name

    
    with open(fileIn, 'r') as fpIn:
        for line in fpIn:
            line = line.rstrip()   # Strip trailing spaces and newline

            # INV-0014
            result = re.search("INV-([0-9]+)", line)
            if result: 
                in_numb = result.group(1)
                print(f"in_numb : {in_numb}\n")
                invoice['in_numb'] = in_numb

            # Subtotal $84.00
            result = re.search("Subtotal \$(\d+\.\d+)", line)
            if result: 
                product_subtotal = result.group(1)
                print(f"product_subtotal : {product_subtotal}\n")
                invoice['product_subtotal'] = product_subtotal

            # Shipping $52.00
            result = re.search("Shipping \$(\d+\.\d+)", line)
            if result: 
                product_ship = result.group(1)
                print(f"product_ship : {product_ship}\n")
                invoice['product_ship'] = product_ship
            # Tax $0.00

            # Total $136.00

            # the date in the format: 4/7/2021

            result = re.search("([0-9]+\/[0-9]+\/[0-9]{4})", line)
            if result: 
                in_date = result.group(1)
                print(f"Date : {in_date}\n")
                invoice['in_date'] = in_date


            result = re.search("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", line)
            
            if result: 
                email = result.group(1)
                print(f"Email : {email}\n")
                invoice['email'] = email
            
            
    print(f"Invoice : {invoice}\n")

    with open(fileOut, 'w') as fpOut:
        fpOut.write(f"{invoice}\n")


main()
