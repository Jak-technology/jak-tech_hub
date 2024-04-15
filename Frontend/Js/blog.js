document.addEventListener('DOMContentLoaded', () => {
    const cardList = document.querySelector('.card-list');

    fetch('https://jak-tech-hub.onrender.com/blog/list/', {
        mode: 'cors' 
    })
    .then(response => response.json())
    .then(data => {

        data.forEach(blogData => {
             // console.log(blogData)
            const cardElement = createCardElement(blogData);
            console.log(cardElement)
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
    developerSpan.textContent = data.author.username;

    const titleHeader = document.createElement('h3');
    titleHeader.textContent = data.title;

    const arrowDiv = document.createElement('div');
    arrowDiv.className = 'arrow';

    const cardIcon = document.createElement('i');
    cardIcon.className = 'fas fa-arrow-right card-icon';

    arrowDiv.appendChild(cardIcon);

    cardItem.appendChild(cardImage);
    cardItem.appendChild(developerSpan);
    cardItem.appendChild(titleHeader);
    cardItem.appendChild(arrowDiv);

    return cardItem;
}
