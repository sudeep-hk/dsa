def get_hash(key):
    sum=0
    for c in key:
        sum = sum+ ord(c)
    return sum % 100

print(get_hash('march 46546'))
