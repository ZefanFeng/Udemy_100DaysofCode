# check positive integer since year start from 1.
while True:
  try:
    year = int(input("Which year do you want to check?\n ")) 
    year >= 1
    break
  except ValueError:
    print("please input a positive integer.")
  #except year < 1:
    #print("please input a positive integer.")
    
# evenly divisive by 4, 100, 400
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")



