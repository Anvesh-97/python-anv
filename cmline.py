
final1 = ""
while True :
    str1 = input("Enter a string until 'done'")
    if str1!='done':
        final1 = final1 + str1
        continue
    else :
        break

print(final1)