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
    console.log(blogID)
    fetch(`https://jak-tech-hub.onrender.com/blog/list/${blogID}/`, {
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


const form = document.getElementById('comment-form')
    form.addEventListener('submit', event => {
        event.preventDefault();

        const formData = new FormData(form)
        const data = Object.fromEntries(formData)
        data['content'] = data['comment'];
        data['author'] = data['name'];
        delete data['comment']
        delete data['name'];

        blogID = getblogID()
        
        fetch(`https://jak-tech-hub.onrender.com/blog/comments/create/${blogID}/`, {
            headers : {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            method: 'POST',
            body: JSON.stringify(data)
        })        
        .then(response => {
            if (response.ok) {
                alert('Your comment has been submitted successfully!');
                setTimeout(function() {
                    window.location.reload();
                }, 2000);
            } else {
                alert('Error submitting comment');
            }
        })
        .catch(error => console.log("Error creating comment", error));
    })


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
