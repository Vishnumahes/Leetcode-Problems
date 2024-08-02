class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res= ""
        carry =0
        
        a,b=a[::-1],b[::-1]
        
        for i in range(max(len(a),len(b))):
            digitsA = ord(a[i])-ord("0") if i < len(a) else 0
            digitsB = ord(b[i])-ord("0") if i <len(b) else 0
            
            total = digitsA + digitsB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
        if carry:
            res = "1" +res
        return res
        