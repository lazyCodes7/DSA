class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        required_num1 = 0
        required_num2 = 0
        index = []
        for i in range(len(nums)):
            try:
                mapping[nums[i]]+=1
                
            except:
                mapping[nums[i]]=1
                
        for keys in mapping.keys():
            required = target-keys
            try:
                if(required==keys and mapping[required]>1):
                    required_num1 = keys
                    required_num2 = required
                    break
                elif(mapping[required]>=1 and required!=keys):
                    required_num1 = keys
                    required_num2 = required
                    break
            except:
                pass
                                
        for i in range(len(nums)):
            if(nums[i] == required_num1):
                index.append(i)
                break
                
        for i in range(len(nums)-1,-1,-1):
            if(nums[i] == required_num2):
                index.append(i)
                break
                
        return index