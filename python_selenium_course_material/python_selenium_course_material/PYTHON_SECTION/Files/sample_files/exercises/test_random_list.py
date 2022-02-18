email = "middelhove@msn.com"
spl_char = "@"
print("The original string : " + str(email))
domain = email.partition(spl_char)[2]
print(domain)

