import sys
   #check if correct number of argument a
if len(sys.argv) != 5:
   print("Usage: python empoloye.py <name> <userid> <salary> <expirence>") 
   sys.exit(1)

# sys.argv[0] is always the program name
script_name = sys.argv[0]
name = sys.argv[1]
userid = sys.argv[2]
salary = sys.argv[3]
expirence = sys.argv[4]

print("Script name:", script_name)
print("employe name:", name)
print("empolye id:",id)
print("employe salary:",salary)
print("employe expirence:",expirence)
