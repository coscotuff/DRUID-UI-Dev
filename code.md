~~~
## **HTML**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meeting Scheduler</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <script src="script.js" defer></script>
</head>
<body>
    <form id="meetingSchedulerForm">
        <!-- Time Slot Dropdown -->
        <label for="timeSlot">Choose a time slot:</label>
        <select id="timeSlot" name="timeSlot"></select>

        <!-- Agenda Textarea -->
        <label for="agenda">Meeting Agenda:</label>
        <textarea id="agenda" name="agenda" rows="4" cols="50" placeholder="Enter the meeting agenda..."></textarea>

        <!-- Participants Multi-Select -->
        <label for="participants">Select Participants:</label>
        <select id="participants" name="participants" multiple></select>

        <!-- Submit Button -->
        <button type="button" id="submitBtn">Submit</button>
    </form>
</body>
</html>
```

## **CSS**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

#meetingSchedulerForm {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#meetingSchedulerForm label {
    display: block;
    margin-top: 20px;
    margin-bottom: 5px;
}

#meetingSchedulerForm select,
#meetingSchedulerForm textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box; /* So that width includes padding */
}

#meetingSchedulerForm button {
    padding: 10px 20px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

#meetingSchedulerForm button:hover {
    background-color: #4cae4c;
}
```

## **Javascript**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const timeSlots = ['10-11 AM', '11-12 PM', '12PM-1PM', '2PM-3PM', '3PM-4PM', '4PM-5PM'];
    const participants = ['Anmol', 'Sukrit', 'Rahul', 'Riya', 'Sakshi', 'Rohan'];
    const timeSlotSelect = document.getElementById('timeSlot');
    const participantsSelect = document.getElementById('participants');
    const submitBtn = document.getElementById('submitBtn');
    const agendaTextarea = document.getElementById('agenda');

    // Populate time slots dropdown
    timeSlots.forEach(function(slot) {
        const option = document.createElement('option');
        option.value = slot;
        option.textContent = slot;
        timeSlotSelect.appendChild(option);
    });

    // Populate participants multi-select
    participants.forEach(function(participant) {
        const option = document.createElement('option');
        option.value = participant;
        option.textContent = participant;
        participantsSelect.appendChild(option);
    });

    // Submit button event listener
    submitBtn.addEventListener('click', function() {
        const selectedTimeSlot = timeSlotSelect.value;
        const selectedParticipants = Array.from(participantsSelect.selectedOptions).map(option => option.value);
        const agenda = agendaTextarea.value.trim();

        // Validate form data
        if (!selectedTimeSlot) {
            alert('Please select a time slot.');
            return;
        }
        if (selectedParticipants.length === 0) {
            alert('Please select at least one participant.');
            return;
        }
        if (!agenda) {
            alert('Please enter the meeting agenda.');
            return;
        }

        // Handle form submission
        console.log('Meeting Time Slot:', selectedTimeSlot);
        console.log('Meeting Participants:', selectedParticipants);
        console.log('Meeting Agenda:', agenda);
        // Here you would typically send the data to a server or handle it as needed
    });
});
```
~~~