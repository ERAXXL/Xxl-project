let form = document.querySelector('form');
let show = document.querySelector('.show');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    let name = document.querySelector('#name').value;
    let comment = document.querySelector('#comment');
    let sale = document.querySelector('#sale').value;
    let photo = document.querySelector('#photo');

    let shows = document.createElement('li');

    const savedItems = localStorage.getItem('shows');
    if (savedItems) {
        show.innerHTML = savedItems;
    }

    shows.innerHTML = `
    <p><strong>${name}</strong><p>
    <img src='${photo}' alt='${name}'>
    <p>${comment}</p>
    <p>Цена:  ${sale} тг</p>
    <button class="delete">Удалить</button>
    `;

    show.appendChild(shows);
    form.reset();

    localStorage.setItem('shows', show.innerHTML);

    let deleteButtons = document.querySelectorAll('.delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', () => {
            button.parentElement.remove();
            localStorage.setItem('shows', show.innerHTML);
        });
    });
});
