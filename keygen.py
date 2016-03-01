#keygen example for Unicorn Crackme
# https://reverse.put.as/wp-content/uploads/2010/05/2-Unicorn.zip
# Charles Leerink 2016
#
# Yes I know this is an old one, but hey I did it anyways.....


import hashlib

salt = "+unicorn"

print "#############################################"
print "#       Unicorn CrackMe KeyGen Example      #"
print "#############################################"
print ""
print ""
name = raw_input("Name: ")
md5 = hashlib.md5(name+salt)
final_string = md5.hexdigest()
print "Serial: " + final_string.upper()[0:20]
print ""
print ""






