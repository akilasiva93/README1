
def round_to_two_places(num):
    x = round(num,-2)
    print(x)
    return x

round_to_two_places(3.3346)

def to_smash(candies,persons):
    if not persons:
       persons = 3
    y = candies%persons
    print(y)
    return y

to_smash(203,2)
to_smash(302,())


a = -10
b = 5
# # Which of the two variables above has the smallest absolute value?
x = abs(a)
y = abs(b)
print (min(x, y))

def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

def can_run_for_president(nature_citizen,age):
   return nature_citizen and (age >= 35)

print (can_run_for_president(True,36))
print (can_run_for_president(False,36))
print (can_run_for_president(True, 34))

print (bool(""))
print (bool("1234"))

