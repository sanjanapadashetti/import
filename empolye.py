import sys
   #check if correct number of argument 
if len(sys.argv) !=5:
   print("Usage: python empoloye.py <name> <id> <salary> <experience>") 
   sys.exit(1)

# sys.argv[0] is always the program name
script_name = sys.argv[0]
name = sys.argv[1]
id = sys.argv[2]
salary = sys.argv[3]
experience = sys.argv[4]

print("Script name:", script_name)
print("employe name:", name)
print("id number:",id)
print(" salary:",salary)
print("expirence:",experience)
