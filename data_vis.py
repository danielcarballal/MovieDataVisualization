import matplotlib.pyplot as plt
import json
from numpy import sin
from numpy import cos, pi

circles = {}
labels = {}

HEIGHT_X = 500
HEIGHT_Y = 500
SPACE_BETWEEN_DEPTH = 70
CIRCLE_DIAM = 20

CENTER_X = HEIGHT_X / 2
CENTER_Y = HEIGHT_Y / 2

MAX_DEPTH = 7
MAX_CHILD = 2

INITIAL_NODES = 5

# Recurses on two actors which have not been recursed on yet
def recurse_on_movie(movie_name, depth, angle):
	if MAX_DEPTH == depth:
		return -1 
	if movie_name not in films:
		return -1
	info = films[movie_name]
	dist_to_center = (SPACE_BETWEEN_DEPTH * depth)
	new_x = CENTER_X + cos(angle) * dist_to_center
	new_y = CENTER_Y + sin(angle) * dist_to_center
	c = plt.Circle((new_x, new_y), CIRCLE_DIAM, color='b')
	plt.text(new_x - CIRCLE_DIAM, new_y, movie_name, fontsize=6)
	if info["year"] != 0:
		plt.text(new_x - CIRCLE_DIAM/2, new_y + CIRCLE_DIAM/2, str(info["year"]), fontsize=6)
	if info["box_office"] != 0:
		plt.text(new_x - CIRCLE_DIAM * 3/4, new_y - CIRCLE_DIAM/2, str(info["box_office"]), fontsize=6)
	print 'Created ' + movie_name + ' at ' + str(new_x) + ' ' + str(new_y)
	circles[movie_name] = c
	child = 0

	for actor in info["actors"]:
		if actor not in circles:
			if child <= 1:
				recurse_val = recurse_on_actor(actor, depth + 1, angle + (child * 2 - 1) * (2 * pi / INITIAL_NODES) * pi/( 2**(depth + 1)) )
				if recurse_val != -1:
					child += 1
	return [new_x, new_y]

# Recurses on two actors 
def recurse_on_actor(actor_name, depth, angle):
	if MAX_DEPTH == depth:
		return -1
	if actor_name not in actors:
		return -1
	info = actors[actor_name]
	dist_to_center = (SPACE_BETWEEN_DEPTH * depth)
	new_x = CENTER_X + cos(angle) * dist_to_center
	new_y = CENTER_Y + sin(angle) * dist_to_center
	c = plt.Circle((new_x, new_y), CIRCLE_DIAM, color='r')
	plt.text(new_x - CIRCLE_DIAM, new_y, actor_name, fontsize=6)
	if info["age"] != 0:
		plt.text(new_x - CIRCLE_DIAM/2, new_y + CIRCLE_DIAM/2, str(info["age"]), fontsize=6)
	if info["total_gross"] != 0:
		plt.text(new_x - CIRCLE_DIAM * 3/4, new_y - CIRCLE_DIAM/2, str(info["total_gross"]), fontsize=6)
	child = 0
	print 'Created ' + actor_name + ' at ' + str(new_x) + ' ' + str(new_y)
	circles[actor_name] = c
	for movie in info["movies"]:
		if movie not in circles:
			if child <= 1:
				recurse_val = recurse_on_movie(movie, depth + 1, angle + (child * 2 - 1) * (2 * pi / INITIAL_NODES) *  pi/( 2**(depth + 2)) )
				if recurse_val != -1:
					child += 1
	return [new_x, new_y]

def generate_circles(first_name):

	if first_name in actors:
		c = plt.Circle((CENTER_X, CENTER_Y), CIRCLE_DIAM, color='r')
		plt.text(CENTER_X - CIRCLE_DIAM, CENTER_Y, first_name, fontsize=8)
		info = actors[first_name]
		circles[first_name] = c
	 	angle = 0
		for movie in info["movies"]:
			if angle < 2 * pi:
				recurse_on_movie(movie, 1, angle)
			angle += 2 * pi / INITIAL_NODES
	elif first_name in movies:
		c = plt.Circle((CENTER_X, CENTER_Y), CIRCLE_DIAM, color='b')
		plt.text(CENTER_X - CIRCLE_DIAM, CENTER_Y, first_name, fontsize=8)
		info = films[first_name]
		circles[first_name] = c
	 	angle = 0
		for actor in info["actors"]:
			if angle < 2 * pi:
				recurse_on_movie(actor, 1, angle)
			angle += 2 * pi / INITIAL_NODES
	else:
		print "Starting node not found!"

file = open("data.json")
j = json.load(file)
actors = j[0]
films = j[1]

fig, ax = plt.subplots()

generate_circles(NAME)
ax.set_xlim((0, HEIGHT_X))
ax.set_ylim((0, HEIGHT_Y))
for name in circles:
	ax.add_artist(circles[name])

plt.axis('off')

fig.savefig('plotcircles.png')