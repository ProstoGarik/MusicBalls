import pygame
import pymunk
import pymunk.pygame_util
import time

BALL_COLLISION_TYPE = 1
PLATFORM_COLLISION_TYPE = 2
SOUND_OUTPUT_DEVICE = "YOUR DEVICE" # It didn't work for me without specifying the output device

WIDTH, HEIGHT = 800, 600

pygame.mixer.init(devicename=SOUND_OUTPUT_DEVICE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

draw_options = pymunk.pygame_util.DrawOptions(screen)

# World setup
space = pymunk.Space()
space.gravity = (0, 980)

# Bottom floor
floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
floor_body.position = (400, 580)
floor_shape = pymunk.Poly.create_box(floor_body, size=(800, 20))
floor_shape.friction = 0.5
floor_shape.elasticity = 0.5
floor_shape.collision_type = PLATFORM_COLLISION_TYPE
space.add(floor_body, floor_shape)
sound = pygame.mixer.Sound('noteC.wav')

# Ball
mass = 1
radius = 40
moment = pymunk.moment_for_box(mass, (60, 60))
circle_body = pymunk.Body(mass, moment)
circle_body.position = (400, 300) 
circle_shape = pymunk.Circle(circle_body, radius)
circle_shape.friction = 0.5
circle_shape.elasticity = 0.8 
circle_shape.collision_type = BALL_COLLISION_TYPE
space.add(circle_body, circle_shape)

def ball_floor_collide_begin(arbiter, space, data):
    print("Touched")
    play_note()
    circle_body.apply_impulse_at_local_point([0,500])
    return

def play_note():
    # Загрузите звук заранее, чтобы не грузить каждый раз
    sound.play()

handler = space.on_collision(BALL_COLLISION_TYPE, PLATFORM_COLLISION_TYPE, ball_floor_collide_begin)

# Simulation loop
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