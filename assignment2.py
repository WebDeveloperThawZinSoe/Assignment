###
# Thaw Zin Soe
# thawzinsoe.dev@gmail.com
# 09403077739
###

recevie_input = input("Enter Any String :")
result = {}

for char in recevie_input:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1
    

print(result)
    