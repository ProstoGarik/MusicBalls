import pygame
import pymunk
import pymunk.pygame_util
from musicBallsClasses import NotePlatform, Ball, BALL_COLLISION_TYPE, PLATFORM_COLLISION_TYPE

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

draw_options = pymunk.pygame_util.DrawOptions(screen)

# World setup
space = pymunk.Space()
space.gravity = (0, 0)

# Left floor
platform1 = NotePlatform((400, 520), (500, 20), 0 ,"B", space)
platform2 = NotePlatform((400, 100), (500, 20), 0 ,"C", space)


# Ball
ball = Ball([400,320], 30, 1, space)
ball.push(0, 150)

# Ball
ball2 = Ball([300,300], 30, 1, space)
ball2.push(0, 150)

# Ball
ball2 = Ball([500,340], 30, 1, space)
ball2.push(0, 150)


# Ball and platform collision handler
def ball_floor_collide_begin(arbiter, space, data):
    platform_shape = arbiter.shapes[1]
    platform_data = platform_shape.data
    platform_data.play_note()
    print("Touched")
    return

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