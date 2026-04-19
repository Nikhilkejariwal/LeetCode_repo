class Solution(object):
    def romanToInt(self, string):
        """
        :type s: str
        :rtype: int
        """
        string+=" "
        num = 0
        for i in range(len(string)):
            if "M" == string[i]:
                num+=1000
            elif "D"==string[i]:
                num+=500
            elif "C"==string[i]:
                if"D"==string[i+1]:  
                    num+=(400-500)
                elif"M"==string[i+1]:  
                    num+=(900-1000)
                else:
                    num+=100
            elif "L"==string[i]:
                num+=50
            elif "X"==string[i]:
                if"L"==string[i+1]:  
                    num+=(40-50)
                elif"C"==string[i+1]:  
                    num+=(90-100)
                else:
                    num+=10
            elif "V"==string[i]:
                num+=5
            elif "I"==string[i]:
                if"V"==string[i+1]:  
                    num+=(4-5)
                elif"X"==string[i+1]:
                    num+=(9-10)
                else:
                    num+=1
            
            
        return num
