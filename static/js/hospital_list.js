document.addEventListener('DOMContentLoaded', function() {
    // Apply animation to hospital list items
    const hospitalItems = document.querySelectorAll('.hospital-item');
    hospitalItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
        item.classList.add('fade-in');
    });
});
