const hamburger = document.querySelector('.hamburger');

hamburger.addEventListener('click', function () {
    this.classList.toggle('is-active');
});

const mobilemenu = document.querySelector('.mobilemenu');

hamburger.addEventListener('click', function () {
    mobilemenu.classList.toggle('is-open');
});