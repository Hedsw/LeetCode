class MinStack:
    def __init__(self):

        self.datas = []
        
    def push(self, x: int) -> None:
        m = x
        if self.datas:
            m = self.datas[-1][-1]
            if m > x:
                m = x 
        self.datas.append((x,m))

    def pop(self) -> None:
        self.datas.pop()
        
    def top(self) -> int:


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
    
    def push(self, x: int) -> None:
        m = x
        if self.nums:
            m = self.nums[-1][1]
            if m > x:
                m = x
        self.nums.append((x,m))

    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1][0]

    def getMin(self) -> int:
        return self.nums[-1][1]
 