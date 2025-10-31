const spotsURL = "https://cwpeng.github.io/test/assignment-3-1";
const picturesURL = "https://cwpeng.github.io/test/assignment-3-2";
const picHostURL = "https://www.travel.taipei";

const App = {
  itemCount: 3,
};

document.addEventListener("DOMContentLoaded", async () => {
  try {
    const [spots, pictureMap] = await fetchData();
    setup(spots, pictureMap);
    updateUI(spots, pictureMap);
  } catch (error) {
    console.error(error);
  }
});

function setup(spots, pictureMap) {
  App.contentGrid = document.querySelector(".content-grid");
  const loadMoreButton = document.getElementById("load-more-button");
  App.loadMoreButton = loadMoreButton;
  loadMoreButton.addEventListener("click", () => {
    loadMore(spots, pictureMap);
  });
}

async function fetchData() {
  try {
    const spotsResponse = await fetch(spotsURL);
    const spotsData = await spotsResponse.json();
    const spots = spotsData.rows;
    const picturesResponse = await fetch(picturesURL);
    const picturesData = await picturesResponse.json();
    const pictures = picturesData.rows;
    const pictureMap = new Map(pictures.map((p) => [p.serial, p]));
    return [spots, pictureMap];
  } catch (error) {
    console.log(error);
  }
}

function updateUI(spots, pictureMap) {
  // spots for promotion display (we using flex box here)
  const promotionSpots = spots.filter((spot) => {
    return spot._id <= 3;
  });

  promotionSpots.forEach((spot, i) => {
    let promotionDiv = document.querySelector(`.promotion${i + 1}`);
    const image = createImageFrom(pictureMap, spot);

    const textNode = document.createTextNode(spot.sname);
    promotionDiv.appendChild(image);
    promotionDiv.appendChild(textNode);
  });

  // spots for grid display
  loadMore(spots, pictureMap);
}

function loadMore(spots, pictureMap) {
  // spots for grid display
  const grid_spots = spots.slice(App.itemCount, App.itemCount + 10);
  const fragment = document.createDocumentFragment();
  grid_spots.forEach((spot, i) => {
    let contentDiv = document.createElement("div");
    contentDiv.classList.add("content");
    let icon = document.createElement("i");
    icon.classList.add("star-icon");
    icon.textContent = "⭐";
    let p = document.createElement("p");
    p.textContent = spot.sname;
    p.classList.add("content-footer");

    const picturesObj = pictureMap.get(spot.serial);
    const firstFragment = picturesObj?.pics?.split(".jpg")?.[0];
    if (firstFragment) {
      contentDiv.style.backgroundImage = `url(${
        picHostURL + firstFragment + ".jpg"
      })`;
    } else {
      contentDiv.style.backgroundImage = "";
    }
    contentDiv.appendChild(icon);
    contentDiv.appendChild(p);

    fragment.appendChild(contentDiv);
  });
  App.itemCount += grid_spots.length;
  App.contentGrid.appendChild(fragment);
  App.loadMoreButton.disabled = App.itemCount >= spots.length;
}

function createImageFrom(pictureMap, spot) {
  const image = document.createElement("img");
  const picturesObj = pictureMap.get(spot.serial);
  const firstFragment = picturesObj?.pics?.split(".jpg")?.[0];
  if (firstFragment) {
    image.src = picHostURL + firstFragment + ".jpg";
  } else {
    image.src = "";
  }

  image.alt = spot.sname;
  return image;
}
