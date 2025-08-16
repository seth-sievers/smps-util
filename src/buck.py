from converter import Converter

class Buck(Converter):
        def __init__(self):
                super().__init__() # initialize base class 
                super().converter_list.append(self) # add itself to the converter list 
                
                self.topology = 'Buck'

# Global declaration 
Buck()



