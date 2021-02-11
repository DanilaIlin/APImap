import pygame
import requests

map_file = 'map.jpg'
mapl = ['map', 'sat', 'sat,skl']

def gm(ln, lt, m, ll):
    global map_file
    global mapl
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={ln},{lt}8&spn={m},{str(float(m)/2)}&size=500,450&l={mapl[ll]}"
    response = requests.get(map_request)
    if str(response) != '<Response [404]>':
        print('OK')
        with open(map_file, 'wb') as file:
            file.write(response.content)
    else:
        print('Error')


pygame.init()
size = width, height = 500, 450
pygame.display.set_caption('map')
screen = pygame.display.set_mode(size)
run = True
lnn = input('Введите долготу')
ltt = input('Введите широту')
mm = input('Введите маштаб 0-17')
lll = 0
gm(lnn, ltt, mm, lll)
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while run:
    for el in pygame.event.get():
        if el.type == pygame.QUIT:
            run = False
        if el.type == pygame.KEYDOWN:
            if el.key == pygame.K_UP and (float(ltt) + float(mm) < 90):
                ltt = str(float(ltt) + 0.5 * float(mm))
                gm(lnn, ltt, mm, lll)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if el.key == pygame.K_DOWN and (float(ltt) - float(mm) > -90):
                ltt = str(float(ltt) - 0.5 * float(mm))
                gm(lnn, ltt, mm, lll)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if el.key == pygame.K_RIGHT and (float(lnn) + float(mm) < 180):
                lnn = str(float(lnn) + 0.5 * float(mm))
                gm(lnn, ltt, mm, lll)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if el.key == pygame.K_LEFT and (float(lnn) - float(mm) > -180):
                lnn = str(float(lnn) - 0.5 * float(mm))
                gm(lnn, ltt, mm, lll)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if el.key == pygame.K_PAGEUP and (float(mm) < 175):
                mm = str(float(mm) + 5)
                gm(lnn, ltt, mm, lll)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if el.key == pygame.K_PAGEDOWN and (float(mm) > 5):
                mm = str(float(mm) - 5)
                gm(lnn, ltt, mm, lll)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if el.key == pygame.K_k:
                lll += 1
                if lll == 3:
                    lll = 0
                gm(lnn, ltt, mm, lll)
                screen.blit(pygame.image.load(map_file), (0, 0))

    pygame.display.flip()


pygame.quit()
