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

rarities = ["M", "S", "R", "U", "C"]

rarity_map = {}
for rarity in rarities:
    rarity_map[rarity] = [card[1:] for card in cards if card.startswith(rarity)]
    
for key, value in rarity_map.items():
    shuffle(value)
    
for key, value in rarity_map.items():
    print(len(value), key)
    

def generate_packs(count,counts, prefix=''):
    packs = []
    for i in range(count):
        pack = []
        for count, rarity in zip(counts, rarities):
            for _ in range(count):
                pack.append(rarity + rarity_map[rarity][-1])
                rarity_map[rarity].pop()
        with open(str(i+1) + prefix + "-pack.txt", 'w') as packFile:
            packFile.write('\n'.join(pack))
        packs.append(pack)
    return packs


generate_packs(5, [4], prefix='-commander')
generate_packs(15, [0, 1, 2, 4, 8])