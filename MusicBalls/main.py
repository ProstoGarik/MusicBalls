import pygame
import pymunk
import pymunk.pygame_util


WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = (0, 980)

floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
floor_body.position = (400, 580)
floor_shape = pymunk.Poly.create_box(floor_body, size=(800, 20))
floor_shape.friction = 0.5
floor_shape.elasticity = 0.5
space.add(floor_body, floor_shape)

mass = 1
radius = 40
moment = pymunk.moment_for_box(mass, (60, 60))
circle_body = pymunk.Body(mass, moment)
circle_body.position = (400, 300) 

circle_shape = pymunk.Circle(circle_body, radius)
circle_shape.friction = 0.5
circle_shape.elasticity = 0.8 
space.add(circle_body, circle_shape)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    space.step(1 / 60.0)

    screen.fill((30, 30, 30))
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()