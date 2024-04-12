~~~
## **HTML**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Schedule Meeting</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <form id="meetingForm">
        <!-- Contact Selector -->
        <label for="contactSelector">Select Contacts:</label><br/>
        <select id="contactSelector" multiple required>
            <option value="">--Please choose an option--</option> 
            <!-- Options will be populated dynamically using JS -->
        </select><br/>

        <!-- Time Slot Selector -->
        <label for="timeSlotSelector">Select Time Slot:</label><br/>
        <select id="timeSlotSelector" required>
            <!-- Options will be populated dynamically using JS -->
            </select><br/>

         <!-- Agenda Input Field -->   
         <label for='agenda'>Agenda:</label><br/>  
         <input type='text' id='agenda' name='agenda'><br/>

         <!-- Submit Button -->   
         <button type='submit' onclick= 'scheduleMeeting()'>Schedule Meeting</button>  
     </form> 
<script src = "script.js"></script>    
</body>

</html>

```

## **CSS**
```css
body {
  font-family: Arial, sans-serif;
}

#meetingForm {
  width: 300px;
  margin: auto;
}

#meetingForm label,
#meetingForm select,
#meetingForm input,
#meetingForm button {
  display: block;
  margin-bottom: 15px;
}

#contactSelector, #timeSlotSelector{
   height :100px; 
   width :250px; 
} 

input[type=text]{
   padding :10px; 
   border-radius :5px; 
} 

button[type=submit]{
   background-color:#4CAF50; 
   color :white; 
   padding :10px 20px;
   border-radius:5px;
}

button[type=submit]:hover{
    background-color:#45a049;
}
```

## **Javascript**
```javascript
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
```
~~~