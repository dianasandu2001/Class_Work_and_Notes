Shopping_List = []
while True:
    item = input("Enter item on shopping list: ")
    if item.lower() == 'done':
        break
    Shopping_List.append(item)
for index, item in enumerate(Shopping_List, start=1):
    print(f"{index}:{item}")