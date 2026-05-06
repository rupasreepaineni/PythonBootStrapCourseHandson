import prettytable
table = prettytable.PrettyTable() #here we're creating/constructing an object of the class PrettyTable
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
table.align = "l" # it's like using variable

print(table)