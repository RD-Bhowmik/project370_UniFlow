document.addEventListener('DOMContentLoaded', function() {
    // Apply animation to event list items
    const eventItems = document.querySelectorAll('.event-item');
    eventItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.3)';
        });
        item.addEventListener('mouseleave', function() {
            this.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
        });
    });
});
