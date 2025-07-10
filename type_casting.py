#type_casting = the process of converting a variable from one date type to another
#               str(), int(), float(), bool()
#---------------------------------------------------------
name = "Mike"
age = 24
gpa = 3.7
is_student = False

print(type(is_student))
#----------------------------------------------------------
gpa = int(gpa)
#age = float(age)
age = str(age)



print(gpa)
print(age)
print(type(age))
#-----------------------------------------------------------
age = 24
age = str(age)
age += "1"
print(age)
#--------------------------------------------------------------
name = "Jimmy"
#name = ""  False
name = bool(name)

print(name)
