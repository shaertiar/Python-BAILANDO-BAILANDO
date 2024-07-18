import pygame as pg
import gif_pygame as gifpg

# Иниацилизация
pg.init()

# Переменные 
is_game = True
RES = WW, WH = 360, 260
clock = pg.time.Clock()
FPS = 10
is_pause  = False
frames = 0

# Звуки
pg.mixer.music.load('src/music.mp3')
pg.mixer.music.play(-1)

# Создание окна
window = pg.display.set_mode(RES)
pg.display.set_caption('Dance')
pg.display.set_icon(pg.image.load('src/ico.png'))

# Классы
gif = gifpg.load('src/konata-dance.gif')

# Функция отображения паузы
def blit_pause():
    dimming_filter = pg.Surface(RES)
    dimming_filter.fill((0, 0, 0))
    dimming_filter.set_alpha(200)
    window.blit(dimming_filter, (0, 0))
    
    pg.draw.rect(window, (255, 255, 255), (WW/2 - 10, WH / 2 - 25, 10, 50))
    pg.draw.rect(window, (255, 255, 255), (WW/2 + 10, WH / 2 - 25, 10, 50))

# Игровой цикл
while is_game:
    # Отображение gif
    window.fill((255, 255, 255))
    gif.render(window, (0, 0))
    
    # Обработка событий
    for event in pg.event.get():
        # Обработка выхода
        if event.type == pg.QUIT:
            is_game = False
            
        # Обработка нажатия клавиши
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                is_pause = not is_pause
                
                if is_pause:
                    pg.mixer.music.pause()
                    gif.pause()
                    
                else:
                    pg.mixer.music.unpause()
                    gif.unpause()
                    
    # Отображение пацзы
    if is_pause:
        blit_pause()

    # Обновление экрана
    pg.display.update()
    clock.tick(FPS)
        