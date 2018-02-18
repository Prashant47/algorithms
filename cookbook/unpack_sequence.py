# unpack all values
p = (3, 5)
x, y = p
# skipping valus in unpack
data = ['abc',50, 8.3, (2018,2,15)]
_, val, floating, _ = data
print(val,floating)

# unapack from iterable of arbitary length 
# ( Python3 only ) use * expression in python

data = ['Prashant', 'abc@xyz.com', 45.6, 67.8]
name, email, *vals = data
print(name, email, vals)

# * with _
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_ , (*_, year ) = record
print(name, year)
