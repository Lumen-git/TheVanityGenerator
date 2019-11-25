from bitcoin import *
import time

target = input('Input Target Phrase\n>')

priv = random_key()
addr = pubtoaddr(privtopub(priv))
count = 1

startTime = time.time()
while not addr.lower().startswith('1{}'.format(target)) or addr.lower().startswith('3{}'.format(target)):
    priv = random_key()
    addr = pubtoaddr(privtopub(priv))
    if addr.lower().startswith('1{}'.format(target[:count])):
        print('Current best: {}'.format(addr))
        count += 1

endTime = time.time() - startTime
print('Address: {}\nPrivate Key: {}'.format(addr, priv))
print('Total Time: {}'.format(endTime))
