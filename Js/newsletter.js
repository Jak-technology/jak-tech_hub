document.addEventListener("DOMContentLoaded", function() {
    const newsletterForm = document.getElementById('newsletterForm');
    const submitButton = newsletterForm.querySelector('button[type="submit"]');
    
    const loadingImage = document.createElement("img");
    loadingImage.setAttribute("src", "../../assets/loading3.gif");
    loadingImage.setAttribute("id", "loading");
    loadingImage.setAttribute("alt", "Loading");

    const overlay = document.createElement("div");
    overlay.setAttribute("id", "overlay");

    function setStyle(elId, propertyObject) {
        var el = elId;
        for (var property in propertyObject) {
            el.style[property] = propertyObject[property];
        }
    }
    setStyle(loadingImage, {
        "display": "none",
        "position": "fixed",
        "top": "50%",
        "left": "50%",
        "transform": "translate(-50%, -50%)",
        "z-index": "1001",
        "width": "90px",
        "height": "90px",
    });
    setStyle(overlay, {
        "display": "none",
        "position": "fixed",
        "top": "0",
        "left": "0",
        "width": "100%",
        "height": "100%",
        "background": "rgba(0, 0, 0, 0.5)",
        "z-index": "1000",
    })

    document.body.append(loadingImage);
    document.body.append(overlay);

    newsletterForm.addEventListener("submit", event => {
        event.preventDefault();

        loadingImage.style.display = "block";
        overlay.style.display = "block";

        const emailInput = newsletterForm.querySelector('input[type="email"]');
        const email = emailInput.value;
        const data = {
            email: email
        };

        fetch('https://jak-tech-hub.onrender.com/subscriber/create/', {
            headers: {
              "content-Type": "application/json"
            },
            mode: "cors",
            method: "POST",
            body: JSON.stringify(data)
        })
        .then(response => {
          loadingImage.style.display = "none";
          overlay.style.display = "none";
          if (response.ok) {
            event.target.reset();
            alert("Subscription successful!")
          } else {
            alert("Error! Subscription was not successful.")
          }
        })
        .catch(error => {
            loadingImage.style.display = "none";
            overlay.style.display = "none";
            console.error('Error:', error);
            alert("An error occurred. Please try again later."); // You can customize this message
        });
    });
});
