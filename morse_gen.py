import wave
import random


option = input('(r)andom text, or (i)nput text? ')
if option.lower() == 'r':
    number_of_words = int(input('how many words in the generated string? '))
    wordlist = []
    string = ''
    f = open('wordsEn.txt', 'r')
    for i in f:
        wordlist.append(i)
    for i in range(number_of_words):
        linenum = random.randint(0, len(wordlist))
        string += wordlist[linenum][:-1] + ' '
else:
    string = input('convert this to morse: ')



outfile = input('name the .wav file: ') + '.wav'
lowercase = list(string.lower())

morse_letters = {'a':'. -',
              'b':'- . . .',
              'c':'- . - .',
              'd':'- . .',
              'e':'.',
              'f':'. . - .',
              'g':'- - .',
              'h':'. . . .',
              'i':'. .',
              'j':'. - - -',
              'k':'- . -',
              'l':'. - . .',
              'm':'- -',
              'n':'- .',
              'o':'- - -',
              'p':'. - - .',
              'q':'- - . -',
              'r':'. - .',
              's':'. . .',
              't':'-',
              'u':'. . -',
              'v':'. . . -',
              'w':'. - -',
              'x':'- . . -',
              'y':'- . - -',
              'z':'- - . .', }

morse_nums = {'1':'. - - - -',
              '2':'. . - - -',
              '3':'. . . - -',
              '4':'. . . . -',
              '5':'. . . . .',
              '6':'- . . . .',
              '7':'- - . . .',
              '8':'- - - . .',
              '9':'- - - - .',
              '0':'- - - - -', }

morse_string = ''
filename_list = []

for i in lowercase:
    if ord(i)>=97 and ord(i)<=122:
        morse_string += morse_letters[i]
    elif ord(i)>=48 and ord(i)<=57:
        morse_string += morse_nums[i]
    elif i == ' ':
        #original ' '
        morse_string += ' '
    else:
        #original ' '
        morse_string += ' '
        break
    #original '  '
    morse_string += '  '

for j in morse_string:
    if j == '.':
        filename_list.append('dit.wav')
    elif j == '-':
        filename_list.append('dah.wav')
    else:
        filename_list.append('space.wav')
        


data = []
w = wave.open(filename_list[0], 'rb')
params = w.getparams()
for infile in filename_list:
    w = wave.open(infile, 'rb')
    data.append( w.readframes(w.getnframes()) )

output = wave.open(outfile, 'wb')
output.setparams(params)
for i in data:
    output.writeframes(i)
output.close()
