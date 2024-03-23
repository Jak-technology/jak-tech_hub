function getblogID() {
    const stringID = window.location.search.substring(1);
    const params = new URLSearchParams(stringID);
    const blogID = params.get("id");
    return parseInt(blogID, 10);
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
            <strong${comment.author}</strong> [${comment.date_created}]<br
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

        console.log(data)
        blogID = getblogID()
        
        fetch(`http://localhost:8000/blog/comments/create/${blogID}/`, {
            headers : {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            method: 'POST',
            body: JSON.stringify(data)
        })
        
        .then(response => response.json())
        .then(data => {
            console.log(data)
        //     const commentsContainer = document.getElementById('comment');
            // data.forEach(comment => {
        //         // create a new comment element
        //         const commentElement = document.createElement('div')
        //         commentElement.classList.add('comment');
        //         // Construct HTML for the  comment
        //         commentElement.innerHTML = `
        //         <strong${comment.author}</strong> [${comment.date_created}]<br
        //         <p>${comment.content}</p>
        //         `;
        //         // Append the comment element to the comments container
        //         commentsContainer.appendChild(commentElement);
        //     });
            
        })
        .catch(error => console.log("Error creating comment", error))
    })