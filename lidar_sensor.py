"""lidar_sensor controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

motor1 = robot.getDevice('lm1') 
motor3 = robot.getDevice('lm3') 
motor2 = robot.getDevice('lm2')
motor4 = robot.getDevice('lm4')

#lidar

lidar = robot.getDevice('lidar')
lidar.enable(timestep)
lidar.enablePointCloud() 

 

L_motor = [motor1,motor3]
R_motor = [motor2,motor4]

keyboard = robot.getKeyboard()
keyboard.enable(timestep)


for Lm in L_motor:
    
    Lm.setPosition(float('inf'))
    Lm.setVelocity(0.0)


for Rm in R_motor:
    
     Rm.setPosition(float('inf'))
     Rm.setVelocity(0.0)




# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:


    ranges = lidar.getRangeImage()
    key = keyboard.getKey()
    
    
    for Lm in L_motor:
        Lm.setVelocity(0.0)


    for Rm in R_motor:
        Rm.setVelocity(0.0)
        
    print(ranges[0:5])
    
    if key == 315:
           
        for Lm in L_motor:
            Lm.setVelocity(3.0)
            
        for Rm in R_motor:
            Rm.setVelocity(3.0)
            
    elif key == 317:
                
        for Lm in L_motor:
            Lm.setVelocity(-1*1.0)
            
        for Rm in R_motor:
            Rm.setVelocity(-1*1.0)
            
    elif key == 316:
            
        for Lm in L_motor:
            Lm.setVelocity(2.0)
            
        for Rm in R_motor:
            Rm.setVelocity(-1*3.0)
        
    elif key == 314:
            
        for Lm in L_motor:
            Lm.setVelocity(-1*3.0)
            
        for Rm in R_motor:
            Rm.setVelocity(2.0)


        
   

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)


# Enter here exit cleanup code.
