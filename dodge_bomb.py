import random
import sys
import time
import pygame as pg

# こうかとん移動量
delta = {pg.K_UP: (0, -1), 
         pg.K_DOWN: (0, +1), 
         pg.K_LEFT: (-1, 0), 
         pg.K_RIGHT: (+1, 0)}

# speed
speed = [a for a in range(1, 11)]
print(speed)

# avx, avy = vx*speed[min(tmr//1000, 9)], vy*speed[min(tmr//1000, 9)]
             
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    fonto  = pg.font.Font(None, 150)
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()


    # 爆弾
    bb_img = pg.Surface((20, 20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_img.set_colorkey((0, 0, 0))
    x, y = random.randint(0, 1600), random.randint(0, 900)  # 爆弾のx, y座標
    vx, vy = +1, +1             # 横方向、縦方向の速度
    bb_rct = bb_img.get_rect()  # rectクラスのsurface取得
    bb_rct.center = (x, y)      # centerの位置をランダムに設定
    
    
    tmr = 0         # タイマー初期値

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:           # ✕ボタンが押されたら
                return 0                        # プログラム終了

        tmr += 1    # タイマー

        key_lst = pg.key.get_pressed()          # 押されたキーを取得
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)

        if check_bound(screen.get_rect(), kk_rct) != (True, True):
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0], -mv[1])

        screen.blit(bg_img, [0, 0])             # 背景表示
        screen.blit(kk_img, kk_rct)             # こうかとん表示

        avx, avy = vx*speed[min(tmr//1000, 9)], vy*speed[min(tmr//1000, 9)]
        bb_rct.move_ip(avx, avy)                  # 爆弾を動かす
        
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko:        # 横方向にはみ出したら
            vx *= -1
        if not tate:        # 縦方向にはみ出したら
            vy *= -1
        screen.blit(bb_img, bb_rct)             # 爆弾表示

        if kk_rct.colliderect(bb_rct):          # こうかとんと爆弾が重なったら
            return                              # プログラム終了
        

        pg.display.update()
        clock.tick(1000)

        # print(vx, vy)

# 画面内or画面外の判定をする関数
def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す変数
    引数1:　画面surfaceのrect
    引数2:　こうかとん、または爆弾surfaceのrect
    戻り値:　横方向、縦方向のはみだし判定結果(画面内: True／画面外: False)
    """
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False

    return yoko, tate

# こうかとんの向きを変える関数を作ろうとして未完成
"""
def kokaton(x, y):
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img2 = pg.transform.flip(kk_img, True, False)
    # こうかとんの向き
    direction = {pg.transform.rotozoom(kk_img2, -90, 2.0): (0, -1),
                 pg.transform.rotozoom(kk_img2, -45, 2.0): (1, -1),
                 pg.transform.rotozoom(kk_img2, 0, 2.0): (1, 0),
                 pg.transform.rotozoom(kk_img2, 45, 2.0): (1, 1),
                 pg.transform.rotozoom(kk_img2, 90, 2.0): (0, 1),
                 pg.transform.rotozoom(kk_img, 45, 2.0): (-1, 1),
                 pg.transform.rotozoom(kk_img, 0, 2.0): (-1, 1),
                 pg.transform.rotozoom(kk_img, -45, 2.0): (-1, -1)}
    for k, d in direction.items():
        if d == (x, y):
            muki = d
    return k, muki
"""

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()