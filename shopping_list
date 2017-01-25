#SHOPPING APP
def help_list():
    print("Welcome to the shop list APP")
    print("""
    Enter 'DONE' to stop the app
    Enter 'HELP' to see this help table
    Enter 'SHOW' to see saved items on the list
    """)
def show(a):
    for listt in a:
        print(listt)

shopping_list=[]
count=0

while True:
    value=input("Item :")
    if value=="HELP":
        help_list()

    shopping_list.append(value)
    if value=="SHOW" or value=="DONE" or value=="HELP":
        shopping_list.remove(value)
    else:
        count += 1
        print("{} added to the list and list has {} items".format(value,count))
    if value=="SHOW":
        show(shopping_list)
    if value=="DONE":
        show(shopping_list)
        break





