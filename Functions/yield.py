def generat():

   yield "Welcome"

   yield "to"

   yield "Simplilearn"

gen_object = generat()

print(type(gen_object))

for i in gen_object:

   print(i)