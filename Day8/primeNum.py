#Write your code below this line 👇
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
    # or for j in range(2, int(math.sqrt(i))+1), since < squrt
    # or for j in res. res = [prime]
      is_prime = False
  if is_prime:
      print(f"number {number} is not a prime.")
  else:
      print(f"number {number} is a prime.")





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



