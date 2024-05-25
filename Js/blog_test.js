

function getblogID() {
    const urlparams = new URLSearchParams(window.location.search);
    const blogID = urlparams.get("id");
    return parseInt(blogID);
}

const formatDate = (dateString) => {
    const options = {year: "numeric", month: "long", day: 'numeric'};
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', options)
}


document.addEventListener('DOMContentLoaded', () => {
    blogID = getblogID();
    console.log(blogID)
    fetch(`http://localhost:8000/blog/list/${blogID}/`, {
        mode: 'cors',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.title)
        console.log(data.comment)
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

    
});


const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
    e.preventDefault();

    const content = document.querySelector('textarea').value;
    const author = document.querySelector('#commentField').value;
    const email = document.querySelector('#emailField').value;
    const checkbox = document.querySelector('#checkboxId').checked;

    const data = {
        content,
        author,
        email
    };

    fetch(`http://localhost:8000/blog/comments/create/${blogID}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            alert('Comment posted successfully!');
            return response.json();
        } else {
            alert('Failed to post comment!');
            throw new Error('Failed to post comment!');
        }
     })
     .then(data => {
        // Update the comments on the page
        const commentsContainer = document.getElementById('comments-container');
        const commentHtml = `
            <div>
                <h4>${data.name}</h4>
                <p>${data.comment}</p>
            </div>
        `;
        commentsContainer.insertAdjacentHTML('beforeend', commentHtml);
     
        // Update the URL
        const newUrl = `http://127.0.0.1:5500/jak-tech_hub-dev_frontend2/Frontend/html%20files/inner_html/base_blog.html?id=${blogId}`;
        window.history.pushState({}, '', newUrl);
     })
     
     
    .catch(error => {
        alert('Error: ' + error.message);
    });
});






document.addEventListener("DOMContentLoaded", function() {
    const newsletterForm = document.getElementById('newsletterForm');

    newsletterForm.addEventListener("submit", event => {
        event.preventDefault();

        const emailInput = newsletterForm.querySelector('input[type="email"]');
        const email = emailInput.value;

        if (!email) {
            alert("Please enter your email address.");
            return;
        }

        const data = {
            email: email
        };

        fetch('https://jak-tech-hub.onrender.com/subscriber/create/', {
            headers: {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            method: "POST",
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            alert("Subscription successful!"); // You can customize this message
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An error occurred. Please try again later."); // You can customize this message
        });
    });
});
