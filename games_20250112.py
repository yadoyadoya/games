#七並べ
import pyxel as px
import random as rmd
#from input_detector import InputDetector as Input

class App:
    def __init__(self):
        px.init(240, 160)
        px.mouse(True)
        px.load("trumpgame_resource.pyxres")
        self.init_cards()
        
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
        
    # def update(self):
    #     if Input.is_pressed(Input.UP):
    #         print("pressed UP")
    #     if Input.is_pressed(Input.DOWN):
    #         print("pressed DOWN")
    #     if Input.is_released(Input.LEFT):
    #         print("released LEFT")
    #     if Input.is_released(Input.RIGHT):
    #         print("released RIGHT")
        
    def draw(self):
        px.cls(3)
        ### カードの描画
        for i in range(5):
            #px.blt(34,145,0,0,0,10,15)
            px.blt(34+i*16,145,0,self.nums[i],self.suits[i],10,15)
        
        px.text(20,50,"pressed UP",1)
        px.text(40,50,"pressed DOWN",1)
        px.text(60,50,"released LEFT",1)
        px.text(80,50,"released RIGHT",1)

App().run()
