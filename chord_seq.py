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
    
    
SCALE = {
    'a minor': ['A', 'B', 'C', 'D', 'E', 'F', 'G'] ,
    'a major': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],  
    'b minor': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A'],
    'b major': ['B', 'C#' 'D', 'E', 'F#', 'G#', 'A#'],
    'c minor': ['C', 'D', 'D#', 'F', 'G', 'GS', 'AS#'],
    'c major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'd minor': ['D', 'E', 'F', 'G', 'A', 'A#', 'C'],
    'd major': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    'e minor': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
    'e major': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    'f minor': ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#'],
    'f major': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'],
    'g minor': ['G', 'A', 'A#', 'C', 'D', 'D#', 'F'],
    'g major': ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
}

scale = input('Enter the name of the chord you want: ').lower().strip().split()

def chord_generator(scale):
    chord, add_tone = ' '.join(scale[:2]), scale[2:]
    #get scale from SCALE dictionary 
    scale = Key(SCALE[chord])
    #DICTIONARY for add tones 
    extra_intervals = {'seventh': scale.seventh,
                'sixth': scale.sixth,
                'ninth': scale.ninth,
                'sus': scale.sus
    }
    #adding add tone into chord
    if add_tone:
        # Check if additional tone is valid
        if add_tone[0] in extra_intervals:
            print(', '.join(extra_intervals[add_tone[0]]))
        else:
            print('Unrecognized additional tone "{}".'.format(add_tone[0]))
    else:
        # Print regular third
        print(', '.join(scale.third))
       

    
chord_generator(scale)

#progression = input('Enter the chord sequence you want: ').lower().strip()
#print(progression)
#for x in progression:
#join two elements
#    x = ' '.join(x, progression[x + 1])
#    if SCALE[x]:
#        x = SCALE[' '.join(x, progression[x + 1], progression[x + 2])]
#        if SCALE[x]:
#            chord_generator(x)
#        else:
#            x = ' '.join(x, progression[x + 1])
#            chord_generator(x)