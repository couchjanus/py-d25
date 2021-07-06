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
