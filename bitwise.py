a = 13
b = 11

print("BITWISE AND")
print(a&b) #Bitwise AND
print("BITWISE OR")
print(a|b) #Bitwise OR
print("BITWISE XOR")
print(a^b) #Bitwise XOR
print("BITWISE NOT")
print(~a) #Bitwise NOT
print("BITWISE LEFT SHIFT")
# Bitwise Left Shift
print(a<<1)#Left Shift is adding zeroes at the end of the right bit
# Bitwise Right Shift
print(a>>4)#Right Shift is removing bits from right
print("{0:b}".format(a<<1))
print("{0:b}".format(a>>4))
print(bin(13), bin(13<<8))


print("{0:b}".format(65))
print(65<<1)
print("{0:b}".format(65<<1))