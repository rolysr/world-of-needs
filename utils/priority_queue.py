#Class for representing a min heap that behaves like a priority queue
class PriorityQueue:
    def __init__(self):
        self.base = list()
        self.base_size = 0
        self.heap_size = 0

    def is_equal(self, a, b): #Determine if two tuples of three elements of the specified format are equals
        return (a[0] == b[0] and a[1] == b[1] and a[2] == b[2])

    def is_less_than(self, a, b): #Determine if a tuple "a" of the specified format is less than a tuple "b"
        return ((a[0] < b[0]) or (a[0] == b[0] and a[1] < b[1]))      

    def push(self, value): #Pushes a value into the heap
        if len(self.base) == self.heap_size:
            self.base.append(value)
            self.base_size = self.base_size + 1

        self.base[self.heap_size] = value
        self.heap_size += 1
        pos = self.heap_size - 1

        while(pos>0 and self.is_less_than(self.base[pos],self.base[int((pos-1)/2)])):
            temp = self.base[pos]
            self.base[pos] = self.base[int((pos-1)/2)]
            self.base[int((pos-1)/2)] = temp
            pos=int((pos-1)/2)

    def top(self):#Returns the minimum element
        if self.heap_size > 0:
            return self.base[0]

    def pop(self): #Pops a value into the heap
        if self.heap_size == 0:
            return
        ans = self.base[0]
        self.heap_size = self.heap_size - 1
        if self.heap_size > 0:
            self.base[0]=self.base[self.heap_size]
            pos=0
            while True:
                neutral=(10000000000000,"$" , None)
                m=neutral
                if pos*2+1<self.heap_size:
                    m=self.base[pos*2+1]
                if pos*2+2<self.heap_size and self.is_less_than(self.base[pos*2+2],m):
                    m=self.base[pos*2+2]
                if self.is_equal(m,neutral) or self.is_less_than(self.base[pos],m):
                    break
                else:
                    if self.is_equal(m, self.base[pos*2+1]):
                        temp = self.base[pos*2+1]
                        self.base[pos*2+1] = self.base[pos]
                        self.base[pos] = temp
                        pos=pos*2+1
                    else:
                        temp = self.base[pos*2+2]
                        self.base[pos*2+2] = self.base[pos]
                        self.base[pos] = temp
                        pos=pos*2+2
        return ans