class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # k = k-1
        # index = 0
        # li = [i for i in range(1,n+1)]
        # def cal(k,index):
        #     if len(li) == 1:
        #         return li[0]
        #     index = (index + k)% len(li)
        #     del li[index]
        #     return cal(k,index)
        # return cal(k,index)
        
        k -= 1
        friends = [i for i in range(1, n + 1)]
        index = 0
        def winner(k ,index):
            if len(friends) == 1:
                return friends[0]
            index = (index + k) % len(friends)
            del friends[index]
            return winner(k , index)
        
        
        return winner(k , index)
        
            
            
        
        
    
    