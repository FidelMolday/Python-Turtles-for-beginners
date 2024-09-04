import turtle as t
t.tracer(10,1)

N = 10
angle = 1

turtles = []
for position in range(N):
  look_at = 360/N*position
  new = t.Turtle()
  new.setheading(look_at)
  turtles.append(new)

for radius in range(360):
  for my in turtles:
    my.circle(radius, angle)


t.update()
