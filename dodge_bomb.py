import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta={
    pg.K_UP:(0,-5),
    pg.K_DOWN:(0,+5),
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(+5,0),
}

def check_bound(obj_rct:pg.Rect):
    yoko,tate=True,True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko=False
    if obj_rct.top<0 or HEIGHT <obj_rct.bottom:
        tate=False
    return yoko,tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    """こうかとん"""
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)#こうかとん回転
    kk_rct=kk_img.get_rect()
    kk_rct.center=(900,400)



    """ばくだん"""
    bd_img = pg.Surface((20, 20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10) 
    bd_rct=bd_img.get_rect() #Surfaceからrectを抽出
    x,y=random.randint(0,WIDTH),random.randint(0,HEIGHT)
    bd_rct.center=(x,y)
    vx,vy= +5,+5 #練習２：爆弾の速度

    clock = pg.time.Clock()

    #accs=[a for a in range(1,11)]


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bd_rct):
            print("ゲームオーバー")
            return 

        screen.blit(bg_img, [0, 0])

        """こうかとん"""
        key_lst=pg.key.get_pressed()
        sum_mv=[0,0]

        for key, mv in delta.items():
            if key_lst[key]:
                sum_mv[0]+=mv[0]#練習３：横方向の合計移動量
                sum_mv[1]+=mv[1]#練習３：縦方向の合計移動量
        kk_rct.move_ip(sum_mv[0],sum_mv[1])#練習３：移動させる
        if check_bound(kk_rct)!=(True,True):#練習４：はみだし判定
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])
        screen.blit(kk_img, kk_rct)#練習３：移動後の座標に表示させる「￥

        """回転こうかとん"""
        #if pg.K_UP:#上
            #screen.blit(pg.transform.rotozoom(kk_img, 90, 1.0), kk_rct)
        #elif pg.k_DOWN:
            #screen.blit(pg.transform.rotozoom(kk_img, -90, 1.0), kk_rct)

            
        #else:
            #screen.blit(pg.transform.rotozoom(kk_img, 0, 1.0), kk_rct)


        #爆弾

        bd_rct.move_ip(vx,vy)
        yoko,tate=check_bound(bd_rct)
        if not yoko:
            vx*=-1
        if not tate:
            vy*=-1
        screen.blit(bd_img, bd_rct)

        bd_rct.move_ip(vx,vy)
        screen.blit(bd_img,bd_rct) #練習１試しにblit
        pg.display.update()
        tmr += 1
        clock.tick(50)

        if tmr==100: #時間経過にともない早くなる
            vx=20
            vy=20
        
        if tmr==300:
            vx=30
            vy=30
        
        if tmr==500:
            vx=40
            vy=40



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()