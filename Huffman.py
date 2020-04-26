import PQHeap
from Element import Element

def huffman(queue):
    n = len(queue)
    q = queue
    for i in range(len(queue)-1):
        x = PQHeap.extractMin(q)
        y = PQHeap.extractMin(q)
        z = x.key + y.key
        PQHeap.insert(q, Element(z, [x, y]))
    return PQHeap.extractMin(q)
    
