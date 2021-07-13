import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# After analyzing the output, we realize that the last element of the list is not sorted. We analyze the code and discover an off-by-one error in line for passnum in reversed(range(len(alist) - 1)):. 

# Let’s fix it by changing the following line: reversed(range(len(alist) - 1)):

def bubble_sort(alist):
    logging.info(f'Sorting the list: {alist}')
    # for passnum in reversed(range(len(alist) - 1)):
    # Change the preceding line to the following one:
    for passnum in reversed(range(len(alist))):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
            logging.debug(f'alist: {alist}')

    logging.info(f'Sorted list     : {alist}')
    return alist


assert [1, 2, 3, 4, 7, 10] == bubble_sort([3, 7, 10, 2, 4, 1])
