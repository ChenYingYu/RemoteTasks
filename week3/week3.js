const spotsURL = "https://cwpeng.github.io/test/assignment-3-1";
const picturesURL = "https://cwpeng.github.io/test/assignment-3-2";
const picHostURL = "https://www.travel.taipei";

let spots = [];
let pictures = [];

let itemCount = 3;

document.addEventListener("DOMContentLoaded", async () => {
  setup();
  try {
    [spots, pictures] = await fetchData();
    updateUI(spots, pictures);
  } catch (error) {
    console.error(error);
  }
});

function setup() {
  let loadMoreButton = document.getElementById("load-more-button");
  loadMoreButton.addEventListener("click", () => {
    loadMore(spots, pictures);
  });
}

async function fetchData() {
  try {
    const spotsResponse = await fetch(spotsURL);
    const spotsData = await spotsResponse.json();
    spots = spotsData.rows;
    const picturesResponse = await fetch(picturesURL);
    const picturesData = await picturesResponse.json();
    pictures = picturesData.rows;
    return [spots, pictures];
  } catch (error) {
    console.log(error);
  }
}

function updateUI(spots, pictures) {
  // spots for promotion display (we using flex box here)
  const promotionSpots = spots.filter((spot) => {
    return spot._id <= 3;
  });

  promotionSpots.forEach((spot, i) => {
    let promotionDiv = document.querySelector(`.promotion${i + 1}`);
    const image = createImageFrom(pictures, spot);
    const textNode = document.createTextNode(spot.sname);
    promotionDiv.appendChild(image);
    promotionDiv.appendChild(textNode);
  });

  // spots for grid display
  loadMore(spots, pictures);
}

function loadMore(spots, pictures) {
  // spots for grid display
  let grid_spots = [];
  let counter = 0;
  for (let i = 0; i < 10; i++) {
    if (i + itemCount < spots.length) {
      grid_spots.push(spots[i + itemCount]);
    }
  }
  let gridDiv = document.querySelector(".content-grid");
  grid_spots.forEach((spot, i) => {
    let contentDiv = document.createElement("div");
    contentDiv.classList.add("content");
    let icon = document.createElement("i");
    icon.classList.add("star-icon");
    icon.textContent = "⭐";
    let p = document.createElement("p");
    p.textContent = spot.sname;
    p.classList.add("content-footer");

    const picturesURL = pictures.find(
      (picture) => picture.serial === spot.serial
    );
    const firstPicURL = picturesURL.pics?.split(".jpg").at(0) + ".jpg";
    contentDiv.style.backgroundImage = `url(${picHostURL + firstPicURL})`;
    contentDiv.appendChild(icon);
    contentDiv.appendChild(p);

    gridDiv.appendChild(contentDiv);
  });
  itemCount += 10;
}

function createImageFrom(pictures, spot) {
  const image = document.createElement("img");
  const picturesURL = pictures.find(
    (picture) => picture.serial === spot.serial
  );
  const firstPicURL = picturesURL.pics?.split(".jpg").at(0) + ".jpg";
  image.src = picHostURL + firstPicURL;
  image.alt = spot.sname;
  return image;
}
