import math

#
# def time(Sy,):
#     t = ((2*Sy) / 9.8) **0.5
#     return t

# def Speed(Sy,Sx,): #при альфа = 0
#     return Sx / time(Sy)

# ИЗ ТОГО ЧТО МЫ НАСЧИТАЛИ ПРИ  угле = 0
# t = 0.42 s
# Sy = 0.9 m

# dS1x = 1.37 m
# v1 = 3.19 m/s

# dS2x =  1,8075 m
# v2 = 4.2175 m/s

# dS3x =  2,245 m
# v3 = 5.2383 m/s

class Balistic:
    def __init__(self, V0, h, alpha, targetH):
        self.V0 = V0
        self.h = h
        self.targetH= targetH
        self.alpha = alpha

    def SpeedX(self, ):
        self.Vx = round(self.V0 * math.cos(self.alpha),2)

    def SpeedY(self, ):
        self.Vy = round( self.V0 *  math.sin(self.alpha), 2)

    def Time(self):
         self.t =round( (self.Vy  + (self.Vy**2 + 4*4.9*self.h)**0.5) / 9.8, 2)

    def Lenght(self):
        self.l = round(self.Vx * self.t, 2)

    def Target(self):
        t = round((self.Vy + (self.Vy ** 2 + 4 * 4.9 * (self.h-self.targetH))**0.5) / 9.8, 2)
        self.targetLenght = round(self.Vx * t, 2)

    def __str__(self):
        print("скорсоть по х:", self.Vx)

        print("скорсоть по y:", self.Vy)

        print("время полета:",self.t)

        print("длина полета по х:", self.l)

        print("расстояние по х до цели:", self.targetLenght)
        return str()



bal = Balistic(4.21, round(( 0.9+0.85 ) / 2,2),0,0.2)#5.23,round((0.8+0.75)/2,2),0, 0.2
bal.SpeedX()#4.21, round(( 0.9+0.85 ) / 2,2),0,0.2
bal.SpeedY()
bal.Time()
bal.Lenght()
bal.Target()
print(bal)
