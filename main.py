rotorOptions = {
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

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert(letter, a, b, offset):
    index = a.find(letter)
    index += offset
    if index > 25:
        index -= 26
    print(letter, b[index])
    
    return b[index]



def enigma(letter, rotors, reflector):

    for rotor in rotors:
        letter = convert(letter, alpha, rotor[0], rotor[1])
    
    letter = convert(letter, alpha, reflector, 0)

    for rotor in reversed(rotors):
        letter = convert(letter, rotor[0], alpha, -rotor[1])
    
    print(letter)


rotors = [ 
    [rotorOptions[1], 0], 
    [rotorOptions[2], 0], 
    [rotorOptions[3], 0],
]

reflector = reflectors['B']

enigma('A', rotors, reflector)



