f = open("mening_fayilim.txt", 'w')# fayil yaratish
f.write('salom')
f = open("mening fayilim.txt", 'r')# fayil yaratish
print(f.read())

f =open("mening_fayilim.txt", 'w')
f.write("Davletov ")
f.close()

f= open("mening_fayilm.txt", "r")
print(f.read())
f.close()