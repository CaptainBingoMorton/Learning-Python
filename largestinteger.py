def largestinteger(listofintegers):
    smolchungus=listofintegers[0]
    for bigchungus in listofintegers:
        if smolchungus < bigchungus:
            smolchungus=bigchungus
    return smolchungus

print (largestinteger([10,10000000,100000000000000000000000000000000000000000000000000000000000000000000000000]))