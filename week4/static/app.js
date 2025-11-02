document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const checkbox = document.getElementById("policy-agree");

  form.addEventListener("submit", (event) => {
    if (!checkbox.checked) {
      event.preventDefault(); // Policy not accepted. Prevent default form submission.
      alert("請勾選同意條款");
    }
  });
});
