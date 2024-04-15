~~~
## **HTML**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meeting Scheduler</title>
    <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 p-8">
    <div class="max-w-lg mx-auto bg-white p-6 rounded-lg shadow">
        <h1 class="text-xl font-bold mb-4">Schedule a Meeting</h1>
        <form id="meetingForm">
            <!-- Component 1 (Meeting Time Dropdown) -->
            <label for="meetingTime" class="block mb-2 text-sm font-medium text-gray-700">Meeting Time</label>
            <select id="meetingTime" class="block w-full p-2 border border-gray-300 rounded-md mb-4">
                <!-- Options will be populated by JS -->
            </select>

            <!-- Component 2 (Duration Input) -->
            <label for="duration" class="block mb-2 text-sm font-medium text-gray-700">Duration</label>
            <input type="text" id="duration" placeholder="e.g., 1 hour" class="block w-full p-2 border border-gray-300 rounded-md mb-4">

            <!-- Component 3 (Agenda Textarea) -->
            <label for="agenda" class="block mb-2 text-sm font-medium text-gray-700">Agenda</label>
            <textarea id="agenda" rows="4" class="block w-full p-2 border border-gray-300 rounded-md mb-4 resize-y"></textarea>

            <!-- Component 4 (Participants Multi-select) -->
            <label for="participants" class="block mb-2 text-sm font-medium text-gray-700">Participants</label>
            <select id="participants" multiple class="block w-full p-2 border border-gray-300 rounded-md mb-4">
                <!-- Options will be populated by JS -->
            </select>

            <!-- Component 5 (Submit Button) -->
            <button type="submit" class="w-full p-3 bg-blue-500 text-white font-medium rounded-md hover:bg-blue-600 transition duration-300">
                Submit
            </button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

## **Javascript**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Populate meeting time dropdown
    const meetingTimeSelect = document.getElementById('meetingTime');
    const freeSlots = ['10AM-11AM', '11AM-12PM', '12PM-1PM', '2PM-3PM', '3PM-4PM', '4PM-5PM'];
    freeSlots.forEach(slot => {
        const option = document.createElement('option');
        option.value = slot;
        option.textContent = slot;
        meetingTimeSelect.appendChild(option);
    });

    // Populate participants multi-select
    const participantsSelect = document.getElementById('participants');
    const contacts = ['Anmol', 'Sukrit', 'Rahul', 'Riya', 'Sakshi', 'Rohan'];
    contacts.forEach(contact => {
        const option = document.createElement('option');
        option.value = contact;
        option.textContent = contact;
        participantsSelect.appendChild(option);
    });

    // Form submission event listener
    const form = document.getElementById('meetingForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const meetingTime = meetingTimeSelect.value;
        const duration = document.getElementById('duration').value;
        const agenda = document.getElementById('agenda').value;
        const participants = Array.from(participantsSelect.selectedOptions).map(option => option.value);

        // Validate duration input
        if (!duration.match(/^(\d+)(\s)?(hour(s)?|minute(s)?|h|m)$/i)) {
            alert('Please enter a valid duration (e.g., "2 hours", "30 minutes").');
            return;
        }

        // Submit form data
        console.log('Meeting Time:', meetingTime);
        console.log('Duration:', duration);
        console.log('Agenda:', agenda);
        console.log('Participants:', participants);

        // Here you would typically handle the form submission, e.g., send data to a server
        // For this example, we'll just show an alert
        alert('Meeting scheduled successfully!');
    });
});
```
~~~