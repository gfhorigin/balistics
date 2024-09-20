import math

# ИЗ ТОГО ЧТО МЫ НАСЧИТАЛИ ПРИ  угле = 0
# t = 0.42 s
# Sy = 0.9 m

# dS1x = 1.37 m
# v1 = 3.19 m/s

# dS2x =  1,8075 m
# v2 = 4.2175 m/s

# dS3x =  2,245 m
# v3 = 5.2383 m/s

def time(Sy,):
    t = ((2*Sy) / 9.8) **0.5
    return t

def Speed(Sy,Sx,): #при альфа = 0
    return Sx / time(Sy)

def speedY(Sy,):
    SpeedY = (Sy*9.8)**0.5
    return SpeedY

print(Speed(0.9, 2.245))
