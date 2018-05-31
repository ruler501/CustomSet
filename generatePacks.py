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
for i in range(5):
    pack = []
    for _ in range(4):
        pack.append("Com" + commanders[-1])
        commanders.pop()
    with open(str(i+1)+"-commander-pack.txt", 'w') as packFile:
        packFile.write('\n'.join(pack))
for i in range(15):
    pack = []
    for _ in range(1):
        pack.append("S" + lands[-1])
        lands.pop()
    for _ in range(2):
        pack.append("R" + rares[-1])
        rares.pop()
    for _ in range(4):
        pack.append("U" + uncommons[-1])
        uncommons.pop()
    for _ in range(8):
        pack.append("C" + commons[-1])
        commons.pop()
    packs.append(pack)
    with open(str(i+1)+"-pack.txt", 'w') as packFile:
        packFile.write('\n'.join(pack))