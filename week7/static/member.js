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

document.getElementById("update-button").addEventListener("click", async () => {
  const newName = document.getElementById("update-name").value.trim();
  if (newName) {
    const response = await fetch("/api/member", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: newName }),
    });
    const resultDiv = document.getElementById("update-result");
    if (response.ok) {
      const data = await response.json();
      if (data.ok) {
        resultDiv.innerHTML = `<p>更新成功</p>`;
        document.getElementById(
          "welcome-message"
        ).innerText = `${newName}，歡迎登入系統`;
      } else {
        resultDiv.innerHTML = `<p>更新失敗</p>`;
      }
    } else {
      resultDiv.innerHTML = `<p>更新失敗</p>`;
    }
  }
});
