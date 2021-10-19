initial_pos=float(input("enter the object's initial position:"))
initial_vel=float(input("enter the object's initial velocity:"))
acceleration=float(input("enter the acceleration:"))
time=float(input("enter the time:"))

final_pos=initial_pos+(initial_vel*time)+(acceleration*(time*time)/2)
print("final position is: ",final_pos)

     


