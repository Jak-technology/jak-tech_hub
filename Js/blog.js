const formatDate = (dateString) => {
    const options = {year: "numeric", month: "short", day: 'numeric'};
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', options)
}


document.addEventListener('DOMContentLoaded', () => {
    const cardList = document.querySelector('.card-list');

    fetch('https://jak-tech-hub.onrender.com/blog/list/', {
        mode: 'cors' 
    })
    .then(response => response.json())
    .then(data => {

        data.forEach(blogData => {
            console.log(blogData)
            const cardElement = createCardElement(blogData);
            cardList.appendChild(cardElement);
        });
    })
    .catch(error => console.error('Error fetching data:', error));
});

function createCardElement(data) {
    const cardItem = document.createElement('a');
    cardItem.href = `../html files/inner_html/base_blog.html?id=${data.id}`;
    cardItem.className = 'card-item';

    const cardImage = document.createElement('img');
    cardImage.src = data.image;
    cardImage.alt = 'Card Image';

    const developerSpan = document.createElement('span');
    developerSpan.className = 'developer';
    developerSpan.textContent = `${data.author.first_name}`;

    const dateSpan = document.createElement('span')
    dateSpan.className = 'designer';
    dateSpan.textContent = `${formatDate(data.date_created)}`;

    const titleHeader = document.createElement('h3');
    titleHeader.textContent = data.title;

    const p = document.createElement('p');
    p.className = 'blog-p';
    p.textContent = data.description;

    const arrowDiv = document.createElement('div');
    arrowDiv.className = 'arrow';
    const cardIcon = document.createElement('i');
    cardIcon.className = 'fas fa-arrow-right card-icon';

    const read = document.createElement('p');
    read.className = 'read';
    read.textContent = '2 mins read';



    arrowDiv.appendChild(cardIcon);

    cardItem.appendChild(cardImage);
    cardItem.appendChild(developerSpan);
    cardItem.appendChild(dateSpan);
    cardItem.appendChild(titleHeader);
    cardItem.appendChild(p);
    cardItem.appendChild(arrowDiv);
    cardItem.appendChild(read);


    return cardItem;
}

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
