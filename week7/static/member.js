document.querySelectorAll(".delete-button").forEach((button) => {
  button.addEventListener("click", () => {
    const messageId = button.getAttribute("message-id");
    if (confirm("確定要刪除嗎？")) {
      fetch(`/deleteMessage/${messageId}`, {
        method: "DELETE",
      }).then((response) => {
        if (response.ok) {
          window.location.href = "/member";
        }
      });
    }
  });
});

document.getElementById("search-button").addEventListener("click", async () => {
  const memberId = document.getElementById("search-id").value.trim();
  if (!isNaN(memberId)) {
    const response = await fetch(`/api/member/${memberId}`);
    if (response.ok) {
      const data = await response.json();
      const resultDiv = document.getElementById("search-result");
      if (data.data) {
        resultDiv.innerHTML = `
          <p>${data.data.name}(${data.data.email})</p>
        `;
      } else {
        resultDiv.innerHTML = `<p>無此會員</p>`;
      }
    }
  }
});
