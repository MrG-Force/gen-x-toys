
document.addEventListener('DOMContentLoaded', function () {
    var toggleButtons = document.querySelectorAll('.accordion-toggle');

    toggleButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var targetId = button.getAttribute('data-target');
            var target = document.getElementById(targetId);
            var chevron = button.querySelector('.chevron');
            target.classList.toggle('hidden');
            chevron.classList.toggle('rotate-90');
        });
    });
});