import datetime #This is a module 
import math

today = datetime.datetime.now()
shift = datetime.timedelta(weeks=12)

print(today)
print(today + shift)

print(math.fabs(-55))
print(math.factorial(5))
print(math.gcd(30,6))

message = hashlib.sha256()
message.update(b"Hello world!")
print(message.digest())
print(message.hex)