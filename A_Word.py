s = input()
number_upper_letter = 0
number_lower_letter = 0
for letter in s:
    if letter.islower():
        number_lower_letter +=1
    else:
        number_upper_letter +=1
if (number_lower_letter == number_upper_letter) or (number_lower_letter > number_upper_letter):
    print(s.lower())
else:
    print(s.upper())