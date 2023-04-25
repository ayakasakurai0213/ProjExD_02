import random
import sys
import pygame as pg

# こうかとん移動量
delta = {pg.K_UP: (0, -1), 
         pg.K_DOWN: (0, +1), 
         pg.K_LEFT: (-1, 0), 
         pg.K_RIGHT: (+1, 0)}


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
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

        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)

        screen.blit(bg_img, [0, 0])             # 背景表示
        screen.blit(kk_img, kk_rct)             # こうかとん表示
        bb_rct.move_ip(vx, vy)                  # 爆弾を動かす
        screen.blit(bb_img, bb_rct)             # 爆弾表示

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()