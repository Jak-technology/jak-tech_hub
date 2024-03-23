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
            console.log(comment)

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
        
        fetch(`http://localhost:8000/blog/comments/create/${blogID}/`, {
            headers : {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            method: 'POST',
            body: JSON.stringify(data)
        })        
        .then(response => {
            if (response.ok) {
                console.log('Comment submitted successfully');
                alert('Your comment has been submitted successfully!');
                window.addEventListener('click', function() {
                    window.location.reload();
                });
            } else {
                console.error('Error submitting comment');
                alert('Error submitting comment');
            }
        })
        .catch(error => console.log("Error creating comment", error));
    })