import sys

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
    'b major': ['B', 'C#', 'D', 'E', 'F#', 'G#', 'A#'],
    'c minor': ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#'],
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


def chord_generator(chord_args):
    # Separate chord from additional tone
    chord, add_tone = ' '.join(chord_args[:2]), chord_args[2:]
    if chord in SCALE:
        scale = Key(SCALE[chord])
        extra_intervals = {'seventh': scale.seventh,
                           'sixth': scale.sixth,
                           'ninth': scale.ninth,
                           'sus': scale.sus}
        # Check if an additional tone was provided
        if add_tone:
            # Check if additional tone is valid
            if add_tone[0] in extra_intervals:
                print(', '.join(extra_intervals[add_tone[0]]))
                return
        # Print regular third
        print(', '.join(scale.third))
    else:
        print("Chord not valid.")
       
#if sys.argv[1:]:
#    scale = sys.argv[1:]
#    scale = [thing.lower() for thing in scale]
#else:
#    scale = input('Enter the name of the chord you want: ').lower().strip().split()
#chord_generator(scale)

#create progression and join every two elements
progression = input('Enter the chord sequence you want: ').lower().strip().split()
for x in progression:
    list_name = [x, progression[progression.index(x) + 1]]
    triad = ' '.join(list_name)
    print(triad)

#if SCALE[triad]:
#    y = SCALE[' '.join(x, progression[x + 1], progression[x + 2])]
#    if SCALE[y]:
#        chord_generator(y)
#    else:
#        y = ' '.join(x, progression[x + 1])
#        chord_generator(y)
