import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

alice_in_wonderland = requests.get('http://www.gutenberg.org/cache/epub/19033/pg19033.txt')
alice_in_wonderland = alice_in_wonderland.text

alice_in_wonderland = alice_in_wonderland.replace('.', '')
alice_in_wonderland = alice_in_wonderland.replace('\n', '')
alice_in_wonderland = alice_in_wonderland.replace('!', '')
alice_in_wonderland = alice_in_wonderland.replace(')', '')
alice_in_wonderland = alice_in_wonderland.replace('(', '')
alice_in_wonderland = alice_in_wonderland.replace('…', '')
alice_in_wonderland = alice_in_wonderland.replace('–', '')
alice_in_wonderland = alice_in_wonderland.replace('?', '')
alice_in_wonderland = alice_in_wonderland.replace('\'', '')
alice_in_wonderland = alice_in_wonderland.replace('-', '')
alice_in_wonderland = alice_in_wonderland.replace('[', '')
alice_in_wonderland = alice_in_wonderland.replace(']', '')
alice_in_wonderland = alice_in_wonderland.replace(',', '')
alice_in_wonderland = alice_in_wonderland.replace(';', '')
alice_in_wonderland = alice_in_wonderland.replace('|', '')
alice_in_wonderland = alice_in_wonderland.replace('_', '')
alice_in_wonderland = alice_in_wonderland.replace('"', '')

#print(alice_in_wonderland)

Wizard_of_Oz = requests.get('http://www.gutenberg.org/cache/epub/55/pg55.txt')
Wizard_of_Oz = Wizard_of_Oz.text

#print(Wizard_of_Oz)

Romeo_Juliet = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
Romeo_Juliet = Romeo_Juliet.text

#print(Romeo_Juliet)

the_odyssey = requests.get('http://www.gutenberg.org/cache/epub/1727/pg1727.txt')
the_odyssey = the_odyssey.text

#print(the_odyssey)

sherlock_holmes = requests.get('http://www.gutenberg.org/files/48320/48320-0.txt')
sherlock_holmes = sherlock_holmes.text

#print(sherlock_holmes)

grimm = requests.get('http://www.gutenberg.org/cache/epub/11027/pg11027.txt')
grimm = grimm.text

#print(grimm)

beowulf = requests.get('http://www.gutenberg.org/cache/epub/981/pg981.txt')
beowulf = beowulf.text

#print(beowulf)

list_of_pronouns = ['he','she','her','him','hers','his']


alice_words = alice_in_wonderland.split()

alice_keys = {}

for word in alice_words:
    
    if word in alice_keys:
        key = alice_keys[word]
        
        alice_keys[word] = key + 1
    else:
        alice_keys[word] = 1

#print(alice_keys)
actions = {}
for i in range(len(alice_words)-1):
    
        if alice_words[i] in list_of_pronouns:
            string = ' '.join([alice_words[i], alice_words[i+1]])
        
            string = string.split();

            if string[0] in actions:
            
                if string[1] in actions[string[0]]:
                    key = actions[string[0]][string[1]]
                    actions[string[0]][string[1]] = key + 1
                else:
                    actions[string[0]][string[1]] = 1
            else:
                actions[string[0]] = {}
                actions[string[0]][string[1]] = 1
        
#print(actions['her'])

she = actions['she']
new_verbs1 = list(she.keys())
plt.bar(range(len(she)), list(she.values()),tick_label= new_verbs1)
plt.xticks(rotation=90)
plt.show()

