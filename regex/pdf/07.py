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

def setItem(pattern, string, key):
    result = re.search(pattern, string)
    if result: 
        invoice[key] = result.group(1)

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

    lines = []
    lines = find_following_line(fileIn, "Billing Information Shipping Information", (1,5))

    invoice['bill_info'] = lines[0:2]
    invoice['ship_info'] = lines[2:4]
    
    lines = find_following_line(fileIn, "Price", (1,3))
    
    invoice['product_description'] = lines[0:1]
    unit = ''.join(lines[1:2])

    setItem("\$(\d+\.\d+)", unit, 'product_price')
    setItem("(\d+)", unit, 'product_qty')
    setItem("([a-zA-Z :_.-]+)", unit, 'product_name')

    with open(fileIn, 'r') as fpIn:
        for line in fpIn:
            line = line.rstrip()
            setItem("INV-([0-9]+)", line, 'in_numb')
            setItem("Subtotal \$(\d+\.\d+)", line, 'product_subtotal')
            setItem("Shipping \$(\d+\.\d+)", line, 'product_ship')
            setItem("([0-9]+\/[0-9]+\/[0-9]{4})", line, 'in_date')
            setItem("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", line, 'email')
            
    print(f"Invoice : {invoice}\n")

    with open(fileOut, 'w') as fpOut:
        fpOut.write(f"{invoice}\n")

main()

