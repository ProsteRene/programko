rychlost = float(input("jak rychle beži kůň: "))

if rychlost < 0:
	print("tvůj kůň couva")

elif rychlost == 0:
	print ("tvůj kůň stoji")

elif rychlost <= 8:
	print("tvůj kůň děla kroky")

elif rychlost <= 15:
	print("tvůj kůň děla klusa")

elif rychlost <= 30:
	print ("tvůj kůň děla cval")

else:
	print ("tvůj kůň děla raketu")