#this program simulates proof of work concept
#used by miners when calculating transaction blocks on the cryptocurrency blockchain network
#I designed this program as I wass studying about the cryptocurrency blockchain
import hashlib
import time
import os

def run():
    max_value = 1000                #the initial maximum value the the hash should equate to
    
    for z in range(0,1000):         
        counter = 0                 #counter represents the nonce, the value change in the block to find the min value
    
        data = os.urandom(256)
        start_time = time.time()
        while True:
            #the counter represents the nonce, while data represents a block of transactions
            hash_value = hashlib.md5((counter.to_bytes(32, 'big'))+ data).hexdigest()
            value = convert_to_decimal(hash_value)
            
            if value <= max_value:
                print('Minimun Hash :', hash_value, 'value',value, 'counter',counter ,'Max value', max_value,'time :',(time.time()-start_time))
                break
            counter += 1
        max_value -= 1               #decrementing the max value increases the difficulty
        

def convert_to_decimal(hash_value):
    value = 0
    for i in hash_value:
        value += int(i, 16) #converts to int

    return value

if __name__=='__main__':
    run()