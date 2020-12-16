class Note:
	def __repr__(self):
		return '{name}'.format(name = self.name)
	
	def __init__(self, name, alt, other):
		self.name = name
		self.alt = alt
		self.other = other 
		
		
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

		
A = Note('A', 'a', 'ASb')
B = Note('B', 'b', 'BSb')
C = Note('C', 'c', 'CSb')
D = Note('D', 'd', 'DSb')
E = Note('E', 'e', 'ESb')
F = Note('F', 'f', 'FSb')
G = Note('G', 'g', 'GSb')
AS = Note('A#', 'a#', 'A*')
BS = Note('B#', 'b#', 'B*')
CS = Note('C#', 'c#', 'B*')
DS = Note('D#', 'd#', 'D*')
ES = Note('E#', 'e#', 'E*')
FS = Note('F#', 'f#', 'F*')
GS = Note('G#', 'g#', 'G*')

note_list = [A, B, C, D, E, F, G, AS, BS, CS, DS, ES, FS, GS]

a_minor = [A, B, C, D, E, F, G]
as_minor = [AS, C, CS, DS, F, FS, GS]
a_major = [A, B, CS, D, E, FS, GS]
as_major = [AS, C, D, DS, F, G, A]
b_minor = [B, CS, D, E, FS, G, A]
b_major = [B, CS, D, E, FS, GS, AS]
c_minor = [C, D, DS, F, G, GS, AS]
c_major = [C, D, E, F, G, A, B]
d_minor = [D, E, F, G, A, AS, C]
d_major = [D, E, FS, G, A, B, CS]
e_minor = [E, FS, G, A, B, C, D]
e_major = [E, FS, GS, A, B, CS, DS]
f_minor = [F, G, GS, AS, C, CS, DS]
f_major = [F, G, A, AS, C, D, E]
g_minor = [G, A, AS, C, D, DS, F]
g_major = [G, A, B, C, D, E, FS]		   

keys_list = [a_minor, a_major, b_minor, b_major, c_minor, c_major, d_minor, d_major, e_minor, e_major, f_minor, f_major, g_minor, g_major, g_major]

raw_key = input("Enter the chord you want: ").lower().split()
raw_key.append('')
root = raw_key[0].lower()
third = raw_key[1].lower()
add_tone = raw_key[2].lower()

for note in note_list:
	if root == note.name:
		root = note
		break
	else:
		continue

		
for scale in keys_list:
	if note == scale[0]:
		break
	else:
		continue

		
if third == 'minor':
	if add_tone == '':
		chord = Key(scale)
		print(chord.third)

		
elif third == 'major':
	if add_tone == '':
		scale = keys_list[keys_list.index(scale) + 1]
		chord = Key(scale)
		print(chord.third)

		
#if add_tone == '7' or 'SEVEN' or 'SEVENTH':
#	chord = Key(key)
#	print(chord.seventh)	
#if add_tone == 'sixth':
#	chord = Key(key)
#	print(chord.sixth)