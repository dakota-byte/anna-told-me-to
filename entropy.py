# entropy.py
# a program to calculate the entropy of string
# assumed to be generated from the english alpabet

# frequencies of the english alphabet, counted from the Concise Oxford Dictionary 
# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# hindsight I could've just used https://www.dcode.fr/frequency-analysis
# double hindsight one should not simply CONVERT THE HEX TO AsCII
P = {
    "A": 0.084966,
    "B": 0.020720,
    "C": 0.045388,
    "D": 0.033844,
    "E": 0.111607,
    "F": 0.018121,
    "G": 0.024705,
    "H": 0.030034,
    "I": 0.075448,
    "J": 0.001965,
    "K": 0.011016,
    "L": 0.054893,
    "M": 0.030129,
    "N": 0.066544,
    "O": 0.071635,
    "P": 0.031671,
    "Q": 0.001962,
    "R": 0.075809,
    "S": 0.057351,
    "T": 0.069509,
    "U": 0.036308,
    "V": 0.010074,
    "W": 0.012899,
    "X": 0.002902,
    "Y": 0.017779,
    "Z": 0.002722,
} # sum = 1.0000010000000001 (silly computer)

# I will use shannons entropy formula to calculate the
# amount of information stored in each string

# can I call this the amount of "english" information? if "english"
# is defined to be the set of english alphabets. well actually
# its "hexadecimal" information

file = open("challenge.txt", "r") # begin analysis

for line in file:
    print(line)

f.close() # end analysis

# TOO MUCH HOMEWORK :(