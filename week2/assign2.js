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

// Task 2
console.log("=== Task 2 ===");

let availableSlot = new Map([
  ["S1", new Set()],
  ["S2", new Set()],
  ["S3", new Set()],
]);
let availableServices = [];

function func2(ss, start, end, criteria) {
  const timeSlot = new Set(
    Array.from({ length: end - start }, (_, index) => start + index)
  );
  availableServices = checkAvailability(timeSlot);
  // check what kind of criteria

  const strArr = criteria.split("=");
  const strPrefix = strArr[0];
  const strPostfix = strArr[1];
  let targetService = "";

  if (strPrefix[0] == "r") {
    // do rating logic
    const condition = strPrefix.at(-1);
    const ratingCriteria = strPostfix;
    if (condition == "<") {
      targetService = findMaxRatingBelow(ratingCriteria);
    } else if (condition == ">") {
      targetService = findMinRatingAbove(ratingCriteria);
    }
  } else if (strPrefix[0] == "c") {
    // do cost logic
    const condition = strPrefix.at(-1);
    const costCriteria = strPostfix;
    if (condition == "<") {
      targetService = findMaxCostBelow(costCriteria);
    } else if (condition == ">") {
      targetService = findMinCostAbove(costCriteria);
    }
  } else if (criteria[0] == "n") {
    // do name logic
    const name = strPostfix;
    targetService = findService(name);
  }

  if (targetService != "Sorry") {
    book(targetService, timeSlot);
  } else {
    console.log("Sorry");
  }
}

function findMaxRatingBelow(ratingCriteria) {
  targetService = "Sorry"; // default none
  let maxRating = null;

  for (const service of services) {
    if (!availableServices.includes(service["name"])) {
      continue;
    }
    const rating = service["r"];
    if (rating <= ratingCriteria) {
      if (maxRating === null) {
        maxRating = rating;
        targetService = service["name"];
      } else if (rating > maxRating) {
        maxRating = rating;
        targetService = service["name"];
      }
    }
  }

  return targetService;
}

function findMinRatingAbove(ratingCriteria) {
  targetService = "Sorry"; // default none
  let minRating = null;

  for (const service of services) {
    if (!availableServices.includes(service["name"])) {
      continue;
    }
    const rating = service["r"];
    if (rating >= ratingCriteria) {
      if (minRating === null) {
        minRating = rating;
        targetService = service["name"];
      } else if (rating < minRating) {
        minRating = rating;
        targetService = service["name"];
      }
    }
  }

  return targetService;
}

function findMaxCostBelow(ratingCriteria) {
  targetService = "Sorry"; // default none
  let maxCost = null;

  for (const service of services) {
    if (!availableServices.includes(service["name"])) {
      continue;
    }
    const cost = service["c"];
    if (cost <= ratingCriteria) {
      if (maxCost === null) {
        maxCost = cost;
        targetService = service["name"];
      } else if (cost > maxCost) {
        maxCost = cost;
        targetService = service["name"];
      }
    }
  }

  return targetService;
}

function findMinCostAbove(ratingCriteria) {
  targetService = "Sorry"; // default none
  let minCost = null;

  for (const service of services) {
    if (!availableServices.includes(service["name"])) {
      continue;
    }
    const cost = service["c"];
    if (cost >= ratingCriteria) {
      if (minCost === null) {
        minCost = cost;
        targetService = service["name"];
      } else if (cost < minCost) {
        minCost = cost;
        targetService = service["name"];
      }
    }
  }

  return targetService;
}

function findService(name) {
  targetService = "Sorry"; // default none
  for (const service in services) {
    if (!availableServices.includes(service["name"])) {
      continue;
    }
    if (name == service["name"]) {
      targetService = service["name"];
      return targetService;
    }
  }

  return targetService;
}

function checkAvailability(timeSlot) {
  availableServices = [];
  for (const [service, set] of availableSlot) {
    const isDisjoint = (set1, set2) =>
      [...set1].every((item) => !set2.has(item));

    if (isDisjoint(timeSlot, set)) {
      availableServices.push(service);
    }
  }

  return availableServices;
}

function book(service, timeSlot) {
  availableSlot.set(
    service,
    new Set([...availableSlot.get(service), ...timeSlot])
  );
  console.log(service);
}

const services = [
  { name: "S1", r: 4.5, c: 1000 },
  { name: "S2", r: 3, c: 1200 },
  { name: "S3", r: 3.8, c: 800 },
];

func2(services, 15, 17, "c>=800"); // S3
func2(services, 11, 13, "r<=4"); // S3
func2(services, 10, 12, "name=S3"); // Sorry
func2(services, 15, 18, "r>=4.5"); // S1
func2(services, 16, 18, "r>=4"); // Sorry
func2(services, 13, 17, "name=S1"); // Sorry
func2(services, 8, 9, "c<=1500"); // S2

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

// Task 4
console.log("=== Task 4 ===");

function func4(sp, stat, n) {
  //  rule: fit people into a car
  const statArr = stat.split("");

  let minAvailable = null;
  let maxAvailable = null;
  let minAvailableIndex = null;
  let maxAvailableIndex = null;

  for (let index in statArr) {
    if (stat[index] == "1") {
      continue; // skip this car since 1 means not available
    }
    if (sp[index] == n) {
      console.log(index); // perfect match, end the process
      return;
    } else if (sp[index] > n) {
      if (maxAvailable === null) {
        maxAvailable = sp[index];
        maxAvailableIndex = index;
      } else if (sp[index] < maxAvailable) {
        maxAvailable = sp[index];
        maxAvailableIndex = index;
      }
    } else if (sp[index] < n) {
      if (minAvailable === null) {
        minAvailable = sp[index];
        minAvailableIndex = index;
      } else if (sp[index] > minAvailable) {
        minAvailable = sp[index];
        minAvailableIndex = index;
      }
    }
  }

  // Answer
  if (maxAvailableIndex !== null) {
    console.log(maxAvailableIndex);
  } else if (minAvailableIndex !== null) {
    console.log(minAvailableIndex);
  } else {
    console.log("Error");
  }
}

func4([3, 1, 5, 4, 3, 2], "101000", 2); // print 5
func4([1, 0, 5, 1, 3], "10100", 4); // print 4
func4([4, 6, 5, 8], "1000", 4); // print 2
