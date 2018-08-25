import math

class InvertedPendulum(object):

    def __init__(self, dt, *iniCond):

        # in a future work, maybe we can inicialize the problem with randon values
        self.m = 1.1   # car mass + pendulum mass
        self.g = 9.8   # gravity aceleration
        self.l = 0.5   # pendulum size
        self.mb = 0.1  # pendulum mass

        self.thdd = 0          # inicializing the variable of angular aceleration of the pendulum
        self.thd = iniCond[0]  # inicializing the variable of angular velocity of the pendulum
        self.th = iniCond[1]   # inicializing the variable of angular position of the pendulum

        self.xdd = 0           # inicializing the variable of linear aceleration of the car
        self.xd = iniCond[2]   # inicializing the variable of linear velocity of the car
        self.x = iniCond[3]    # inicializing the variable of linear position of the car

        self.dt = dt   # integration period

    def modeldd(self, f):

        self.thdd = ((self.m * self.g * math.sin(self.th)) - math.cos(self.th) * (f + self.mb * self.l * math.pow(self.thd, 2) * math.sin(self.th))) / ((4 / 3) * self.m * self.l - self.mb * self.l * math.pow(math.cos(self.th), 2))
        self.xdd = (f + self.mb * self.l * (math.pow(self.x, 2) * math.sin(self.x) - self.thdd * math.cos(self.x))) / self.m

    def integrate(self, f):


        self.modeldd(f) # call the func to calculate the double dot states (Angular and linear acelerations)

        self.thd = self.thd + self.dt * self.thdd # calc the angular velocity of the pendulum by integrating the angular velocity
        self.th = self.th + self.dt * self.thd    # calc the angular position of the pendulum by integrating the angular velocity

        self.xd = self.xd + self.dt * self.xdd    # calc the linear velocity of the car by integrating the linear velocity
        self.x = self.x + self.dt * self.xd       # calc the linear position of the car by integrating the linear velocity

        return ([self.th, self.x])

    def resetsys(self):
        self.thdd = 0  # reset the variable of angular aceleration of the pendulum
        self.thd = 0   # reset the variable of angular velocity of the pendulum
        self.th = 0    # reset the variable of angular position of the pendulum

        self.xdd = 0   # reset the variable of linear aceleration of the car
        self.xd = 0    # reset the variable of linear velocity of the car
        self.x = 0     # reset the variable of linear position of the car