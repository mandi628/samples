#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 3: Strings

#print("Challenge 026")
# Pig Latin takes the first consonant of a word, moves it to the end of the word
# and adds on an "ay". If a word begins with a vowel you just add "way" to the
# end. For example, pig becomes igpay, banana becomes ananabay, and aadvark
# becomes aadvarkway. Create a program that will ask the user to enter a word and
# change it into Pig Latin. Make sure the new words is displayed in lower case.
#word = input("Enter a word: ")
#first = word[0]
#length = len(word)
#rest = word[1:length]

#if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
#    newword = rest + first + "ay"
#else:
#    newword = word + "way"
#print(newword)

phrase = input("Enter a phrase you would like to translate to Pig Latin\n::")
words = phrase + " "

found_words = ()
start = 0
end = 0

for char in words:
    if char == " ":
        found_words = found_words + (phrase[start:end],)
        start = end + 1
        end = end + 1
    else:
        end = end + 1

latin = ()

for word in found_words:
    first = word[0]
    length = len(word)
    rest = word[1:length]
    if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
        newword = rest + first + "ay"
        latin = latin + (newword,)
    else:
        newword = word + "way"
        latin = latin + (newword,)

res = ' '.join([str(pig) for pig in latin])
print("Your phrase, translated to Pig Latin is\n::", (str.capitalize(res) + "."))
