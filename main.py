import pygame as pg
import gif_pygame as gifpg
import os

# Иниацилизация
pg.init()

# Переменные 
is_game = True
RES = WW, WH = 370, 260
clock = pg.time.Clock()
FPS = 10
is_pause  = False
volume = 20

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
    try: 
        window.blit(pg.transform.scale(pg.image.load('src/NTBG.png'), (360, 280)), (0, 0))
        window.blit(pg.transform.scale(pg.image.load('src/BG.png'), (360, 280)), (0, 0))
    except: 
        window.fill((255, 255, 255))
    gif.render(window, (0, 0))
    
    # Обработка событий
    for event in pg.event.get():
        # Обработка выхода
        if event.type == pg.QUIT:
            is_game = False
            
        # Обработка нажатия клавиши
        if event.type == pg.KEYDOWN:
            # Пазуа
            if event.key == pg.K_SPACE:
                is_pause = not is_pause
                
                if is_pause:
                    pg.mixer.music.pause()
                    gif.pause()
                    
                else:
                    pg.mixer.music.unpause()
                    gif.unpause()
            
            # Увеличение и уменьшение звука
            elif event.key == pg.K_UP:
                volume += 1
                if volume > 20: volume = 20
                
                pg.mixer.music.set_volume(volume/20)
                
            elif event.key == pg.K_DOWN:
                volume -= 1
                if volume < 0: volume = 0
                
                pg.mixer.music.set_volume(volume/20)
                
            # Перезапуск
            elif event.key == pg.K_r:
                pg.mixer.music.play(-1)
                gif = gifpg.load('src/konata-dance.gif')
                is_pause = False
                    
    # Отображение пацзы
    if is_pause:
        blit_pause()
        
    # Отображение звука
    pg.draw.rect(window, (255, 255, 255), (360, 0, 10, 260))
    pg.draw.rect(window, (128, 128, 128), (360, 0, 10, 260-volume*13))

    # Обновление экрана
    pg.display.update()
    clock.tick(FPS)
        