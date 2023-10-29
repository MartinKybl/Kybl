from machine import Pin
import time
#project done on Raspberry Pico W
#defining output led

led = Pin("LED", Pin.OUT)
led.off()

#defining the time of a dot and a comma

tdot = 200
tcomma = 3*tdot

#defining the time between words and letters

tword = 7*tdot
tletter = tcomma

#morse dictionary

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

#input data

vstup = input()
seznam = []

#making every letter capital baby

for letter in vstup:
    seznam.append(letter.upper())

i = 0
while(i<len(seznam)):
    
    # spliting morse letters into individual symbol

    print(morseovka_dic[seznam[i]])
    x = list(morseovka_dic[seznam[i]])
    print(x)
    z = 0
    
    #blinking for daddy
    
    for n in range(len(x)):
        y = x[z]
        
        if y ==".":
            led.on()
            
            time.sleep_ms(tdot)
            
            led.off()
            time.sleep_ms(tletter)
        else: 
            if y =="-":
                led.on()
                
                time.sleep_ms(tcomma)
                
                led.off()
                time.sleep_ms(tletter)
            else:
                if y =="/":
                    led.off
                    time.sleep_ms(tword)
                
        z = z + 1    
    
    i = i + 1

print("translation complete")
    

