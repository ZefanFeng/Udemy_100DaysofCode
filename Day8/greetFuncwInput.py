# function with inputs 

def greet(name, location):
  import time

  local_time = time.asctime(time.localtime(time.time()))
  print(f"Good Morning! {name}")
  print(f"it's {local_time}today")
  input(f"How s the weather today in {location}?\n")

greet("Zefan", "Boston")

