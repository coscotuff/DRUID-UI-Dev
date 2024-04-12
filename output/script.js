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