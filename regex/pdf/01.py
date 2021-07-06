import sys
import os

def main():
    # Check and retrieve command-line arguments
    # sys.argv содержит список параметров, переданных программе через командную строку, 
	# причем нулевой элемент списка - это имя скрипта.

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

    # Process the file line-by-line
    
    with open(fileIn, 'r') as fpIn, open(fileOut, 'w') as fpOut:
        lineNumber = 0
        for line in fpIn:
            lineNumber += 1
            line = line.rstrip()   # Strip trailing spaces and newline
            fpOut.write("{}: {}\n".format(lineNumber, line))

        # Need \n, which will be translated to platform-dependent newline
        print("Number of lines: {}\n".format(lineNumber))

main()

