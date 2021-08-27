

class Haffman_node():
    def __init__(self,left=None,right=None,weight=0):
        self.left = left
        self.right = right
        self.weight = weight



def sift_up(heap,child):
    cur = heap[child]
        #与其父节点进行比较
    while child>>1>0 and cur>heap[child>>1]:
        heap[child] = heap[child>>1]
        child >>= 1
    heap[child] = cur

def construct_heap(elements):
    heap = [0]
    for i in range(len(elements)):
        heap.append(elements[i])
        sift_up(heap,len(heap)-1)
    print(heap)


def sift_down(heap,root):
    cur = heap[root]
    while root<<1<len(heap):
        child = root<<1
        #找到子节点中较小的那个
        if child|1<len(heap) and heap[child|1]>heap[child]:
            child = child|1
        if cur<heap[child]:
            heap[root] = heap[child]
            root = child
        else:
            break
    heap[root] = cur

def construct_heap2(elements):
    heap = [0]
    heap.extend(elements)
    for i in range(len(elements)//2,0,-1):
        sift_down(heap,i)
    print(heap)

def sift_up2(heap,child):
    cur = heap[child]
    while child >> 1 >0 and heap[child>>1].weight > cur.weight:
        heap[child] = heap[child>>1]
        child = child >> 1
    heap[child] = cur

def sift_down2(heap,root):
    cur = heap[root]
    while root<<1<len(heap):
        child = root<<1
        #找到子节点中较小的那个
        if child|1<len(heap) and heap[child|1].weight<heap[child].weight:
            child = child|1
        if cur.weight > heap[child].weight:
            heap[root] = heap[child]
            root = child
        else:
            break
    heap[root] = cur

def constructHuffmanHeap(huffman_heap):
    for i in range((len(huffman_heap)-1) // 2 , 0, -1):
        sift_down2(huffman_heap, i)
    return huffman_heap

def deleteHeap(huffman_heap):
    huffman_heap[1] = huffman_heap[-1]
    del huffman_heap[-1]
    if len(huffman_heap)>1:
        sift_down2(huffman_heap,1)
    return huffman_heap

#从最后面插入一个元素
def insertHeap(huffman_heap,node):
    huffman_heap.append(node)
    sift_up2(huffman_heap,len(huffman_heap)-1)

if __name__ == '__main__':
    # elements = [17,7,6,14,12,11,15]
    # construct_heap2(elements)
    #
    weights = [1,2,3,4,5]
    huffman_heap = [Haffman_node()]
    for i in range(len(weights)):
        huffman_heap.append(Haffman_node(weight=weights[i]))
    print(huffman_heap)
    while len(huffman_heap)>2:

       huffman_heap = constructHuffmanHeap(huffman_heap)
       min_node_1 = huffman_heap[1]
       huffman_heap = deleteHeap(huffman_heap)
       min_node_2 = huffman_heap[1]
       huffman_heap = deleteHeap(huffman_heap)

       new_node = Haffman_node(left=min_node_1,right=min_node_2,
                               weight=min_node_1.weight+min_node_2.weight)
       insertHeap(huffman_heap,new_node)
    result = huffman_heap[-1]
    print(huffman_heap)
    a=2
