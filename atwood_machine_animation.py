from vpython import *


rope_length = 20.
anchor_point = vector(0., 1.25*rope_length, 0.)
standard_gravity = 9.80665

mass_one = 12.0
mass_two = 5.0
total_mass = mass_one + mass_two

pulley_radius = 5.0

origin_one = anchor_point - vector(pulley_radius, 0., 0.)
initial_position_one = origin_one - vector(0., 1.25*rope_length, 0.)
origin_two = anchor_point + vector(pulley_radius, 0., 0.)
initial_position_two = origin_two - vector(0., 0.75*rope_length, 0.)


pulley_thickness = 0.2
pulley = cylinder(pos=anchor_point,
                  axis=vector(0., 0., 1.),
                  radius=pulley_radius,
                  color=color.gray(0.9))

weight_length = pulley_radius
weight_height = weight_length/sqrt(2)
weight_width = 0.2*weight_length


weight_one = box(pos=initial_position_one,
                 axis=vector(1., 0., 0.),
                 length=weight_length, height=weight_height, width=weight_width,
                 texture=textures.wood)


weight_two = box(pos=initial_position_two,
                 axis=vector(1., 0., 0.),
                 length=weight_length, height=weight_height, width=weight_width,
                 texture=textures.wood)


length_one = abs(origin_one.y - initial_position_one.y)
rope_one = cylinder(pos=origin_one,
                    axis=vector(0., -length_one, 0.),
                    radius=0.1,
                    texture=textures.rough)

length_two = abs(origin_two.y - initial_position_two.y)
rope_two = cylinder(pos=origin_two,
                    axis=vector(0., -length_two, 0.),
                    radius=0.1,
                    texture=textures.rough)

position_one = initial_position_one
acceleration_one = vector(0., (mass_one - mass_two) * standard_gravity / total_mass, 0.)
acceleration_two = -acceleration_one
position_two = initial_position_two
number_of_steps = 1000
time_step = 0.1
while True:
    rate(200)

    position_one = position_one + 0.5 * acceleration_one * time_step**2
    position_two = position_two + 0.5 * acceleration_two * time_step**2

    length_one = abs(origin_one.y - position_one.y)
    length_two = abs(origin_two.y - position_two.y)

    weight_one.pos = position_one
    weight_two.pos = position_two
    rope_one.axis = vector(0., -length_one, 0.)
    rope_two.axis = vector(0., -length_two, 0.)

    if (position_one.y >= origin_one.y - pulley_radius - 0.5*weight_height)\
            or (position_two.y >= origin_two.y - pulley_radius - 0.5*weight_height):
        break
