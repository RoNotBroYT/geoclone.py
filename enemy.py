

from graphics import *
import random

class Enemy:

    def __init__(self, win:GraphWin):
        
        self.direction = random.randint(0, 1)
        if self.direction == 0:     
            self.direction -= 1
            self.x = 750
        else:
            self.x = 0

        strength = random.randint(1, 3)
        self.health = strength
        self.speed = strength    

        if self.health == 3:
            self.color = "Red"
        if self.health == 2:
            self.color = "Yellow"
        if self.health == 1:
            self.color = "Green"
        if self.direction == -1:
            self.speed *= -1

    def getX(self):
        return self.x

    def flip(self):
        self.direction *= -1
        self.speed *= -1

   




class Sphere(Enemy):

    def __init__(self, win: GraphWin):
        super().__init__(win)
        self.rad = 25
        self.y = 175     
        self.sphere = Circle(Point(self.x, self.y), self.rad)
        self.hitbox = Rectangle(Point(self.x - self.rad, self.y - self.rad//2), Point(self.x + self.rad,  self.y -self.rad//3))
        self.killbox = Rectangle(Point(self.x - self.rad, self.y + self.rad//2 + 5), Point(self.x + self.rad,  self.y +self.rad//3 + 5))
        self.peak = 50

    def draw(self, win: GraphWin):
        self.sphere.setFill(self.color)
        self.sphere.draw(win)

      
        self.hitbox.setFill("green")
        self.hitbox.draw(win)
        self.killbox.setFill("yellow")
        self.killbox.draw(win)

    def undraw(self):           
        self.sphere.undraw()
        self.hitbox.undraw()
        self.killbox.undraw()

    def charge(self):
        self.sphere.move(self.speed, 0)
        self.hitbox.move(self.speed, 0)
        self.killbox.move(self.speed, 0)
        self.x += self.speed
 

    def hit(self):
        """deducts health, flips, and kills """
        self.health -= 1
        self.speed -= 1
        self.flip()
        if self.health == 2:
            self.color = "Yellow"
        if self.health == 1:
            self.color = "Green"

        if self.health == 0:
            self.undraw()

class Cone(Enemy):
    def __init__(self, win: GraphWin):
        super().__init__(win)
        self.sideLen = 50   
        self.y = 250     
        self.triangle = Polygon(Point(self.x, self.y), Point(self.x + self.sideLen,  self.y), Point(self.x + (.5 * self.sideLen), self.y + (self.sideLen)))
        self.hitbox = Rectangle(Point(self.x, self.y), Point(self.x + self.sideLen,  self.y + 2))
        self.killbox = Rectangle(Point(self.x + 10, self.y + 20), Point(self.x + 40,  self.y + 25))
        self.peak = 100

    def draw(self, win: GraphWin):
        self.triangle.setFill(self.color)
        self.triangle.draw(win)
        
      
        self.hitbox.setFill("green")
        self.killbox.setFill("yellow")
        self.hitbox.draw(win)
        self.killbox.draw(win)

    def undraw(self):          
        self.triangle.undraw()
        self.hitbox.undraw()
        self.killbox.undraw()

    def charge(self):
        self.triangle.move(self.speed, 0)
        self.hitbox.move(self.speed, 0)
        self.killbox.move(self.speed, 0)
        self.x += self.speed

    def hit(self):                     
        """deducts health, flips, and kills """
        self.health -= 1
        self.speed -= 1
        self.flip()
        if self.health == 2:
            self.color = "Yellow"
        if self.health == 1:
            self.color = "Green"

        if self.health == 0:
            self.undraw()

class Box(Enemy):
    count = 1
    def __init__(self, win: GraphWin):
        super().__init__(win)
        self.side = 50
        self.y = 350     
        self.box = Rectangle(Point(self.x, self.y), Point(self.x + self.side, self.y + self.side))
        self.hitbox = Rectangle(Point(self.x, self.y), Point(self.x + 50,  self.y + 5))         
        self.killbox = Rectangle(Point(self.x, self.y + 20), Point(self.x + 50,  self.y + 25))
        self.peak = 310
        Box.count += 1


    def draw(self, win: GraphWin):
        self.box.setFill(self.color)
        self.box.draw(win)

        self.killbox.setFill("yellow")
        self.hitbox.setFill("green")
        self.hitbox.draw(win)
        self.killbox.draw(win)

    def undraw(self):          
        self.box.undraw()
        self.hitbox.undraw()
        self.killbox.undraw()

    def charge(self):
        self.box.move(self.speed, 0)
        self.hitbox.move(self.speed, 0)
        self.killbox.move(self.speed, 0)
        self.x += self.speed
 

    def hit(self):
        """deducts health, flips, and kills """
        self.health -= 1
        self.speed -= 1
        self.flip()
        if self.health == 2:
            self.color = "Yellow"
        if self.health == 1:
            self.color = "Green"

        if self.health == 0:
            Box.count -= 1
            print(Box.count)
            self.undraw()


