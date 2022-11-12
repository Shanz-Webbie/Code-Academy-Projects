# Write your large_power function here:

def large_power(base, exponent):
  powered_base = base ** exponent
  if powered_base > 5000:
    return True
  else:
    return False

print(large_power(2, 13))
#should print True
print(large_power(2, 12))
# should print False