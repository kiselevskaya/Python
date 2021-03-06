

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

hey_jude = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
hello_word = ' .... . .-.. .-.. ---   .-- --- .-. .-.. -.. '
bits_hello ='11001100110011000000110000001100111111001100110000001100111111001100110000001111110011111100111111'


def decodeBits(bits):
    print(bits)
    bits = bits.strip('0')
    t = min([len(s) for s in bits.split('1') + bits.split('0') if s])
    print(t)
    return bits.replace('111'*t, '-').replace('000'*t, ' ').replace('1'*t, '.').replace('0'*t, '').replace('0000000'*t, '   ')


def decodeMorse(morseCode):
    print(morseCode)
    print(' '.join(''.join(MORSE_CODE[char] for char in word.split(' ')) for word in morseCode.strip().split('  ')))
    return ' '.join(''.join(MORSE_CODE[char] for char in word.split(' ')) for word in morseCode.strip().split('  '))


decodeMorse(decodeBits(bits_hello))
