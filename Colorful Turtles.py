#Turtle Race

import turtle
import random

screen = turtle.Screen()
screen.title = ('Colors')
screen.screensize(500, 500)

##########The Color Turtles##########
tim = turtle.Turtle()
tim.color ('red')
tim.pensize (7)
tim.shape ('turtle')
tim.speed (3)

dave = turtle.Turtle()
dave.color ('orange')
dave.pensize (7)
dave.shape ('turtle')
dave.speed (3)

sam = turtle.Turtle()
sam.color ('yellow')
sam.pensize (7)
sam.shape ('turtle')
sam.speed (3)

jay = turtle.Turtle()
jay.color ('green')
jay.pensize (7)
jay.shape ('turtle')
jay.speed (3)

ron = turtle.Turtle()
ron.color ('blue')
ron.pensize (7)
ron.shape ('turtle')
ron.speed (3)

michael = turtle.Turtle()
michael.color ('purple')
michael.pensize (7)
michael.shape ('turtle')
michael.speed (3)

bill = turtle.Turtle()
bill.color ('magenta')
bill.pensize (7)
bill.shape ('turtle')
bill.speed (3)
##########The Color Turtles##########

##########Position##########
tim.penup()
tim.setpos (-240, -250)
tim.left (90)

dave.penup()
dave.setpos (-160, -250)
dave.left (90)

sam.penup()
sam.setpos (-80, -250)
sam.left (90)

jay.penup()
jay.setpos (0, -250)
jay.left (90)

ron.penup()
ron.setpos (80, -250)
ron.left (90)

michael.penup()
michael.setpos (160, -250)
michael.left (90)

bill.penup()
bill.setpos (240, -250)
bill.left (90)
##########Position##########

##########Colors##########

tim.speed(3)
tim.pendown()
tim.forward (500)

dave.speed(3)
dave.pendown()
dave.forward (500)

sam.speed(3)
sam.pendown()
sam.forward (500)

jay.speed(3)
jay.pendown()
jay.forward (500)

ron.speed(3)
ron.pendown()
ron.forward (500)

michael.speed(3)
michael.pendown()
michael.forward (500)

bill.speed(3)
bill.pendown()
bill.forward (500)

##########Colors##########



