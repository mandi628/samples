#! /usr/bin/env python3

message_file = open(input("Enter the filename you'd like to decode: "), "r").readlines()
#print("message_file: ", message_file)
#return message_file

#filename = input("Enter the filename you'd like to decode: ")
#file = open("msg/msg000.txt")
#file = open(filename, 'r')
#message_file = file

msg = {
    '6': 'computers',
    '3': 'love',
    '1': 'I',
    '4': 'dogs',
    '5': 'you',
    '2': 'cats',
    '7': 'meet',
    '8': 'elephants',
    '9': 'parade',
    '0': 'party',
    's': 'Suzi',
    't': 'Tess',
    'm': 'Micky',
    'h': 'Ashleigh',
    'a': 'Abbie',
    'c': 'Mama',
    'z': 'at',
}

def decode(message_file):
    c = ()
    junk = ()
    i = 0
    while i < len(message_file):
        c = c + (message_file[i][-2],)
        i += 1
#    print("tuple c: ", c)
        return c
    y = 0
    while y < len(c):
        junk = junk + (msg.get(c[y]),)
        y += 1
#    print("tuple junk: ", junk)
        return junk

words = decode(message_file)
#msg = ' '.join([str(word) for word in words])
print(words)
#file.close()

#z = 0
#while z < len(junk):


# I noticed one tiny flaw. When reading the text file in the text(), it is starting with line 2 of the file, instead of line 1. Is that an indexing thing?
