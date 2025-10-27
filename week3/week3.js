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
      var promotionDiv = document.querySelector(`.promotion${i + 1}`);
      const image = createImageFrom(pictures, spot);
      const textNode = document.createTextNode(spot.sname);
      promotionDiv.appendChild(image);
      promotionDiv.appendChild(textNode);
    });

    // spots for grid display
    const grid_spots = spots.filter((spot) => {
      return (4 <= spot._id) & (spot._id <= 13);
    });
    for (const spot of grid_spots) {
      console.log(spot._id, spot.sname, spot.serial);
    }
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
  console.log(image);
  return image;
}

document.addEventListener("DOMContentLoaded", () => {
  fetchData();
});
