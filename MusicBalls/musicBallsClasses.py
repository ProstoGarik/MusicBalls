import pymunk
import pygame


SOUND_OUTPUT_DEVICE = "Наушники гарнитуры (G435 Wireless Gaming Headset)" # It didn't work for me without specifying the output device (use getDeviceList.py)
BALL_COLLISION_TYPE = 1
PLATFORM_COLLISION_TYPE = 2

pygame.mixer.init(devicename=SOUND_OUTPUT_DEVICE)

# Note names setup
notes = {
    'C': pygame.mixer.Sound('note1.mp3'),
    'D': pygame.mixer.Sound('note2.mp3'),
    'B': pygame.mixer.Sound('note3.mp3')
}

class NotePlatform:
    def __init__(self, pos, size, rot, note_name, space):
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

class Ball:
    def __init__(self, pos, radius, mass, space):
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.circle_body = pymunk.Body(mass, moment)
        self.circle_body.position = pos
        circle_shape = pymunk.Circle(self.circle_body, radius)
        circle_shape.friction = 0.5
        circle_shape.elasticity = 1
        circle_shape.collision_type = BALL_COLLISION_TYPE
        space.add(self.circle_body, circle_shape)

    def push(self, x, y):
        self.circle_body.apply_impulse_at_local_point([x,y])

