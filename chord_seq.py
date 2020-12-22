class Key:
    
    def __repr__(self):
        return '{scale}'.format(scale = self.scale)
        
    def __init__(self, scale):
        self.scale = scale
        self.third = scale[0], scale[2], scale[4]
        self.ninth = scale[0], scale[2], scale[4], scale[1]
        self.seventh = scale[0], scale[2], scale[4], scale[6]
        self.sus = scale[0], scale[2], scale[4], scale[3]
        self.sixth = scale[0], scale[2], scale[4], scale[5]
    
    
#def extra_int(self, triad):


        
SCALE = {
    'a minor': ['A', 'B', 'C', 'D', 'E', 'F', 'G'] ,
    'a major': ['A', 'B', 'CS', 'D', 'E', 'FS', 'GS'],  
    'b minor': ['B', 'CS', 'D', 'E', 'FS', 'G', 'A'],
    'b major': ['B', 'CS', 'D', 'E', 'FS', 'GS', 'AS'],
    'c minor': ['C', 'D', 'DS', 'F', 'G', 'GS', 'AS'],
    'c major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'd minor': ['D', 'E', 'F', 'G', 'A', 'AS', 'C'],
    'd major': ['D', 'E', 'FS', 'G', 'A', 'B', 'CS'],
    'e minor': ['E', 'FS', 'G', 'A', 'B', 'C', 'D'],
    'e major': ['E', 'FS', 'GS', 'A', 'B', 'CS', 'DS'],
    'f minor': ['F', 'G', 'GS', 'AS', 'C', 'CS', 'DS'],
    'f major': ['F', 'G', 'A', 'AS', 'C', 'D', 'E'],
    'g minor': ['G', 'A', 'AS', 'C', 'D', 'DS', 'F'],
    'g major': ['G', 'A', 'B', 'C', 'D', 'E', 'FS']
}

#get chord from user 
scale = input('enter name of chord you want: ').lower().strip()
#separate segments of chord 
chord = scale.split()
chord.append('')
scale = Key(SCALE[scale])

add_tone = input('Enter any add tones : ').lower().strip()

extra_intervals = {'seventh': scale.seventh,
            'sixth': scale.sixth,
            'ninth': scale.ninth,
            'sus': scale.sus
}

add_tone = extra_intervals[add_tone]
print(add_tone)


#print(scale.third)

#triad = chord(scale)
#print(scale.third)