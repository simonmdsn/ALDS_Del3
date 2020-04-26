import sys
from Element import Element
import Huffman
import PQHeap
import bitIO

inputfile = open(sys.argv[1], "rb")
outputfile = open(sys.argv[2], "wb")

bitstreamout = bitIO.BitWriter(outputfile)

occurences = 256 * [0]
codes = 256 * [0]


def read_file_occurences():
    while True:
        byte = inputfile.read(1)
        if byte == b"":
            break
        else:
            count_occurence(byte)


def count_occurence(byte):
    # We have a byte --> translate to integer with [0], increment occurence of that index.
    occurences[byte[0]] += 1


def create_priority_queue():
    n = len(occurences)
    q = []
    for i in range(len(occurences)):
        element = Element(occurences[i], i)
        PQHeap.insert(q, element)
    return q


def in_order_walk_with_helper(path, node):
    if(node.data is not None):
        if(isinstance(node.data, int)):
            codes[node.data] = path
        else:
            in_order_walk_with_helper(path + "0", node.data[0])
            print("Key "+str(node.key)+": "+path)
            in_order_walk_with_helper(path + "1", node.data[1])


def in_order_walk_with_path(T):
    in_order_walk_with_helper("", T)


def write_occurences_to_output():
    for occurence in occurences:
        bitstreamout.writeint32bits(occurence)

# Måske forbryderen, vi vender tilbage


def writes_codes_to_output():
    while True:
        byte = inputfile.read(1)
        print(byte[0])
        if byte == b"":
            break
        else:
            print("code: ", codes[byte[0]])
            bitstreamout.writebit(codes[byte[0]])
    bitstreamout.close()


read_file_occurences()
queue = create_priority_queue()
ele = Huffman.huffman(queue)
in_order_walk_with_path(ele)
write_occurences_to_output()
writes_codes_to_output()
