document.addEventListener("DOMContentLoaded", () => {
  const memberForm = document.getElementById("member-form");
  const checkbox = document.getElementById("policy-agree");

  memberForm.addEventListener("submit", (event) => {
    if (!checkbox.checked) {
      event.preventDefault(); // Policy not accepted. Prevent default form submission.
      alert("請勾選同意條款");
    }
  });

  const hotelForm = document.getElementById("hotel-form");
  const hotelIdInput = document.getElementById("hotel");

  hotelForm.addEventListener("submit", () => {
    event.preventDefault();

    const hotelId = Number(hotelIdInput.value);
    console.log(hotelId);
    if (Number.isInteger(hotelId) & (hotelId > 0)) {
      window.location.href = `/hotel/${hotelId}`;
    } else {
      alert("請輸入正整數");
    }
  });
});
