import reedsolo as rs

from transmit_color import display_transmission

#Pre-defined colors for encoding
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

bit_transform = {'00': RED,
                 '01': GREEN,
                 '10': BLUE}

class CSKPoint:
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

    def get_color(self):
        return (self.r, self.g, self.b)

    def __str__(self):
        return f'({self.r}, {self.g}, {self.b})'

class CSKConstellation:
    #Ensure that size of constellation remains consistent throughout implementation
    def __init__(self, method):
        self.size_C = method  #Size should always be fixed to match M-CSK method
        self.points = [None] * self.size_C        #Input points as list of color

    def add_point(self, index, point):
        self.points[index] = point #Point should be a CSKPoint object

    def __str__(self):
        return f'{self.points}'


def convert_to_binary(string):
    #Initialize empty list of ascii characters
    bin_string = list()
    
    #Create list of each character's ASCII value as integer,
    #then convert ascii value to binary
    for c in string:
        bin_c = bin(int(ord(c)))
        bin_c = bin_c.replace('b', '')
        
        grouping = list()
        for n in range(0, len(bin_c), 2):
            pair = bin_c[n:n+2]
            grouping.append(pair)
        
        bin_string.append(tuple(grouping))

    return bin_string


def map_constellation(bin):
    cons = CSKConstellation(len(bin) * 4) #Each character should be 8 bits sorted into 4 2-bit packages
    
    i = 0
    for c in bin:
        for p in c:
            co = bit_transform[p]
            color_point = CSKPoint(co[0], co[1], co[2])
            cons.add_point(i, color_point)
            i += 1

    return cons