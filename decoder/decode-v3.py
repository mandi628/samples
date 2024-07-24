#! /usr/bin/env python3

filename = input("Enter the filename you'd like to decode: ")
#file = open("messages/message_file1.txt")
file = open(filename)
message_file = file

msg = {'6': 'computers', '3': 'love', '1': 'I', '4': 'dogs', '5': 'you', '2': 'cats', '7': 'meet', '8': 'elephants', '9': 'parade', '0': 'party', 's': 'Suzi', 't': 'Tess', 'm': 'Micky', 'h': 'Ashleigh', 'a': 'Abbie', 'c': 'Mama'
}

def text():
	text = []
	for text in message_file:
		text = message_file.readlines()
		return text

def char():
	x = 0
	char = []
	while x < len(text):
		char.append(text[x][-2])
		x += 1
	return char

def decode(message_file): # ? Would this still work if I didn't have the "message_file" parameter here?
	y = 0
	junk = []
	while y < len(char):
		junk.append(msg.get(char[y]))
		y += 1
	return junk

text = text()
#print("Text = %s" % text)

char = char()
#print("Characters = %s" % char)

junk = decode(message_file)
msg = ' '.join([str(word) for word in junk])
print(msg)
file.close()

#z = 0
#while z < len(junk):


# I noticed one tiny flaw. When reading the text file in the text(), it is starting with line 2 of the file, instead of line 1. Is that an indexing thing?
