# base class for all types of power converters in order to define shared methods 
class Converter:
        # static class variable will auto populate when a derived class is instantiated
        converter_list = []


        # topology: string of the converter name Ex: "Buck", "Boost", "Flyback "
        def __init__(self):
                
                # generic converter attributes 
                self.topology = ''