first_name= "Damian"
last_name = "Zakryś"
full_name = first_name + " " + last_name
print(full_name)
print(len(full_name))
print(first_name[2])
print(last_name[-1])
print(first_name[0:6])
word = "ZINGBA"
word = "ba" + word[:4] + "a"
word.lower()
print(word.lower())
test="CHOMIK"
print(test.lower())
print(test.lstrip().lower())
print(test.startswith("CH"))
print(test.endswith("MIK"))
test=test.lower()
print(test.startswith("CH"))
##############################################################

var1 = "Animals"
var2 = "Badger"
var3 = "Honey Bee"
var4 = "Honey Badger"
print(var1.lower() + " " + var2.lower() + " " + var3.lower() + " " + var4.lower())
print(var1.upper() + " " + var2.upper() + " " + var3.upper() + " " + var4.upper())

string1 = "   Filet Mignon"
string2 = "Brisket   "
string3 = "   Cheeseburger   "
print(string1)
print(string2)
print(string3)
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

string4 = "Becomes"
string5 = "becomes"
string6 = "BEAR"
string7 = "   bEautigul"
print(string4.startswith("be"))
print(string5.startswith("be"))
print(string6.startswith("be"))
print(string7.startswith("be"))

print(string4.startswith("Be"))
print(string5.startswith("be"))
print(string6.startswith("BE"))
print(string7.startswith("   "))
####
prompt="Hey, what's up?! "
user_input = input(prompt)
print("You say: " + user_input)

disp=input()
print(disp.lower())
print(len(disp))
