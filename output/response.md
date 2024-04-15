~~~
## **HTML**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurant Reservation Form</title>
    <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-800 text-white">
    <div class="container mx-auto p-4">
        <h1 class="text-3xl font-bold text-center mb-6">Restaurant Reservation</h1>
        <form id="reservationForm" class="space-y-4">
            <!-- Component 1 (Restaurant Selection) -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <!-- Truffles -->
                <label class="block border border-gray-700 bg-gray-900 hover:bg-gray-700 p-4 rounded shadow">
                    <input type="radio" name="restaurant" value="Truffles" class="mr-2">
                    <img src="https://content.jdmagicbox.com/v2/comp/bangalore/a4/080pxx80.xx80.170403121558.u8a4/catalogue/truffles-kalyan-nagar-bangalore-restaurants-vtskn.jpg" alt="Truffles" class="w-full h-32 object-cover rounded">
                    <p>Burgers, sandwiches & other American bites, plus desserts, in chill surrounds with a modern vibe.</p>
                </label>
                <!-- Toast & Tonic -->
                <label class="block border border-gray-700 bg-gray-900 hover:bg-gray-700 p-4 rounded shadow">
                    <input type="radio" name="restaurant" value="Toast & Tonic" class="mr-2">
                    <img src="https://images.slurrp.com/prodarticles/h8ias9n688c.webp" alt="Toast & Tonic" class="w-full h-32 object-cover rounded">
                    <p>Casual bar serving international gastropub cuisine and mixing classic cocktails.</p>
                </label>
                <!-- Olive Beach -->
                <label class="block border border-gray-700 bg-gray-900 hover:bg-gray-700 p-4 rounded shadow">
                    <input type="radio" name="restaurant" value="Olive Beach" class="mr-2">
                    <img src="https://lh3.googleusercontent.com/a8QC8iI3QqKwPyu9ubrVEs3CDTw_6FuSL-fnLALBhyl-lj03upT6K45-BLZnZQYRQbKzG4bdNCAwCigGZp4gJ862cIJN=w1200-rw" alt="Olive Beach" class="w-full h-32 object-cover rounded">
                    <p>Contemporary Mediterranean bistro with beachy, white-walled decor & stylish furnishings.</p>
                </label>
            </div>

            <!-- Component 2 (Reservation Date Picker) -->
            <div>
                <label for="reservationDate" class="block mb-2">Reservation Date</label>
                <input type="date" id="reservationDate" name="reservationDate" class="w-full bg-gray-700 border border-gray-600 p-2 rounded">
            </div>

            <!-- Component 3 (Reservation Time Selector) -->
            <div>
                <label for="reservationTime" class="block mb-2">Reservation Time</label>
                <input type="time" id="reservationTime" name="reservationTime" class="w-full bg-gray-700 border border-gray-600 p-2 rounded">
            </div>

            <!-- Component 4 (Number of Guests Selector) -->
            <div>
                <label for="numberOfGuests" class="block mb-2">Number of Guests</label>
                <select id="numberOfGuests" name="numberOfGuests" class="w-full bg-gray-700 border border-gray-600 p-2 rounded">
                    <!-- JavaScript will populate this dropdown -->
                </select>
            </div>

            <!-- Component 5 (Special Requests Textarea) -->
            <div>
                <label for="specialRequests" class="block mb-2">Special Requests</label>
                <textarea id="specialRequests" name="specialRequests" rows="4" class="w-full bg-gray-700 border border-gray-600 p-2 rounded"></textarea>
            </div>

            <!-- Component 6 (Submit Button) -->
            <div>
                <button type="submit" class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Submit
                </button>
            </div>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

## **Javascript**
```javascript
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
```
~~~