'''
1、三个厨师，每3秒做一个，满了的话停三秒做
2、有5个客人，每人100元，一个面包2元，没有面包等2两秒，钱花完为止
3、房间可以放500个面包

'''

import threading
import time

bread = 0


class chef(threading.Thread):
    name = ""
    c = 0
    def run(self) ->None:
        global bread
        while True:
            if bread<500:
                bread = bread + 1
                self.c = self.c + 1
                print(self.name,"做了一个面包，现在有",bread,"个面包")
                time.sleep(0.01)
            else:
                time.sleep(3)
                print(self.name,"睡了3秒")
                print(self.name,"做了",self.c,"个面包")

class client(threading.Thread):
    name = ""
    money = 1000
    a = 0

    def run(self) -> None:
        global bread
        while True:
            if bread > 0 and self.money>0:
                self.money = self.money - 2
                self.a = self.a + 1
                bread = bread - 1
                print(self.name,"卖了一个面包，现在还有",bread,"个面包，还有",self.money,"钱")
                time.sleep(0.05)
            elif self.money <=0:
                print(self.name,"没有钱了")
                break
            else:
                time.sleep(2)
                print(self.name,"卖了",self.a,"个面包")
                print(self.name,"等待两秒")



c1 = chef()
c2 = chef()
c3 = chef()
c1.name = "厨师1"
c2.name = "厨师2"
c3.name = "厨师3"

ce1 = client()
ce2 = client()
ce3 = client()
ce4 = client()
ce5 = client()
ce1.name = "顾客1"
ce2.name = "顾客2"
ce3.name = "顾客3"
ce4.name = "顾客4"
ce5.name = "顾客5"

c1.start()
c2.start()
c3.start()

ce1.start()
ce2.start()
ce3.start()
ce4.start()
ce5.start()
