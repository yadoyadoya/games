#import util.device_checker as dchk

import pyxel as px
import random as rmd
#from input_detector import InputDetector as Input
#from device_checker import DeviceChecker as Ckr
from util.device_checker import DeviceChecker as dchk

BUTTON_X = 80 #ボタンのx軸
BUTTON_Y = 120 #ボタンのy軸

class App:
    def __init__(self):
        px.init(240, 160)
        #px.mouse(True)
        px.load("trumpgame_resource.pyxres")
        self.init_cards()
        self.button = False
        
        # PC(非タップ端末)からの実行時のみマウスカーソルを表示する
        self.deviceChecker = dchk()
        px.mouse(self.deviceChecker.is_pc())
        
    def init_cards(self):
        
        self.usednumber_flags = [0] * 52
        
        ramnums = [0,11,22,33,44,55,66,77,88,99,110,121,132]
        #ramnums = [0,11,22] #test
        ramsuits = [0,16,32,48]
        #ramsuits = [0,16] #test
        
        self.nums = [0,0,0,0,0]   # 
        self.suits = [0,0,0,0,0]  # 
        
        self.pattern = ['','','','',''] 
        
        self.count = 0
        
        for i in range(5):
            #self.nums[i]  = rmd.sample(ramnums,5)
            self.Tmpnums = rmd.choice(ramnums)
            self.Tmpsuits = rmd.choice(ramsuits)
            
            self.nums[i] = self.Tmpnums
            self.suits[i] = self.Tmpsuits
            
            #仮組み合わせ
            tmppatn = str(self.Tmpnums) + str(self.Tmpsuits)
            
            
            if self.count > 0:
                #仮組み合わせが被ってたらループで被りがなくなるまで繰り返す
                while tmppatn in self.pattern:
                    self.nums[i] = rmd.choice(ramnums)
                    self.suits[i] = rmd.choice(ramsuits)
                    
                    tmppatn = str(self.nums[i]) + str(self.suits[i])
            
            #組み合わせリストに追加
            self.pattern[i] = tmppatn
            
            self.count += 1
        
    def run(self):
        #px.playm(0, loop = True)
        px.run(self.update, self.draw) # アプリケーションの実行
        
    def update(self):
        # if Input.is_pressed(Input.UP):
        #     print("pressed UP")
        # if Input.is_pressed(Input.DOWN):
        #     print("pressed DOWN")
        # if Input.is_released(Input.LEFT):
        #     print("released LEFT")
        # if Input.is_released(Input.RIGHT):
        #     print("released RIGHT")
        if px.btnp(px.MOUSE_BUTTON_LEFT): #クリック
            if BUTTON_X < px.mouse_x < BUTTON_X + 16 and BUTTON_Y < px.mouse_y < BUTTON_Y + 7: #ボタンの枠内
                self.button = True

        if px.btnr(px.MOUSE_BUTTON_LEFT): #クリックが離されたとき
            self.button = False
        
        if self.button:
            self.init_cards()
        
    def draw(self):
        px.cls(0)
        
        
        px.bltm(0, 0, 0, 0, 0, 240, 160)
        ### カードの描画
        for i in range(5):
            #px.blt(34,145,0,0,0,10,15)
            px.blt(34+i*16,145,0,self.nums[i],self.suits[i],10,15,0)
        
        px.blt(34 ,90 ,1 ,0 ,0 ,16 ,24 ,0)
        if self.button:
            px.blt(BUTTON_X,BUTTON_Y,1,0,49,16,7,0)
        else:
            px.blt(BUTTON_X,BUTTON_Y,1,0,41,16,7,0)
        
        
        
        # px.text(20,50,"pressed UP",1)
        # px.text(40,50,"pressed DOWN",1)
        # px.text(60,50,"released LEFT",1)
        # px.text(80,50,"released RIGHT",1)
        self.test_text(6, 10)

    def test_text(self, x, y):
        px.text(x, y, "text(x,y,s,col)", 7)
        x += 4
        y += 8
        s = (
            f"Elapsed frame count is {px.frame_count}\n"
            f"Current mouse position is ({px.mouse_x},{px.mouse_y})"
        )
        px.text(x + 1, y, s, 1)
        px.text(x, y, s, 9)


App().run()
