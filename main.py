def save(line: str):
  with open("newFile.py", "a") as newFile:
    newFile.write(line)

def clean_line(line: str):
  if line.__contains__("#"):
    line = line.split("#")[0] + "\n"
    return line
  else: 
    return line

with open("orginal.py", "r") as orginalFil:
  for line in orginalFil:
    save(clean_line(line))
  print("Cleaned file")