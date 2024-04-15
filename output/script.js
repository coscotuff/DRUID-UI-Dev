document.addEventListener('DOMContentLoaded', function() {
    // Populate number of guests dropdown
    const numberOfGuestsSelect = document.getElementById('numberOfGuests');
    for (let i = 1; i <= 10; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        numberOfGuestsSelect.appendChild(option);
    }

    // Form submission event listener
    const reservationForm = document.getElementById('reservationForm');
    reservationForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(reservationForm);
        const data = {
            restaurant: formData.get('restaurant'),
            reservationDate: formData.get('reservationDate'),
            reservationTime: formData.get('reservationTime'),
            numberOfGuests: formData.get('numberOfGuests'),
            specialRequests: formData.get('specialRequests')
        };

        // Here you would typically send the data to the server
        console.log('Form Data:', data);
        alert('Reservation submitted!'); // Placeholder for actual submission logic
    });
});