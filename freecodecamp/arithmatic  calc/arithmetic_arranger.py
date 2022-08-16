def arithmetic_arranger(problems, display = False):
  lst = []
  max_length = []
  length_required = []

  for i in range(len(problems)):
    lst.append(problems[i].split(" "))

  #Checking Conditions
  if len(lst) > 5:
    arranged_problems_error= "Error: Too many problems."
    return arranged_problems_error

  for i in range(len(lst)):
    
    #Extra condition
    if(len(lst[i]) != 3):
      arranged_problems_error = "Error: Expression must only contain 2 operands and 1 operator."
      return arranged_problems_error

    if lst[i][1] != '+' and lst[i][1] != '-':
      arranged_problems_error = "Error: Operator must be '+' or '-'."
      return arranged_problems_error
    
    try:
      lst[i][0] = int(lst[i][0])
      lst[i][2] = int(lst[i][2])
    except:
      arranged_problems_error = "Error: Numbers must only contain digits."
      return arranged_problems_error
    
    #length of the longest operand
    max_length.append(max(len(str(lst[i][0])), len(str(lst[i][2]))))
    length_required.append(int(max_length[i]) + 2)

    if lst[i][0] > 9999 or lst[i][2] > 9999:
      arranged_problems_error = "Error: Numbers cannot be more than four digits."
      return arranged_problems_error

  arranged_problems = ""

  #first line
  for i in range(len(lst)):
    space_required = length_required[i] - len(str(lst[i][0]))
    for j in range(space_required):
      arranged_problems += " "
    arranged_problems += str(lst[i][0]) + "    "

  arranged_problems = arranged_problems.rstrip()
  arranged_problems += "\n"

  #second line
  for i in range(len(lst)):
    arranged_problems += lst[i][1]
    space_required = length_required[i] - len(str(lst[i][2])) - 1
    for j in range(space_required):
      arranged_problems += " "
    arranged_problems += str(lst[i][2]) + "    "

  arranged_problems = arranged_problems.rstrip()
  arranged_problems += "\n"

  #dashed line
  for i in range(len(lst)):
    for j in range(length_required[i]):
      arranged_problems += "-" 
    arranged_problems += "    "
  
  arranged_problems = arranged_problems.rstrip()

  #Display is set to False
  if(not display):
    return arranged_problems

  #Display is set to True
  arranged_problems += "\n"
  for i in range(len(lst)):
    if lst[i][1] == "+":
      temp_result = lst[i][0] + lst[i][2]
    else:
      temp_result = lst[i][0] - lst[i][2]
    space_required = length_required[i] - len(str(temp_result))
    for j in range(space_required):
      arranged_problems += " "  
    arranged_problems += str(temp_result) + "    "
  
  arranged_problems = arranged_problems.rstrip()
  return arranged_problems