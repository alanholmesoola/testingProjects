class FancyText:
    def mixed_case(self, text_to_be_formatted):

        '''
        DOCSTRING:
        Takes a string as input
        Applies mixed case of upper and lower to string
        '''

        index = 0
        mystring = ""
    
        for item in text_to_be_formatted:

            if index%2 == 0:
                item = item.upper()
                mystring = mystring+item
                index = index+1
            
            elif index%2 != 0:
                item = item.lower()
                mystring = mystring+item  
                index = index+1
            
        return mystring
