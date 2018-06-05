import xml.etree.ElementTree as etree

def cost_to_cmc(cost):
    if cost is None:
        return 0
    cost = cost.replace('X', '')
    index = 0
    num = ''
    number = 0
    while index < len(cost):
        num += cost[index]
        try:
            number = int(num)
        except:
            break
        index += 1
    return number + len(cost) - index - 2*len([c for c in cost if c == '/'])


tree = etree.parse('carddata.xml')
root = tree.getroot()

print(len(root))
cards = []
for card in root:
    text = card.findall('rules')[0].text
    name = card.findall('name')[0].text
    cost = card.findall('cost')[0].text
    rarity = card.findall('rarity')[0].text
    type_element = card.findall('type')[0]
    type_line = type_element[0].text + ' - ' + (type_element[1].text or '')
    card = {
        'text': text,
        'name': name,
        'cost': cost,
        'rarity': rarity,
        'type_line': type_line
        }
    cards.append(card)


rarities = {
    'C': 1/15,
    'U': 1/15,
    'R': 1/20,
    'S': 1/15,
    'M': 0
    }


def calc_as_fan(fun):
    matching = [c for c in cards if fun(c)]
    as_fan = sum(rarities[c['rarity']] for c in matching)
    return as_fan

counterfalls = calc_as_fan(lambda c: '+1/+1 counter' in (c['text'] or '').lower())
print(counterfalls)

for i in range(8):
    as_fan = calc_as_fan(lambda c: 'Land' not in c['type_line'] and cost_to_cmc(c['cost']) == i)
    print(i, as_fan)