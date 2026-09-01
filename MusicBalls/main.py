import pygame
import pymunk
import pymunk.pygame_util

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

# Note names setup
notes = {
    'C': pygame.mixer.Sound('noteC.mp3'),
    'D': pygame.mixer.Sound('noteD.mp3'),
    'B': pygame.mixer.Sound('noteB.mp3')
}

class NotePlatform:
    def __init__(self, pos, size, rot, note_name):
        self.note_name = note_name
        self.sound = notes[note_name]
        
        # Creating box with collision
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos
        self.body.angle = rot
        self.shape = pymunk.Poly.create_box(self.body, size=size)
        self.shape.friction = 0.5
        self.shape.elasticity = 1
        self.shape.collision_type = PLATFORM_COLLISION_TYPE
        self.shape.data = self
        space.add(self.body, self.shape)

    def play_note(self):
        self.sound.play()

# Left floor
platform1 = NotePlatform((100, 490), (500, 20), 0.5236 ,"B")

# Center floor
platform2 = NotePlatform((400, 580), (500, 20), 0, "C")

# Right floor
platform3 = NotePlatform((700, 490), (500, 20), -0.5236, "D")

# Ball
mass = 1
radius = 40
moment = pymunk.moment_for_box(mass, (60, 60))
circle_body = pymunk.Body(mass, moment)
circle_body.position = (100, 300) 
circle_shape = pymunk.Circle(circle_body, radius)
circle_shape.friction = 0.5
circle_shape.elasticity = 1
circle_shape.collision_type = BALL_COLLISION_TYPE
space.add(circle_body, circle_shape)


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

