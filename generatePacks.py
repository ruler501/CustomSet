# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:06:52 2018

@author: Devon Richards
"""

import glob
import os
from random import shuffle

os.chdir("CardImages")
cards = glob.glob("*.jpg")
cards = [card[:-4] for card in cards]

commanders = [card[3:] for card in cards if card.startswith("Com")]
rares = [card[1:] for card in cards if card.startswith("R")]
lands = [card[1:] for card in cards if card.startswith("S")]
uncommons = [card[1:] for card in cards if card.startswith("U")]
commons = [card[1:] for card in cards if card.startswith("C") and not card.startswith("Com")]
commons += commons

shuffle(commanders)
shuffle(rares)
shuffle(lands)
shuffle(uncommons)
shuffle(commons)

print(len(commanders), "Commanders")
print(len(rares), "Rares")
print(len(lands), "Lands")
print(len(uncommons), "Uncommons")
print(len(commons), "Commons")
packs = []
for i in range(20):
    pack = []
    pack.append("Com" + commanders[-1])
    commanders.pop()
    pack.append("R" + rares[-1])
    rares.pop()
    pack.append("S" + lands[-1])
    lands.pop()
    for _ in range(3):
        pack.append("U" + uncommons[-1])
        uncommons.pop()
    for _ in range(10):
        pack.append("C" + commons[-1])
        commons.pop()
    packs.append(pack)
    with open(str(i+1)+"-pack.txt", 'w') as packFile:
        packFile.write('\n'.join(pack))