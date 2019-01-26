from model.Tab import Tab

# Init model
table = Tab()

# Get items from user and add them
while True:
    item = input(
        "Enter item: (all lowercase and if more than one words then separate with '_') ")
    table.add(item)
    add_another = input("Anything else? (y/n) ")
    if add_another is 'y':
        continue
    elif add_another is 'n':
        break

service_charge = input("Enter service charge amount: ")
tax_charge = input("Enter tax amount: ")
table.print_bill(tax_charge, service_charge)
