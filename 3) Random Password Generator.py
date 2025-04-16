import random, time

start_time = time.time()
options = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\
.!?<>'

print('How many characters do you want your password to be?')
length = int(input())

for i in range(length):
    print(options[random.randint(0, len(options) - 1)], end='')
    # print(options[i]) Checking options

# print(" --- %s seconds" % (time.time() - start_time))
