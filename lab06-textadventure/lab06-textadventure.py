class Room:

    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.west = west
        self.south = south
        self.east = east
def main():
        room_list = []

        room_1 = Room(" Este es el baño de la casa. Tienes dos puertas, una al norte y otra al oeste",3, None, None,4)
        room_list.append(room_1)

        room_2 = Room(" Esta es mi habitación. Tienes tres puertas, una al sur, otra al este y la ultima al oeste",None,4,3,2)
        room_list.append(room_2)

        room_3 = Room("Este es el balcón, lo conseguiste",None,None,1,None)
        room_list.append(room_3)

        room_4 = Room("Esta es la habitación de Marta. Tienes dos puertas, una al sur y la otra al oeste",None,0, None,1)
        room_list.append(room_4)

        room_5 = Room("Esta es la habitación de mis padres. Tienes dos puertas, una al norte y la otra al este",1, None,0, None)
        room_list.append(room_5)

        current_room = 0
        done = False

        while done == False:
            print()
            print(room_list[current_room].description)
            if current_room == 2:
                break
            x = input("¿Que quieres hacer?")

            if x == "n" or x == "norte" or x == "N":
                next_room = room_list[current_room].north
                if next_room == None:
                    print("No puedes ir por ese camino")
                else:
                    current_room = next_room

            elif x == "s" or x == "sur" or x == "S":
                next_room = room_list[current_room].south
                if next_room == None:
                    print("No puedes ir por ese camino")
                else:
                    current_room = next_room

            elif x == "e" or x == "este" or x == "E":
                next_room = room_list[current_room].east
                if next_room == None:
                    print("No puedes ir por ese camino")
                else:
                    current_room = next_room


            elif x == "o" or x == "oeste" or x == "O":
                next_room = room_list[current_room].west
                if next_room == None:
                    print("No puedes ir por ese camino")
                else:
                    current_room = next_room

            elif x == "salir":
                done = True

main()
