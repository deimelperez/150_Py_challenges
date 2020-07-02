tv_shows_list = ["Friends","HIMYM","GoT","Vikings"]
for i in tv_shows_list:
    print(i)
new_show = input("Enter a new tv show: ")
pos = int(input("Enter its position: "))
tv_shows_list.insert(pos,new_show)
for i in tv_shows_list:
    print(i)
    
input("Press enter to continue")
