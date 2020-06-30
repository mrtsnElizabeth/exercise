class Conv:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        self.syb = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I'
        ]
        
    def to_roman(self, num):    
        """
        :param self:
        :param n: int
        :return: str    
        """
        i = 0
        result = ""
        while num: 
            div = num // self.val[i] 
            num %= self.val[i] 
  
            while div: 
                result += self.syb[i] 
                div -= 1
            i += 1
        return result    

print('Converted:', Conv().to_roman(44))