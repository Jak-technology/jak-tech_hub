document.addEventListener('DOMContentLoaded', () => {
    function getblogID() {
        const stringID = window.location.search.substring(1);
        const params = new URLSearchParams(stringID);
        const blogID = params.get("id");
        return parseInt(blogID, 10);
    }
    blogID = getblogID();
    console.log(blogID)
    fetch(`https://jak-tech-hub.onrender.com/blog/list/${blogID}/`, {
        mode: 'cors',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.title)
        document.getElementById("blog-title").textContent = data.title;
        document.getElementById("blog-description").textContent = `"${data.description}"`;
        document.getElementById("blog-image").src = data.image;
        document.querySelector(".blog-content-text").innerHTML = data.content;
    })
    .catch(error => console.error("Error fetching data", error))
});