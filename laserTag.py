import serial
ser = serial.Serial('[your USB port]', 9600)
fullreserve = 900 #number of bullets you get per life
reserve = 900
fullclip = 15 #how many bullets are in a clip
clip = 15
fullhealth = 10 #total shots it takes to kill
health = 10

def updateStats():
    print('RESERVE: ')
    print(reserve)
    print('\n')
    print('\n')
    print('CLIP: ')
    print(clip)
    print('\n')
    print('\n')
    print('HEALTH: ')
    print(health)
    print('\n')
    print('\n')
    print('\n')
    print('\n')

def died():
    print('YOU DIED!')
    print('\n')

    global health
    global fullhealth
    global reserve
    global fullreserve
    global clip
    global fullclip
    health = fullhealth
    reserve = fullreserve
    clip = fullclip

def parseMsg(txt):
    global health
    global fullhealth
    global reserve
    global fullreserve
    global clip
    global fullclip
    if(msg.startswith('RELOAD')):
        reserve = reserve - clip
        clip = fullclip
        updateStats()
    elif(msg.startswith('CLIP')):
        clip = clip - 1
        updateStats()
    elif(msg.startswith('HEALTH')):
        health = health - 1
        updateStats()
    elif(msg.startswith('DIED')):
        died()
while(True):
    global msg
    msg = ser.readline()
    parseMsg(msg)
