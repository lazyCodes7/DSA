class Solution:
    def myAtoi(self, s: str) -> int:
        sign = "+"
        number = ""
        
        i = 0
        
        while(s[i] == " "):
            i+=1
        
        print(i)
        while(i<len(s)):
            print(s[i])
            if((s[i] == "+" or s[i] == "-") and number == ""):
                sign = s[i]
                
            elif(ord(s[i])>=48 and ord(s[i])<=57):
                if((ord(s[i]) == 48 and number!="") or ord(s[i])>48):
                    number+=s[i]
            
            else:
                break
            
            i+=1

        if(number == ""):
            number = 0
        
        if(sign == "-"):
            number = -(int(number))
        else:
            number = int(number)
        
        return number

sol = Solution()
print(sol.myAtoi("   -42"))