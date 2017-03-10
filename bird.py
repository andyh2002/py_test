#!/usr/bin/env python
class Bird:
    def __init__(self):
            self.hungry = True

    def eat(self) -> object:
        if self.hungry:
            print("Aaaah...")
            self.hungry = False
        else:
            print("No. Thanks!")


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)         # 调用超类未绑定的构造方法
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
