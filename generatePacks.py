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

def generate_rarity_map(rarities, cards):
    result = {}
    for rarity in rarities:
        result[rarity] = [card[1:] for card in cards if card.startswith(rarity)]
        
    for key, value in result.items():
        shuffle(value)
    
    return result

        
def generate_packs(count,counts, rarities, rarity_map, prefix=''):
    packs = []
    for i in range(count):
        pack = []
        for count, rarity in zip(counts, rarities):
            r = []
            for _ in range(count):
                r.append(rarity + rarity_map[rarity][-1])
                rarity_map[rarity].pop()
            r.sort()
            pack += r
        with open(str(i+1) + prefix + "-pack.txt", 'w') as packFile:
            packFile.write('\n'.join(pack))
        packs.append(pack)
    return packs

rarity_map = generate_rarity_map(rarities, cards)
generate_packs(5, [4], rarities, rarity_map, prefix='-commander')
generate_packs(15, [0, 1, 2, 4, 8], rarities, rarity_map)

rarity_map = generate_rarity_map(rarities, cards)
generate_packs(3, [6, 5, 10, 20, 40], rarities, rarity_map, "-sealed")