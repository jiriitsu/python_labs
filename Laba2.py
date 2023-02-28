def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def generate_twins(start, end):
   for i in range(start, end):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
         print("{:d} и {:d}".format(i, j))

print("Числа-близнецы от 2 до 1000:")
generate_twins(2, 1001)

#2 способ
def is_prime1(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

for i in range(2, 1001):
    if is_prime1(i) and is_prime1(i + 2):
        print("{:d} и {:d}".format(i, i+2))

print()

    
