class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = list(s[::-1])
        print(stack1)
        stack2 = []
        while(stack1 != []):
            element = stack1.pop()
            if(element == "(" or element == "{" or element == "["):
                stack2.append(element)
            
            else:
                if(stack2==[]):
                    return False
                stac2_top = stack2.pop()
                if(element == ")" and stac2_top!="("):
                    return False
                if(element == "]" and stac2_top!="["):
                    return False
                if(element == "}" and stac2_top!="{"):
                    return False
        if(stack1 == [] and stack2 == []):
            return True
        else:
            return False