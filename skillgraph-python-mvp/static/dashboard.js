document
.getElementById("generateBtn")
.addEventListener("click", async () => {

    const token =
      localStorage.getItem("token");

    const response =
      await fetch(
        "http://localhost:8000/rolefit",
        {
          method:"POST",
          headers:{
            "Authorization":
              `Bearer ${token}`
          }
        }
      );

    const data =
      await response.json();

    document
      .getElementById("fitScore")
      .innerHTML =
      data.role_fit + "%";

});
