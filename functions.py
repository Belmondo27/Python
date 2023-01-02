
def convetToSeconds(hours, minutes):
   return ((hours*60) + minutes) * 60


def convetToHours(minutes):
    hours = (minutes) / 60
    return hours

seconds = convetToSeconds(3, 25)
print(seconds)

hours = convetToHours(120)
print(hours)

def cube(a):
    return a**3

firstexc = cube(2)
print(firstexc)

firstexc = cube(3)
print(firstexc)

firstexc = cube(4)
print(firstexc)

def greet(a):
    return "Hello " + a + " !"

secondexc = greet("Damian")
print(secondexc)