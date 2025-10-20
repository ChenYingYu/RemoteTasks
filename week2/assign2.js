// Task 1
console.log("=== Task 1 ===");

function func1(name) {
  // data
  class Person {
    constructor(name, side, point) {
      this.name = name;
      this.side = side;
      this.point = point;
    }
  }

  class Point {
    constructor(x, y) {
      this.x = x;
      this.y = y;
    }

    getDistance(otherPoint) {
      return Math.abs(this.x - otherPoint.x) + Math.abs(this.y - otherPoint.y);
    }
  }

  const data = [
    new Person("悟空", 0, new Point(0, 0)),
    new Person("辛巴", 0, new Point(-3, 3)),
    new Person("貝吉塔", 0, new Point(-4, -1)),
    new Person("特南克斯", 0, new Point(1, -2)),
    new Person("丁滿", 2, new Point(-1, 4)),
    new Person("弗利沙", 2, new Point(4, -1)),
  ];

  // find current person
  let inputPerson = new Person();
  for (let person of data) {
    if (person.name == name) {
      inputPerson = person;
    }
  }

  // find closest and farthest person (can be multiple)
  let closestPerson = "";
  let farthestPerson = "";
  let minDistance = 99;
  let maxDistance = 0;

  for (let person of data) {
    if (inputPerson == person) {
      continue;
    }

    // if on different side, add 2 more unit to distance later
    const sideDistance = Math.abs(inputPerson.side - person.side);

    // calculate distance
    const distance = inputPerson.point.getDistance(person.point) + sideDistance;

    if (distance < minDistance) {
      closestPerson = person.name;
      minDistance = distance;
    } else if (distance == minDistance) {
      closestPerson += `、${person.name}`;
    } else if (distance == maxDistance) {
      farthestPerson += `、${person.name}`;
    } else if (distance > maxDistance) {
      farthestPerson = person.name;
      maxDistance = distance;
    }
  }

  // Answer
  console.log(`最遠${farthestPerson}；最近${closestPerson}`);
}

func1("辛巴"); // print 最遠弗利沙；最近丁滿、貝吉塔
func1("悟空"); // print 最遠丁滿、弗利沙；最近特南克斯
func1("弗利沙"); // print 最遠辛巴，最近特南克斯
func1("特南克斯"); // print 最遠丁滿，最近悟空

// Task 3
console.log("=== Task 3 ===");

function func3(index) {
  // start: 25
  // rule: -2, -3, +1, +2, repeat
  // your code here
  const start = 25;
  const remain = Math.floor(index / 4);
  const mod = index % 4;
  let y = 0;
  switch (mod) {
    case 1:
      y = -2;
      break;
    case 2:
      y = -5;
      break;
    case 3:
      y = -4;
      break;
  }

  console.log(start + remain * -2 + y);
}

func3(1); // print 23
func3(5); // print 21
func3(10); // print 16
func3(30); // print 6
