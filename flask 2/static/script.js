
document.querySelector(".contact-form").addEventListener("submit", async function(e) {
  e.preventDefault();

  const formData = new FormData(this);

  try {
    let response = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      body: formData
    });

    let result = await response.json();

    if (result.success) {
      document.getElementById("form-status").innerHTML =
        "<span style='color:green;'>Thank you! Your message has been sent.</span>";
      this.reset();
    } else {
      document.getElementById("form-status").innerHTML =
        "<span style='color:red;'>Error: " + result.message + "</span>";
    }
  } catch (error) {
    document.getElementById("form-status").innerHTML =
      "<span style='color:red;'>Something went wrong. Please try again.</span>";
  }
});

