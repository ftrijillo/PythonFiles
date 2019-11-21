test = ['"mgmtInt += 1 if v6Neighbor % \'fe80::[12]\' and Interface == \'mgmt\'"',
       '"inInt += 1 if v6Neighbor % \'fe80::[12]\' and Interface == \'inside\'"',
       '"outInt += 1 if v6Neighbor % \'fe80::[12]\' and Interface == \'outside\'"',]

print(type(test))
print(test)
print(test[1])
