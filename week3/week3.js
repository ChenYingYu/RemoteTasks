const spotsURL = "https://cwpeng.github.io/test/assignment-3-1";
const picturesURL = "https://cwpeng.github.io/test/assignment-3-2";
const picHostURL = "https://www.travel.taipei";

async function fetchData() {
  try {
    const spotsResponse = await fetch(spotsURL);
    const spotsData = await spotsResponse.json();
    const spots = spotsData.rows;
    const picturesResponse = await fetch(picturesURL);
    const picturesData = await picturesResponse.json();
    const pictures = picturesData.rows;

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
    const grid_spots = spots.filter((spot) => {
      return (4 <= spot._id) & (spot._id <= 13);
    });
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

  } catch (error) {
    console.log(error);
  }
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

document.addEventListener("DOMContentLoaded", () => {
  fetchData();
});
