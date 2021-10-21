'''Ceaser Cipher to encrype or decrype letters'''

try:
    import pyperclip # pyperclic copies text to the clipboard
except ImportError:
    pass #if pyperclipn is not installed do nothing it is no big deal

#every possible symber than can be encryped /decrypted
# symbols
SYMBOLS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Ceaser cipher')
print('The ceasar cipher encrypts letters by shifting them over by a')
print('Key number. for example a key of 2 means the letter A is')
print('encryped into C the letter B encrypted into D and so on')
print()

#let the user enter if they are encrypting or decrypting
while True: #keep asking until enters e or d
    print('Do you want to (e)ncrypt or (d)ecrypt')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('PLease enter the leter e or d')

#let the user enter the key to use:
while True: # kepp asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {maxKey}) to use')
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

#let the user enter the message to encrypt/decrypt:
print(f"Enter the message to {mode}")
message = input('> ')

# caesar cipher only works on uppercase letters
message = message.upper()

#stores the encryped /decrypted from of the message
translated = ''

#encrypt/decrypt each symbol in the message
for symbol in message:
    if symbol in SYMBOLS:
        #get the encrtypted or decrypted number for this symbol
        num = SYMBOLS.find(symbol) # get the number of the symbol
        if mode =='encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # handle the wrap around if num i slarger than lengtjh of symbols or less than 0:
        if num >= len(SYMBOLS):
                num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        #ADD encrypted decryoted numbers symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        # just add the symbol without encryoting/decrypting
        translated = translated + symbol

# display the encryped /decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard')

except:
    pass # do notjging if pyper cli was not intealed



