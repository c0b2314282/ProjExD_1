import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) #練習8
    kk_img = pg.image.load("fig/3.png") #練習２前半
    kk_img = pg.transform.flip(kk_img, True, False) #練習２後半
    kk_rct = kk_img.get_rect() #練習10-1:こうかとんRectの抽出
    kk_rct.center = 300, 200 #練習10-2:こうかとんRectの中心座標を指定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #練習10-3

        if key_lst[pg.K_UP]:
            kk_rct.move_ip(0,-1) #練習10-4
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip(0, +1) #練習10-4
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip(-1, 0) #練習10-4
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip(+1, 0) #練習10-4
        
        x = tmr%3200 #練習６
        screen.blit(bg_img, [-x, 0]) #練習６
        screen.blit(bg_img2, [-x+1600, 0]) #練習７
        screen.blit(bg_img, [-x + 3200, 0]) #練習9
        screen.blit(kk_img, [300, 200]) #練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()