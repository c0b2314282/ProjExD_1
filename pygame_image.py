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
        x = tmr%3200 
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #練習10-3

        y = -1
        h = 0
        if key_lst[pg.K_UP]:
            h -=1 #練習10-4
        if key_lst[pg.K_DOWN]:
            h +=1 #練習10-4
        if key_lst[pg.K_LEFT]:
            y -=1 #練習10-4
        if key_lst[pg.K_RIGHT]:
            y +=2 #練習10-4/演習1-2
    
        kk_rct.move_ip(y,h) #演習1


        #x = tmr%3200 #練習６
        screen.blit(bg_img, [-x, 0]) #練習６
        screen.blit(bg_img2, [-x+1600, 0]) #練習７
        screen.blit(bg_img, [-x + 3200, 0]) #練習9
        #screen.blit(kk_img, [300, 200]) #練習4
        screen.blit(kk_img, kk_rct) #練習4 / 練習10-5
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()