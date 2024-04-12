// Contacts and Free Slots Data
var contacts = ['Anmol', 'Sukrit', 'Rahul', 'Riya', 'Sakshi', 'Rohan'];
var freeSlots = ['10-11 AM', '11-12 PM','12PM-1PM','2PM-3PM','3PM-4PM','4PM-5PM'];

// Populate Contact Selector Options
contacts.forEach(function(contact) {
    var option = document.createElement('option');
    option.text = contact;
    document.getElementById('contactSelector').add(option);
});

// Populate Time Slot Selector Options
freeSlots.forEach(function(slot) {
    var option = document.createElement('option');
    option.text = slot;
    document.getElementById('timeSlotSelector').add(option);
});

function scheduleMeeting() {
  event.preventDefault();
  
  // Get Selected Contacts, Time Slot and Agenda from Form Inputs
  var selectedContactsNodeList=document.querySelectorAll('#contactSelector option:checked'); 
  var selectedContactsArray= Array.from(selectedContactsNodeList); 

  let selectedContacts=[];
  
  for(let i=0;i<selectedContactsArray.length;i++){
      selectedContacts.push(selectedContactsArray[i].value)
      }

let timeSlot=document.querySelector('#timeSlotSelector').value;

let agenda=document.querySelector('#agenda').value;

console.log("Selected Contacts:",selectedContacts,"Time Slot:",timeSlot,"Agenda",agenda);

alert("Meeting Scheduled Successfully!");

document.getElementById("meetingForm").reset();

}