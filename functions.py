
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

def convert_cel_to_far(c):
    return c * (9/5) + 32

def convert_far_to_cel(f):
    return (f - 32) * 5 / 9



num = float(input("Enter a temperature in degrees C: "))
far = convert_cel_to_far(num)
print(num, "degrees C = ", round((far),4) , "degrees F"  )


num = float(input("Enter a temperature in degrees F: "))
far = convert_far_to_cel(num)
print(num, "degrees F = ", round((far),2) , "degrees C"  )