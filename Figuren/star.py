import turtle

achtergrondKleur = "lightgreen"
kleurUitlijning = "white"
kleurVulling = "purple"
snelheid = 10
penGrootte = 10
schaal = 2

turtle.title("BAZ | Snuffeldag Januari 2024 - Ster")
turtle.bgcolor(achtergrondKleur)

turtle.pen(pencolor=kleurUitlijning, fillcolor=kleurVulling, speed=snelheid, pensize=penGrootte)

wn = turtle.Screen().getcanvas().winfo_toplevel()
wn.wm_attributes("-fullscreen", 1)
wn.wm_attributes("-topmost", 1)

turtle.begin_fill()
for i in range(8):
    turtle.forward(200 * schaal)
    turtle.left(135)

turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()

# Copyright (c) 2023 Cédric Verlinden & Jasper Verbruggen. All rights reserved.