from machine import Pin
import time

led = Pin("LED", Pin.OUT)
led.off()

morseovka_dic = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':'/'
                    }

vstup = input()
seznam = []

for letter in vstup:
    seznam.append(letter.upper())

i = 0
while(i<len(seznam)):
    print(morseovka_dic[seznam[i]])
    x = list(morseovka_dic[seznam[i]])
    
    z = 0
    for n in range(len(x)):
        y = x[z]
        
        if y ==".":
            led.on()
            
            time.sleep_ms(500)
            
            led.off()
            time.sleep_ms(1000)
        else: 
            if y =="-":
                led.on()
                
                time.sleep_ms(1200)
                
                led.off()
                time.sleep_ms(1000)
            else:
                if y =="/":
                    led.off
                    time.sleep_ms(1200)
                else:
                    print("prace dokoncena sefe")

        z = z + 1    
    
    i = i + 1

    

