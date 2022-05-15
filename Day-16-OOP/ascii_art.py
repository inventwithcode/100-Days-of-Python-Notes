import prettytable
import os

table = prettytable.PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.hrules = prettytable.ALL
print(table)
