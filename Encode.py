import sys
from Element import Element
import Huffman
import PQHeap
import bitIO

'''
Authors:
    Sofie Louise Madsen - sofma18@student.sdu.dk
    Joachim Bülow       - jobul18@student.sdu.dk
    Simon Soele Madsen  - smads18@student.sdu.dk
'''

# Open the files in readbit and write binary mode
inputfile = open(sys.argv[1], "rb")
outputfile = open(sys.argv[2], "wb")

# Instantiate our bitwriter for writing to output file 
bitstreamout = bitIO.BitWriter(outputfile)

# 2 arrays for keeping track of the occurrences of each character/byte 
# and the Huffman codes from root to the leaf containing the byte for each byte.
occurences = 256 * [0]
codes = 256 * [0]

# reads the input file and counts the occurence of each byte
def read_file_occurences():
    while True:
        byte = inputfile.read(1)
        if byte == b"":
            break
        else:
            # We have a byte --> translate to integer with [0], increment occurence of that index.
            occurences[byte[0]] += 1
    inputfile.close()

# creates an element for each character/byte holding the byte and its occurence and inserts into a min-heap. 
def create_priority_queue():
    n = len(occurences)
    q = []
    for i in range(len(occurences)):
        element = Element(occurences[i], i)
        PQHeap.insert(q, element)
    return q


# Recursively walks through our huffman tree, if we reach a leaf its Huffman code path will be added to codes array.
def in_order_walk_with_helper(path, node):
    if(node.data is not None):
        if(isinstance(node.data, int)):
            codes[node.data] = path
        else:
            in_order_walk_with_helper(path + "0", node.data[0])
            in_order_walk_with_helper(path + "1", node.data[1])

# Initiates our recursive walk.
def in_order_walk_with_path(T):
    in_order_walk_with_helper("", T)


# Writes the occurence to output file.
def write_occurences_to_output():
    for occurence in occurences:
        bitstreamout.writeint32bits(occurence)

# Reads the inputfile again and for each byte we write its Huffman code to the output file. 
def writes_codes_to_output():
    inputfile = open(sys.argv[1], "rb")
    while True:
        byte = inputfile.read(1)
        if byte == b"":
            break
        else:
            for bit in codes[byte[0]]:
                bitstreamout.writebit(int(bit))
    bitstreamout.close()


read_file_occurences()
queue = create_priority_queue()
ele = Huffman.huffman(queue)
in_order_walk_with_path(ele)
write_occurences_to_output()
writes_codes_to_output()
