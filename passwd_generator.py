import random

passwd = ""
i = 0
abc = "abcdefghijklmnoprstuvyzqwx"
ABC = "ABCDEFGHIJKLMNOPRSTUVYZQWX"
dots = "!'^+%&/()=?_-*.:,;<>|#$}{[]@"
numbers = "0123456789"
list1 = [abc, ABC, dots, numbers]

count = int(input("Hey! We are here to give you a strong password.\nIf you want a strong password you have to enter the lengt above 8.\nSo please give us length of the password:"))

while i < count:
	random1 = random.choice(list1)
	random2 = random.choice(random1)
	print(random2)
	passwd = passwd + random2

	i += 1
print("Here is your very strong password:\n" + passwd)