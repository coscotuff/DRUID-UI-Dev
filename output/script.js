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