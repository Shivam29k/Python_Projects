from turtle import Turtle
import random

colors = ["red", "blue", "purple", "yellow", "green", "orange", "pink", "teal"]
y_postion = [200, 175, 150, 125, 100, 75, 50, 25, 0, -25, -50, -75, -100, -125, -150, -175, -200]


class Car_manager(Turtle):

    def __init__(self):
        self.car_speed = 5
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(f"{random.choice(colors)}")
            new_car.penup()
            new_car.goto(320,random.choice(y_postion))
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)
        
    

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    
    def inc_car_speed(self):
        self.car_speed += (self.car_speed*0.5)

      
