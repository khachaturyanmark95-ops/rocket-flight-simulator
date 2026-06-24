import matplotlib.pyplot as plt
#Rocket parameters 
mass = 1000        #kg
thrust = 15000     #Newton
fuel = 100         #percent
gravity = 9.8      #m/s2

#lists
time = 0
height = 0
speed = 0
time_list = []
height_list = []
speed_list = []


while fuel > 0 and time < 30:
    acceleration = (thrust / mass) - gravity
    speed = speed + acceleration
    height = height + speed
    fuel = fuel - 2
    time =  time + 1
    time_list.append(time)
    (height_list.append(height))
    speed_list.append(speed)

#Graph
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time_list, height_list, color='blue')
plt.title("Rocket Flight Simulator")
plt.ylabel("Height (meters)")
plt.subplot(2, 1, 2)
plt.plot(time_list, speed_list, color='red')
plt.ylabel("Speed (m/s)")
plt.xlabel("Time (seconds)")

plt.tight_layout()
plt.show()