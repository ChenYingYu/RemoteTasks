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
