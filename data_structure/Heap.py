




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

if __name__ == '__main__':
    elements = [17,7,6,14,12,11,15]
    construct_heap2(elements)