class Box:
    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height

    def volume(self):
        return self.__length * self.__width * self.__height

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

def box_sort(box_list):
    for i in range(1, len(box_list)):
        key = box_list[i]
        j = i - 1
        while j >= 0 and key.volume() > box_list[j].volume():
            box_list[j + 1] = box_list[j]
            j -= 1
        box_list[j + 1] = key
b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)

box_list = [b1, b2, b3]
box_sort(box_list)

for box in box_list:
    print(f"Box with dimensions {box.get_length()} x {box.get_width()} x {box.get_height()} has volume {box.volume()}")
