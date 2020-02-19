import pgzrun

alien = Actor('alien_pic')
alien.topright = 20, 70
WIDTH = 1200
HEIGHT = alien.height + 200


def draw():
    screen.clear()
    alien.draw()


def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    sounds.eep.play()
    alien.image = 'alien_hurt'
    clock.schedule_unique(set_alien_normal, .4)


def set_alien_normal():
    alien.image = 'alien_pic'


pgzrun.go()
