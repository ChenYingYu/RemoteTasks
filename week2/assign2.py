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
        Person("特南克斯", 0, Point(1, -2)),
        Person("丁滿", 2, Point(-1, 4)),
        Person("貝吉塔", 0, Point(-4, -1)),
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
    return f"最遠{farthest_person}；最近{closest_person}"


print(func1("辛巴"))  # print 最遠弗利沙；最近丁滿、貝吉塔
print(func1("悟空"))  # print 最遠丁滿、弗利沙；最近特南克斯
print(func1("弗利沙"))  # print 最遠辛巴，最近特南克斯
print(func1("特南克斯"))  # print 最遠丁滿，最近悟空


## Task 2
print("=== Task 2 ===")

import re, operator

available_slot = {"S1": set(), "S2": set(), "S3": set()}


# book the best match service that fits the criteria and available
def func2(ss, start, end, criteria):
    book_time_slot = set(range(start, end))
    time_available_services = check_time_availability(book_time_slot, ss)
    formatted_criteria = parse_criteria(criteria)

    if formatted_criteria is None:
        return book(None, book_time_slot)

    best_service = find_best_match(formatted_criteria, time_available_services)
    return book(best_service, book_time_slot)


def find_best_match(format_criteria, available_services):
    attribute_key = format_criteria["attribute_key"]
    operator_symbol = format_criteria["operator_symbol"]
    criteria_value = format_criteria["criteria_value"]

    qualified_services = [
        s
        for s in available_services
        if OPERATORS[operator_symbol](s.get(attribute_key, 0), criteria_value)
    ]
    if not qualified_services:
        return None

    if operator_symbol != "=":
        tie_breaker_func = TIE_BREAKER_MAP.get(operator_symbol)
        best_service = tie_breaker_func(
            qualified_services, key=lambda s: s.get(attribute_key, 0)
        )
        return best_service["name"]
    else:
        return qualified_services[0]["name"]


def check_time_availability(book_time_slot, services):
    available_services = [
        s for s in services if (book_time_slot & available_slot[s["name"]]) == set()
    ]
    return available_services


def book(service, time_slot):

    if service is not None:
        available_slot[service] |= time_slot
        return service
    else:
        return "Sorry"


def parse_criteria(criteria):
    match = re.match(r"([a-z]+)([><]=?|=)([\w.]+)", criteria)
    if match:
        attribute_key, operator_symbol, criteria_value = match.groups()

        if attribute_key == "r" or attribute_key == "c":
            criteria_value = float(criteria_value)
        return {
            "attribute_key": attribute_key,
            "operator_symbol": operator_symbol,
            "criteria_value": criteria_value,
        }
    else:
        return None


TIE_BREAKER_MAP = {
    ">=": min,
    "<=": max,
    ">": min,
    "<": max,
}

OPERATORS = {
    "=": operator.eq,
    ">=": operator.ge,
    "<=": operator.le,
    ">": operator.gt,
    "<": operator.lt,
}

services = [
    {"name": "S1", "r": 4.5, "c": 1000},
    {"name": "S2", "r": 3, "c": 1200},
    {"name": "S3", "r": 3.8, "c": 800},
]

if __name__ == "__main__":
    print(func2(services, 15, 17, "c>=800"))  # S3
    print(func2(services, 11, 13, "r<=4"))  # S3
    print(func2(services, 10, 12, "name=S3"))  # Sorry
    print(func2(services, 15, 18, "r>=4.5"))  # S1
    print(func2(services, 16, 18, "r>=4"))  # Sorry
    print(func2(services, 13, 17, "name=S1"))  # Sorry
    print(func2(services, 8, 9, "c<=1500"))  # S2
    print(func2(services, 8, 9, "c<=1500"))  # S1
    print(func2(services, 8, 9, "c<=1500"))  # S3
    print(func2(services, 8, 9, "c<=1500"))  # Sorry

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
    if len(sp) != len(stat):
        raise ValueError("Input 'sp' list and 'stat' string must have the same length.")

    stat_arr = str(stat).split()

    min_available = None
    max_available = None
    min_available_index = None
    max_available_index = None
    for index, char in enumerate(stat):
        if char == "1":
            continue  # skip this car since 1 means not available
        if sp[index] == n:  # perfect match, end the process
            return index
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
        return max_available_index
    elif min_available_index is not None:
        return min_available_index
    else:
        return "Error"


print(func4([3, 1, 5, 4, 3, 2], "101000", 2))  # print 5
print(func4([1, 0, 5, 1, 3], "10100", 4))  # print 4
print(func4([4, 6, 5, 8], "1000", 4))  # print 2
