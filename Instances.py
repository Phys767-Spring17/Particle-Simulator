# import the Particle class from the particle module
import particle as p

# create an empty list to hold observed particle data
obs = []

# append the first particle; by the way, append means to add
obs.append(p.Particle())

# assign its position
obs[0].r = {'x': 100.0, 'y': 38.0, 'z': -42.0}

# append the second particle
obs.append(p.Particle())

# assign the position of the second particle
obs[1].r = {'x': 0.01, 'y': 99.0, 'z': 32.0}

# print the positions of each particle
print(obs[0].r)
print(obs[1].r)

