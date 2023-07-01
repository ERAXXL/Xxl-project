function searchFunction() {
    var input, filter, h1, txtValue, div;
    input = document.getElementById('search');
    filter = input.value.toUpperCase();
    h1 = document.getElementsByTagName('h1');
    div = document.getElementsByClassName('first');

    for (let i = 0; i < h1.length; i++) {
        txtValue = h1[i].textContent || h1[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            h1[i].style.display = '';
            div[i].style.display = '';
        } else {
            h1[i].style.display = 'none';
            div[i].style.display = 'none';
        }
    }
}

var searchInput = document.getElementById('search');
searchInput.addEventListener('input', searchFunction);
