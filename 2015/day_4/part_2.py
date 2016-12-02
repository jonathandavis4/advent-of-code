import hashlib

secret_key = 'yzbqklnj'

n = 0
while True:
    n += 1
    key = '{}{}'.format(secret_key, str(n))
    
    md5 = hashlib.md5()
    md5.update(key)
    if md5.hexdigest()[:6] == '000000':
        print n
        break
