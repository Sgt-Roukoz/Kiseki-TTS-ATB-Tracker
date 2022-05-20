def button_clicked(item):
    print(item)

def return_pressed(event):
    print("Return key pressed")

def add_actor(self, name, spd):
        if spd == "" or name == "":
            self.label.config(text = "Invalid Input for Adding Actor")
        else:
            self.actors.append([name,int(spd),"None"])
            self.label.config(text = "")

# actors = []

# actor_num = int(input("Enter number of actors: "))

# for i in range(actor_num):
#     actor_name = input("Actor " + str(i) + " name: " )
#     actor_SPD = int(input("Actor SPD: "))

#     actors.append([actor_name, actor_SPD])

# actors.sort(key=lambda x: x[1])


# print(actors)