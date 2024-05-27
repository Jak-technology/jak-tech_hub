function getblogID() {
    const stringID = window.location.search.substring(1);
    const params = new URLSearchParams(stringID);
    const blogID = params.get("id");
    return parseInt(blogID, 10);
}

const formatDate = (dateString) => {
    const options = {year: "numeric", month: "long", day: 'numeric'};
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', options)
}


document.addEventListener('DOMContentLoaded', () => {
    blogID = getblogID();


    fetch(`https://jak-tech-hub.onrender.com/blog/list/${blogID}/`, {
        mode: 'cors',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("blog-title").textContent = data.title;
        document.getElementById("blog-description").textContent = `"${data.description}"`;
        document.getElementById("blog-image").src = data.image;
        document.querySelector(".blog-content-text").innerHTML = data.content;
        const commentsContainer = document.getElementById('comments');
        data.comments.forEach(comment => {

            const commentElement = document.createElement('div')
            commentElement.classList.add('comment');
            commentElement.innerHTML = `
            <strong>${comment.author}</strong> [${formatDate(comment.date_created)}]<br>
            <p>${comment.content}</p>
            `;
            
            commentsContainer.appendChild(commentElement);
        });
    })
    .catch(error => console.error("Error fetching data", error))


    const form = document.getElementById('comment-form');
    const loading = document.createElement("img");
    loading.setAttribute("src", "../../assets/loading3.gif");
    loading.setAttribute("id", "loading");
    loading.setAttribute("alt", "Loading");
   
    const overlay = document.createElement("div");
    overlay.setAttribute("id", "overlay");
    
    document.body.appendChild(loading);
    document.body.appendChild(overlay);

    form.addEventListener('submit', event => {
        event.preventDefault();

        loading.style.display = "block";
        overlay.style.display = "block";
        
        const formData = new FormData(form)
        const data = Object.fromEntries(formData)
        data['content'] = data['comment'];
        data['author'] = data['name'];
        delete data['comment'];
        delete data['name'];

        blogID = getblogID();

        fetch(`https://jak-tech-hub.onrender.com/blog/comments/create/${blogID}/`, {
            headers : {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            method: 'POST',
            body: JSON.stringify(data)
        })        
        .then(response => {
            loading.style.display = "none";
            overlay.style.display = "none";
            if (response.ok) {
                alert('Your comment has been submitted successfully!');
                window.location.reload();
            } else {
                alert('Error submitting comment');
            }
        })
        .catch(error => {
          loading.style.display = "none";
          overlay.style.display = "none";
          console.error("Error", error);
          alert("Error! Your comment was not successfully created.\nPlease try again")
        });
    })
});


