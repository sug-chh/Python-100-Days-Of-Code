
# import turtle
#
# timmy = turtle.Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = turtle.Screen()
#
# print(my_screen.canvwidth)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = 'l'

print(table)

