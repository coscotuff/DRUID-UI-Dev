function submitPositions() {
 var xPos = document.getElementById('xPositionInput').value || '0';
 var yPos = document.getElementById('yPositionInput').value || '0';

 // Update position of indicator within posterPlaceholder div.
 var positionIndicator = document.getElementById('positionIndicator');
 if(positionIndicator) { // Check if element exists before trying to update style.
     positionIndicator.style.position = 'absolute';
     positionIndicator.style.left = `${xPos}px`;
     positionIndicator.style.top = `${yPos}px`;
 }

 console.log('Concert Name X Position:', xPos, 'pixels');
 console.log('Concert Name Y Position:', yPos, 'pixels');
}