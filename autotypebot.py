import requests
import threading
import time

last_hunt_time = time.time()  
last_saw_time = time.time()  

total_hunt = 0
total_saw = 0

header = {
    'authorization': "YOUR AUTHENTICATION"
}

# Definisi payload di luar fungsi
payload_data1 = {
    'content': 'rpg hunt h'
}

# Definisi payload2
payload_data2 = {
    'content': 'rpg dynamite'
}

def payload1():
    global last_hunt_time, total_hunt
    while True:
        current_time = time.time()
        if current_time - last_hunt_time >= 61:
            r1 = requests.post('YOUR REQUEST MESSAGE LINK', data=payload_data1, headers=header)
            print('hunt', total_hunt + 1)
            last_hunt_time = current_time
            total_hunt += 1
        time.sleep(1)

def payload2():
    global last_saw_time, total_saw
    while True:
        current_time = time.time()
        if current_time - last_saw_time >= 301:      
            r2 = requests.post('YOUR REQUEST MESSAGE LINK', data=payload_data2, headers=header)
            print('chainsaw', total_saw + 1)
            last_saw_time = current_time
            total_saw += 1
        time.sleep(1)

t1 = threading.Thread(target=payload1)
t2 = threading.Thread(target=payload2)
t1.start()
t2.start()

