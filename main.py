prijs1 = float(input('wat is de prijs '))
korting1 = int(input('wat is de korting '))
prijs2 = prijs1 / 100
korting2 = prijs2 * korting1
prijs3 = prijs1  - korting2
print ('je betaaalt', round(prijs3, 2), "euro" )