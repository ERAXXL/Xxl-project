var block = document.getElementById('block');
var closee = document.getElementById('closee');
var button = document.getElementById('button');

button.onclick = function(){
    block.style.display = 'flex';
};

closee.onclick = function() {
    block.style.display = 'none';
}