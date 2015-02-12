#system parameters
k = 20.0
m = 3.0
x0 = 4.0
dt = 0.001

#initial conditions
x = 2.0
v = 0.0
a = 0.0
t = 0.0
U = 0.0

for i in range (10000):
	f = -k*(x - x0)
	a = f/m
	v = v + a*dt
	x = x + v*dt
	t = i*dt
	U = 0.5*k*v**2

	print t, U
