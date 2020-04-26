import bitIO
import sys
import Huffman
from Element import Element
import PQHeap

inputfile = open(sys.argv[1], "rb")
bitstreamin = bitIO.BitReader(inputfile)
outputfile = open(sys.argv[2], "wb")

occurrences = 256 * [0]

def create_priority_queue():
    n = len(occurrences)
    q = []
    for i in range(len(occurrences)):
        element = Element(occurrences[i], i)
        PQHeap.insert(q, element)
    return q


def read_occurences():
    for i in range(256):
        x = bitstreamin.readint32bits()
        occurrences[i] = x


def make_huffman_tree():
    return Huffman.huffman(queue)


def in_order_walk_with_helper(path, node):
    if(node.data is not None):
        if(isinstance(node.data, int)):
            path
        else:
            in_order_walk_with_helper(path + "0", node.data[0])
            print("Key "+str(node.key)+": "+path)
            in_order_walk_with_helper(path + "1", node.data[1])


def in_order_walk_with_path(T):
    in_order_walk_with_helper("", T)

def calculate_occurrence_sum():
    sum = 0
    for occurrence in occurrences:
        sum += occurrence
    return sum

def read_encoded_file():
    sum = calculate_occurrence_sum()
    cursor = root_element
    done = False
    while not done:
        # Bug. Only reads first bit in file = 0
        x = bitstreamin.readbit()
        if(isinstance(cursor.data, int)):
            # Write to file and reset cursor
            outputfile.write(bytes([cursor.data]))
            sum -= 1
            if sum < 0:
                done = True
            cursor = root_element
        else:
            cursor = cursor.data[x]

read_occurences()
queue = create_priority_queue()
root_element = make_huffman_tree()
read_encoded_file()
bitstreamin.close()
            
        




    


    
    

        
    
