## Task 1
print("=== Task 1 ===")


def func1(name):
    # data
    class Person:
        def __init__(self, name, side, point):
            self.name = name
            self.side = side
            self.point = point

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def get_distance(self, other_point):
            return abs(self.x - other_point.x) + abs(self.y - other_point.y)

    data = [
        Person("悟空", 0, Point(0, 0)),
        Person("辛巴", 0, Point(-3, 3)),
        Person("貝吉塔", 0, Point(-4, -1)),
        Person("特南克斯", 0, Point(1, -2)),
        Person("丁滿", 2, Point(-1, 4)),
        Person("弗利沙", 2, Point(4, -1)),
    ]

    # find current person
    input_person: Person
    for person in data:
        if person.name == name:
            input_person = person

    # find closest and farthest person (can be multiple)
    closest_person = ""
    farthest_person = ""
    min_distance = 99
    max_distance = 0

    for person in data:
        if input_person == person:
            continue

        # if on different side, add 2 more unit to distance later
        side_distance = abs(input_person.side - person.side)

        # calculate distance
        distance = input_person.point.get_distance(person.point) + side_distance

        # print(f"person {person.name} distance {distance} side distance {side_distance}")

        if distance < min_distance:
            closest_person = person.name
            min_distance = distance
        elif distance == min_distance:
            closest_person += f"、{person.name}"
        elif distance == max_distance:
            farthest_person += f"、{person.name}"
        elif distance > max_distance:
            farthest_person = person.name
            max_distance = distance

    # Answer
    print(f"最遠{farthest_person}；最近{closest_person}")


func1("辛巴")  # print 最遠弗利沙；最近丁滿、貝吉塔
func1("悟空")  # print 最遠丁滿、弗利沙；最近特南克斯
func1("弗利沙")  # print 最遠辛巴，最近特南克斯
func1("特南克斯")  # print 最遠丁滿，最近悟空


## Task 3
print("=== Task 3 ===")

def func3(index):
    # start: 25
    # rule: -2, -3, +1, +2, repeat
    # your code here
    start = 25
    remain = index // 4
    mod = index % 4
    y = 0
    if mod == 1:
        y = -2
    elif mod == 2:
        y = -5
    elif mod == 3:
        y = -4
    print(25 + (remain * (-2)) + y)


func3(1)  # print 23
func3(5)  # print 21
func3(10)  # print 16
func3(30)  # print 6
