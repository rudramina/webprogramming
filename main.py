# #variable
# name = "Harry"
# #list
# print(names)
# print(f'main - {names[0]}')
# print(name[0])
# # coordinates 
# coordinatex = 10.0
# coordinatey = 20.0
# coordinates = (10.0, 20.0)
# # ---------------
# a= str(input("enter your name: "))
# #appending in list
# names.append(a)
# #----------------
# print(names)
# #sorting
# names.sort()
# print(names)
# # sets
# s = set()
# s.add(1)
# s.add(33)
# s.add(25)
# print(s)
# s.remove(33)
# print(f"THe set has{len( s )} elements.")
# for i in names:
#     print(i)
# for ch in "Rudra":
#     print(ch)
# houses = {"harry":"gryfinndor","draco": "slytherin"}
# houses["hermoine"] = "gryfindor"
# print(houses["harry"])
# print(houses)
# def square(x):
#     return x * x
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(12,5)
# print(p.x)
# print(p.y)
# class Flight():
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.passengers = []

#     def add_passenger(self, name):
#         if not self.vacant_seats():
#             return False
#         else:
#             self.passengers.append(name)
#             return True

#     def vacant_seats(self):
#         return self.capacity - len(self.passengers)
# flight = Flight(3)
# people = ['harry','hermoine','ron','ginny','draco']
# for name in people:
#     success = flight.add_passenger(name)
#     if success:
#         print(f"Added {name} successfully")
#     else:
#         print(f'No available seats for {name}')