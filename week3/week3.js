const SPOTS_URL = "https://cwpeng.github.io/test/assignment-3-1";
const PICTURES_URL = "https://cwpeng.github.io/test/assignment-3-2";
const PIC_HOST_URL = "https://www.travel.taipei";

const App = {
  loadedCount: 3,
  batchSize: 10,
};

async function fetchData() {
  try {
    const spotsResponse = await fetch(SPOTS_URL);
    const spotsData = await spotsResponse.json();
    const spots = spotsData.rows;
    const picturesResponse = await fetch(PICTURES_URL);
    const picturesData = await picturesResponse.json();
    const pictures = picturesData.rows;
    const pictureMap = new Map(pictures.map((p) => [p.serial, p]));
    return [spots, pictureMap];
  } catch (error) {
    console.log(error);
    // fall-safe return to avoid crashing
    return [[], new Map()];
  }
}

function createImageElement(pictureMap, spot) {
  const image = document.createElement("img");
  const pictureRecord = pictureMap.get(spot.serial);
  const imageFragment = pictureRecord?.pics?.split(".jpg")?.[0];
  if (imageFragment) {
    image.src = PIC_HOST_URL + imageFragment + ".jpg";
  } else {
    image.src = "";
  }

  image.alt = spot.sname;
  return image;
}

function renderUI(spots, pictureMap) {
  // clear previous UI
  if (App.contentGrid) App.contentGrid.innerHTML = "";
  // spots for promotion display (we using flex box here)
  const promotionSpots = spots.filter((spot) => {
    return spot._id <= 3;
  });

  promotionSpots.forEach((spot, i) => {
    let promotionDiv = document.querySelector(`.promotion${i + 1}`);
    if (promotionDiv) promotionDiv.innerHTML = "";

    const image = createImageElement(pictureMap, spot);
    const textNode = document.createTextNode(spot.sname);
    promotionDiv.appendChild(image);
    promotionDiv.appendChild(textNode);
  });

  // spots for grid display
  renderGridBatch(spots, pictureMap);
}

function renderGridBatch(spots, pictureMap) {
  // spots for grid display
  const gridSpots = spots.slice(
    App.loadedCount,
    App.loadedCount + App.batchSize
  );
  const fragment = document.createDocumentFragment();
  gridSpots.forEach((spot) => {
    let contentDiv = document.createElement("div");
    contentDiv.classList.add("content");
    let icon = document.createElement("i");
    icon.classList.add("star-icon");
    icon.textContent = "⭐";
    let p = document.createElement("p");
    p.textContent = spot.sname;
    p.classList.add("content-footer");

    const pictureRecord = pictureMap.get(spot.serial);
    const imageFragment = pictureRecord?.pics?.split(".jpg")?.[0];
    if (imageFragment) {
      contentDiv.style.backgroundImage = `url(${
        PIC_HOST_URL + imageFragment + ".jpg"
      })`;
    } else {
      contentDiv.style.backgroundImage = "";
    }
    contentDiv.appendChild(icon);
    contentDiv.appendChild(p);

    fragment.appendChild(contentDiv);
  });
  App.loadedCount += gridSpots.length;
  App.contentGrid.appendChild(fragment);
  App.loadMoreButton.disabled = App.loadedCount >= spots.length;
}

function setup(spots, pictureMap) {
  App.contentGrid = document.querySelector(".content-grid");
  const loadMoreButton = document.getElementById("load-more-button");
  App.loadMoreButton = loadMoreButton;
  if (!spots || spots.length === 0) {
    App.loadMoreButton.disabled = true;
    return;
  }
  loadMoreButton.addEventListener("click", () => {
    renderGridBatch(spots, pictureMap);
  });
}

document.addEventListener("DOMContentLoaded", async () => {
  try {
    const [spots, pictureMap] = await fetchData();
    setup(spots, pictureMap);
    renderUI(spots, pictureMap);
  } catch (error) {
    console.error(error);
  }
});
