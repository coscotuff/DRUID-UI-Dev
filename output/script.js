document.addEventListener('DOMContentLoaded', function() {
    const reservationForm = document.getElementById('reservationForm');
    const datePicker = document.getElementById('datePicker');
    const timePicker = document.getElementById('timePicker');

    reservationForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // Validate selected restaurant
        const selectedRestaurant = document.querySelector('input[name="restaurant"]:checked');
        if (!selectedRestaurant) {
            alert('Please select a restaurant.');
            return;
        }

        // Validate name input
        const nameInput = document.getElementById('nameInput');
        if (nameInput.value.trim() === '') {
            alert('Please enter your name.');
            return;
        }

        // Validate email input
        const emailInput = document.getElementById('emailInput');
        if (emailInput.value.trim() === '' || !emailInput.checkValidity()) {
            alert('Please enter a valid email address.');
            return;
        }

        // Validate date picker
        const currentDate = new Date().toISOString().split('T')[0];
        if (datePicker.value < currentDate) {
            alert('Please select a valid reservation date.');
            return;
        }

        // Validate time picker
        // Assuming the restaurant operates from 10:00 to 22:00
        const selectedTime = timePicker.value;
        const openingTime = '10:00';
        const closingTime = '22:00';
        if (selectedTime < openingTime || selectedTime > closingTime) {
            alert('Please select a valid reservation time within operating hours (10:00 - 22:00).');
            return;
        }

        // Collect all data for submission
        const reservationData = {
            restaurant: selectedRestaurant.value,
            name: nameInput.value,
            email: emailInput.value,
            date: datePicker.value,
            time: timePicker.value,
            partySize: document.getElementById('partySize').value,
            specialRequests: document.getElementById('specialRequests').value
        };

        console.log('Reservation Data:', reservationData);
        // Here you would typically send the data to the server
        // For this example, we'll just log it to the console

        alert('Reservation submitted successfully!');
    });
});