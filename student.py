import sys
   #check if correct number of argument a
if len(sys.argv) != 3:
   print("Usage: python student.py <name> <roll no>") sys.exit(1)

# sys.argv[0] is always the program name
script_name = sys.argv[0]
name = sys.argv[1]
rollno = sys.argv[2]

print("Script name:", script_name)
print("Student name:", name)
print("Roll number:",rollno)
