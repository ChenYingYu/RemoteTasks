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


## Task 2
print("=== Task 2 ===")


available_slot = {"S1": set(), "S2": set(), "S3": set()}
available_services = []


def func2(ss, start, end, criteria):
    global available_services
    time_slot = set(range(start, end))
    available_services = check_availability(time_slot)
    # check what kind of criteria
    str_arr = str(criteria).split("=")
    str_prefix = str_arr[0]
    str_postfix = str_arr[1]
    target_service = ""

    if str_prefix[0] == "r":
        # do rating logic
        condition = str_prefix[-1]
        rating_criteria = float(str_postfix)
        if condition == "<":
            target_service = find_max_rating_below(rating_criteria)
        elif condition == ">":
            target_service = find_min_rating_above(rating_criteria)

    elif criteria[0] == "c":
        # do cost logic
        condition = str_prefix[-1]
        cost_criteria = float(str_postfix)
        if condition == "<":
            target_service = find_max_cost_below(cost_criteria)
        elif condition == ">":
            target_service = find_min_cost_above(cost_criteria)

    elif criteria[0] == "n":
        # do name logic
        name = str_postfix
        target_service = find_service(name)

    if target_service != "Sorry":
        book(target_service, time_slot)
    else:
        print("Sorry")


def find_max_rating_below(rating_criteria):
    target_service = "Sorry"  # default none
    max_rating = None

    for service in services:
        if service["name"] not in available_services:
            continue
        rating = float(service["r"])
        if rating <= rating_criteria:
            if max_rating is None:
                max_rating = rating
                target_service = service["name"]
            elif rating > max_rating:
                max_rating = rating
                target_service = service["name"]

    return target_service


def find_min_rating_above(rating_criteria):
    target_service = "Sorry"  # default none
    min_rating = None

    for service in services:
        if service["name"] not in available_services:
            continue
        rating = float(service["r"])
        if rating >= rating_criteria:
            if min_rating is None:
                min_rating = rating
                target_service = service["name"]
            elif rating < min_rating:
                min_rating = rating
                target_service = service["name"]

    return target_service


def find_max_cost_below(cost_criteria):
    target_service = "Sorry"  # default none
    max_cost = None

    for service in services:
        if service["name"] not in available_services:
            continue
        cost = float(service["c"])
        if cost <= cost_criteria:
            if max_cost is None:
                max_cost = cost
                target_service = service["name"]
            elif cost > max_cost:
                max_cost = cost
                target_service = service["name"]

    return target_service


def find_min_cost_above(cost_criteria):
    target_service = "Sorry"  # default none
    min_cost = None

    for service in services:
        if service["name"] not in available_services:
            continue
        cost = float(service["c"])
        if cost >= cost_criteria:
            if min_cost is None:
                min_cost = cost
                target_service = service["name"]
            elif cost < min_cost:
                min_cost = cost
                target_service = service["name"]

    return target_service


def find_service(name):
    target_service = "Sorry"  # default none
    for service in services:
        if service["name"] not in available_services:
            continue
        if name == service["name"]:
            target_service = service["name"]
            print(target_service)
            return

    return target_service


def check_availability(time_slot):
    available_services = []
    for service in available_slot:
        if (time_slot & available_slot[service]) == set():
            available_services.append(service)
            # print("append")
            # print(f"available_services {available_services}")
    return available_services


def book(service, time_slot):
    available_slot[service] |= time_slot
    print(service)


services = [
    {"name": "S1", "r": 4.5, "c": 1000},
    {"name": "S2", "r": 3, "c": 1200},
    {"name": "S3", "r": 3.8, "c": 800},
]

func2(services, 15, 17, "c>=800")  # S3
func2(services, 11, 13, "r<=4")  # S3
func2(services, 10, 12, "name=S3")  # Sorry
func2(services, 15, 18, "r>=4.5")  # S1
func2(services, 16, 18, "r>=4")  # Sorry
func2(services, 13, 17, "name=S1")  # Sorry
func2(services, 8, 9, "c<=1500")  # S2


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
    return 25 + (remain * (-2)) + y


print(func3(1))  # print 23
print(func3(5))  # print 21
print(func3(10))  # print 16
print(func3(30))  # print 6

## Task 4
print("=== Task 4 ===")


def func4(sp, stat, n):
    # rule: fit people into a car
    stat_arr = str(stat).split

    min_available = None
    max_available = None
    min_available_index = None
    max_available_index = None
    for index, char in enumerate(stat):
        if char == "1":
            continue  # skip this car since 1 means not available
        if sp[index] == n:  # perfect match, end the process
            print(index)
            return
        elif sp[index] > n:
            if max_available is None:
                max_available = sp[index]
                max_available_index = index
            elif sp[index] < max_available:
                max_available = sp[index]
                max_available_index = index
        elif sp[index] < n:
            if min_available is None:
                min_available = sp[index]
                min_available_index = index
            elif sp[index] > min_available:
                min_available = sp[index]
                min_available_index = index

    # Answer
    if max_available_index is not None:
        print(max_available_index)
    elif min_available_index is not None:
        print(min_available_index)
    else:
        print("Error")


func4([3, 1, 5, 4, 3, 2], "101000", 2)  # print 5
func4([1, 0, 5, 1, 3], "10100", 4)  # print 4
func4([4, 6, 5, 8], "1000", 4)  # print 2
