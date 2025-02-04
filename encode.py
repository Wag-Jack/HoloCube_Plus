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

class CSKConstellation:
    #Ensure that size of constellation remains consistent throughout implementation
    def __init__(self, points):
        self.points = []
        self.size_of_constellation = len(self.points)


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
    constellation = list()
    
    for c in bin:
        for p in c:
            constellation.append(bit_transform[p])

    return constellation


transmission = input('Please give a string to transmit: ')
binary_grouping = convert_to_binary(transmission)
for n in binary_grouping:
    print(type(n))
print(binary_grouping)
sent_constellation = map_constellation(binary_grouping)
print(sent_constellation)
display_transmission(sent_constellation)