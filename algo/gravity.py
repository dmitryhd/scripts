#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
import math
from random import randint

GRAV_CONST = 5
# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]

size = [1100,700]
center = complex(550, 350)
v_max = 50


def get_module(v):
    return math.sqrt(v.real**2 + v.imag**2)

def normalize_vector(v):
    norm = max(abs(v.real), abs(v.imag))
    if norm == 0:
        norm = 1
    v /= norm
    return v

class Particle:
    RADIUS = 5
    def __init__(self, index, x, y, m, v, screen, col=green):
        self.index = index
        self.x = x
        self.y = y
        self.m = m
        self.v = v
        self.screen = screen
        self.col = col

    def __make_sure_not_leaving_field(self, new_x, new_y):
        if new_x < 0:
            new_x = 0
            self.v = complex(-self.v.real, self.v.imag)
        if new_x > size[0]:
            new_x = size[0]
            self.v = complex(-self.v.real, self.v.imag)
        if new_y > size[1]:
            new_y = size[1]
            self.v = complex(self.v.real, -self.v.imag)
        if new_y < 0:
            new_y = 0
            self.v = complex(self.v.real, -self.v.imag)
        if self.index == 0:
            print('move part', self.index, self.x, self.y, self.v)
        return (new_x, new_y)

    def __normalize_speed(self):
        if self.v.real > v_max:
            self.v = complex(v_max, self.v.imag)
        if self.v.imag > v_max:
            self.v = complex(self.v.real, v_max)

    def move(self):
        self.__normalize_speed()
        new_x = self.x + self.v.real
        new_y = self.y + self.v.imag
        self.x, self.y = self.__make_sure_not_leaving_field(new_x, new_y)

    def draw(self):
        pygame.draw.circle(self.screen, self.col, (int(self.x), int(self.y)), int(3 + math.sqrt(self.m)))

    def get_force(self, other_particle):
        vect1 = complex(self.x, self.y)
        vect2 = complex(other_particle.x, other_particle.y)
        vect_res = vect2 - vect1
        force = (GRAV_CONST * (self.m * other_particle.m) / (get_module(vect_res)**2)) * normalize_vector(vect_res)
        return force
# Initialize the game engine
pygame.init()


pi = 3.141592653

# Set the height and width of the screen
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Gravity")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

Particles = []
Particles.append(Particle(100, center.real, center.imag, 200, complex(0, 0), screen, blue))
for i in range(50):
    x = center.real + randint(-200,200)
    y = center.imag + randint(-200,200)
    m = randint(1,3)
    #particle_vector = complex(x, y) - center
    #v = complex(-particle_vector.imag, particle_vector.real)
    #norm = max(abs(v.real), abs(v.imag))
    #v /= norm
    #v *= randint(1,2)
    v = complex(0, 0)
    p = Particle(i, x, y, m, v, screen)
    Particles.append(p)


while done == False:
    clock.tick(7)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    screen.fill(black)

    for particle in Particles:
        particle.move()
        particle.draw()
        for particle2 in Particles:
            if particle2.x == particle.x and particle2.y == particle.y:
                continue
            force = particle.get_force(particle2)
            a = force / particle.m
            particle.v += a
    pygame.display.flip()
# Be IDLE friendly
pygame.quit()
