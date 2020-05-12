import PQHeap
from Element import Element

'''
Authors:
    Sofie Louise Madsen - sofma18@student.sdu.dk
    Joachim Bülow       - jobul18@student.sdu.dk
    Simon Soele Madsen  - smads18@student.sdu.dk
'''

# For each Element in our heap we extract the two smallest elements by key
# Then we insert a new Element into the queue where the key is the sum of their occurences,
# and the data is a subtree (list) with the two elements we have summed.
# Last we extract the root element with extractmin.
def huffman(queue):
    n = len(queue)
    q = queue
    for i in range(len(queue)-1):
        x = PQHeap.extractMin(q)
        y = PQHeap.extractMin(q)
        z = x.key + y.key
        PQHeap.insert(q, Element(z, [x, y]))
    return PQHeap.extractMin(q)