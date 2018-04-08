# Joseph Rice
#2/22/2018
# PY 5 planetay motion
from __future__ import division
from visual import *
from math import * 


# This function will give me the starting value to put earth in orbit so it needs to be on top. 
def orbit_start_speed(mass1,relative_position_vector):
    """mass of center object force"""
    G = 6.67e-11 # N*m^2/kg^2
    start_speed = sqrt((G*mass1)/mag(relative_position_vector))
    Unit_vector_velocity = vector(0,1,0)
    Start_velocity = Unit_vector_velocity*1.1*start_speed
    return Start_velocity


G = 6.67e-11 # N*m^2/kg^2

Sun = sphere(pos=vector(0,0,0),radius=5e10,color=vector(0.9,.5,.3),material=materials.emissive)

Sun.mass = 2e30 #kg



Earth = sphere(pos=vector(1.5e11,0,0),radius=7e9,color=color.yellow,\
               material=materials.earth,make_trail=True)

Earth.mass = 6e24 # kg


#relative position vector
relative_Earth_pos = Earth.pos - Sun.pos # m

# Unit Vector for earth
rhat = vector(1,0,0)


# Earth's momentum
Earth.momentum_inital = Earth.mass*orbit_start_speed(Sun.mass,relative_Earth_pos)# kg m/s


""" simplify the time for the user"""
# converts months to seconds 
def month_to_second(number_month):
    """ Months to seconds  """
    value=number_month*30*24*60*60
    return value

# Turns day to second
def day_to_second(day):
    seconds = day*24*60*60
    return seconds

# converts year to seconds
def year_to_second(number_year):
    "year returns seconds" 
    value = number_year*365*24*60*60
    return value

def Force_on_object(mass_1,mass_2,relative_Earth_pos,rhat):
    """ 2 mass and relative_pos vector are inputs of this function """
    G = 6.67e-11 # N*m^2/kg^2
    Fg = (-(G*mass_1*mass_2)/(mag(relative_Earth_pos))**2)*rhat# N
    return Fg

# Force of gravity from function inputs are Earth's mass and sun's mass 
Force_gravity = Force_on_object(Earth.mass,Sun.mass,relative_Earth_pos,rhat)



## Force scale factor 
force_scale = .000000000002

## momentum scale factor
momentum_scale = .0000000000000000003

# visual Momentum_vector
Momentum_Vector = arrow(pos=Earth.pos,axis=momentum_scale*Earth.momentum_inital,color=color.green)

# visual Force_vector 
Force_vector = arrow(pos=Earth.pos,axis=force_scale*Force_gravity,color=color.red)

## incriments to one day 
Delta_t = day_to_second(1)#s

print("\n Im trying to make my code easy to read please bear with me")
print("\n")
print("staring force of gravity ",Force_gravity, 'N')
print('mass of sun',Sun.mass, "kg")
print("mass of Earth: ",Earth.mass, 'kg')
print("starting orbit speed of the earth: ", orbit_start_speed(Sun.mass,relative_Earth_pos), 'm/s')
print('one day is: ~ ', day_to_second(1),' seconds')
print("\n")
print("Momentum of the earth starting: ")
print(Earth.momentum_inital,' kg*m/s')

#inital time 
t =0
#

# stops after one year
while t < year_to_second(50):
    
    rate(100)
    
    Relative = Earth.pos - Sun.pos
    
    rhat = Relative/mag(Relative)
    
    Fnet = (-(G*Earth.mass*Sun.mass)/(mag(Relative))**2)*rhat

    Earth.momentum_inital = Earth.momentum_inital + Fnet*Delta_t
    
    Earth.pos = Earth.pos + (Earth.momentum_inital/Earth.mass)*Delta_t
    
    Momentum_Vector.pos = Earth.pos
    
    Force_vector.pos = Earth.pos
    
    Momentum_Vector.axis = Earth.momentum_inital*momentum_scale
    
    Force_vector.axis = Fnet*force_scale
##    Sun.pos = Sun.pos + vector(3E8,3E8,0)
    t += Delta_t
    
print("\n")
print("____ After one year____")
print("\n")
print(" force of gravity ",Force_gravity, 'N')
print("orbit speed of the earth: ", orbit_start_speed(Sun.mass,relative_Earth_pos), 'm/s')

    

    






























