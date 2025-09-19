import pygame

L, H = 800, 500
max_iter = 100

palette = [
    (66, 30, 15), (25, 7, 26), (9, 1, 47), (4, 4, 73),
    (0, 7, 100), (12, 44, 138), (24, 82, 177), (57, 125, 209),
    (134, 181, 229), (211, 236, 248), (241, 233, 191),
    (248, 201, 95), (255, 170, 0), (204, 128, 0),
    (153, 87, 0), (106, 52, 3)
]

re_start, re_end = -2.5, 1.0
re_range = re_end - re_start
im_range = re_range * (H / L)
im_start = -im_range / 2
im_end = im_range / 2

def mandelbrot_escape(c):
    z = complex(0, 0)
    for n in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) > 4.0:
            return n
    return max_iter

pygame.init()
screen = pygame.display.set_mode((L, H))
surface = pygame.Surface((L, H))

px = pygame.PixelArray(surface)
for x in range(L):
    re = re_start + (x / (L - 1)) * (re_end - re_start)
    for y in range(H):
        im = im_start + (y / (H - 1)) * (im_end - im_start)
        m = mandelbrot_escape(complex(re, im))
        color = (0, 0, 0) if m == max_iter else palette[m % len(palette)]
        px[x, y] = surface.map_rgb(color)
del px

screen.blit(surface, (0, 0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
