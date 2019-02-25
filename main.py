rotors = {
    0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
    2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
    3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
}

reflectors = {
    'A':'EJMZALYXVBWFCRQUONTSPIKHGD',
    'B':'YRUHQSLDPXNGOKMIEBFZCWVJAT',
    'C':'FVPJIAOYEDRZXWGCTKUQSBNMHL',
}


def enigma(letter):
    alpha = rotors[0]
    
    # alpha => rotor
    for i in range(1,4):
        rotor = rotors[i]
        index = alpha.find(letter)
        newLetter = rotor[index]
        print(f'{letter} => {newLetter}')
        letter = newLetter
    
    # reflect
    reflector = reflectors['B']
    index = alpha.find(letter)
    newLetter = reflector[index]
    print(f'{letter} => {newLetter}')
    letter = newLetter

    # rotor => alpha
    for i in range(1,4):
        rotor = rotors[4-i]
        index = rotor.find(letter)
        newLetter = alpha[index]
        print(f'{letter} => {newLetter}')
        letter = newLetter


enigma('A')


'''
Alpha => Rotor
A => E
E => S
S => G

Reflect:
G => L

Rotor => Alpha
L => F
F => W
W => N

0:'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # alpha
1:'EKMFLGDQVZNTOWYHXUSPAIBRCJ' # rotor1
2:'AJDKSIRUXBLHWTMCQGZNPYFVOE' # rotor2
3:'BDFHJLCPRTXVZNYEIWGAKMUSQO' # rotor3

B:'YRUHQSLDPXNGOKMIEBFZCWVJAT' # reflector

'''


