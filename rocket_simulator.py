import matplotlib.pyplot as plt 

rocket_name = "Falcon 9"
mass = 549000           #kg 
thrust = 7607000        #Newton
fuel = 100              #percent
gravity = 9.8           #m/s2


time_list = []
height_list = []
speed_list = []
acceleration_list = []

time = 0
height = 0
speed = 0

print("launching " + rocket_name + "...")
print("Mass: " + str(mass) + " kg")
print("Thrust: " + str(thrust) + " N")
print("------------------------------")

while fuel > 0 and time < 60:
    acceleration = (thrust / mass) - gravity
    speed = speed + acceleration
    height = height + speed
    fuel = fuel - 1.67
    mass = mass - 9150
    time = time + 1
    time_list.append(time)
    height_list.append(height / 1000)
    acceleration_list.append(acceleration)
    speed_list.append(speed)

print("Max height: " + str(round(max(height_list))) + " km")
print("Max speed: " + str(round(max(speed_list))) + " m/s")
print("Max  acceleration: " + str(round(max(acceleration_list))) + " m/s2")

plt.figure(figsize =(10, 8))

plt.subplot(3, 1, 1)
plt.plot(time_list, height_list, color='blue')
plt.title("Falcon 9 Flight Simulation")
plt.ylabel("Height (km)")

plt.subplot(3, 1, 2)
plt.plot(time_list, speed_list, color ='red')
plt.ylabel("Speed (m/s)")

plt.subplot(3, 1, 3)
plt.plot(time_list, acceleration_list, color ='green')
plt.ylabel("Acceleration (m/s2)")
plt.xlabel("Time (seconds)")

plt.tight_layout()
plt.savefig("rocket_graph.png")
plt.show()
