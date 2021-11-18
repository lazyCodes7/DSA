class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        items = []
        profit = 0.0
        i = 0
        for element in Items:
            weight, value = element.weight, element.value
            ratio = value/weight
            
            items.append([ratio, weight, value])
            
        items.sort(reverse = True)
        #print(items)
        
        while(W>0 and i<len(items)):
            if(W>items[i][1]):
                profit+=items[i][2]
                W-=items[i][1]
                
            else:
                profit+=items[i][2]*(W/items[i][1])
                
                break
            i+=1
        return profit