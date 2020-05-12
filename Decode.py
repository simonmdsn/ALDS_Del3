import bitIO
import sys
import Huffman
from Element import Element
import PQHeap

'''
Authors:
    Sofie Louise Madsen - sofma18@student.sdu.dk
    Joachim Bülow       - jobul18@student.sdu.dk
    Simon Soele Madsen  - smads18@student.sdu.dk
'''

#Open the files in readbit and write binary mode
inputfile = open(sys.argv[1], "rb")
outputfile = open(sys.argv[2], "wb")

# Instantiate our bitreader for reading our input file
bitstreamin = bitIO.BitReader(inputfile)

# Array for keeping track of occurences of each character/byte.
occurrences = 256 * [0]

# creates an element for each character/byte holding the byte and its occurence and inserts into a min-heap. 
def create_priority_queue():
    n = len(occurrences)
    q = []
    for i in range(n):
        element = Element(occurrences[i], i)
        PQHeap.insert(q, element)
    return q

# The first 256 ints in our inputfile is read and occurences added to the array.
def read_occurences():
    for i in range(256):
        x = bitstreamin.readint32bits()
        occurrences[i] = x

# Makes our Huffman tree
def make_huffman_tree():
    return Huffman.huffman(queue)

# We read each bit in our file and traverses through our Huffman tree to determine 
# what byte we have to write in our output file. 
# If the cursor hits a leaf in our tree we know, that we need write the byte, which is data of the leaf.
def read_encoded_file():
    sum = sum(occurrences)
    cursor = root_element
    done = False
    while sum > 0:
        x = bitstreamin.readbit()
        cursor = cursor.data[x]
        if isinstance(cursor.data, int):
            # Write to file and reset cursor
            outputfile.write(bytes([cursor.data]))
            sum -= 1
            cursor = root_element

read_occurences()
queue = create_priority_queue()
root_element = make_huffman_tree()
read_encoded_file()
bitstreamin.close()
            
        




    


    
    

        
    
