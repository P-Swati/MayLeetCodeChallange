# basically while popping elements for particular number, keep count of the no. of elements u have popped
# and store it as well, so that when in future this pushed element gets popped, then popcount for this ele
class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        popcount=0
        if(not self.stack or self.stack[-1][0]>price):
            self.stack.append( (price,0) ) # price,0  indicates that popcount for this is 0
            return 1
        
        while(self.stack and price>=self.stack[-1][0]):
            popcount+= self.stack.pop()[1]+1 # all ele that were popped for pushing this ele + 1(for popping this ele)
            
        self.stack.append( (price,popcount) ) # push total popcount for cur price
         
        return popcount+1 # ans is total popcount + 1(for cur price)
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
