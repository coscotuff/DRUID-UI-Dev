~~~
File: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeatDown Concert Poster</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="poster-container">
  <div id="concert-name">BeatDown</div>
  <!-- Additional poster details can be added here -->
  <div id="concert-info">
      Open Venue Concert<br>
      Capacity: 2500 People<br>
      HSR Layout, Bengaluru<br>
      Date: October 23rd, 2024
  </div>  
</div>

<script src="script.js"></script>

</body>
</html>
```

File: `style.css`
```css
/* Global styles */
:root {
    --primary-color: #ff007f; /* Bright pink for attention-grabbing elements */
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
}

.poster-container {
    position:relative;
    background-image:url('concert-background.jpg');
    color:white;
}

#concert-name {
   position:absolute;
   top : var(--name-position-y);
   left : var(--name-position-x);
   font-size :3rem; /* Large size for the concert's name to stand out */
   color :var(--primary-color); /* Using a bright color from the root variables */
}

#concert-info{
   position:absolute;
   bottom :20px; 
   right :20px; 
}
```

File: `script.js`
```js
document.addEventListener("DOMContentLoaded", function() {

 // Positioning of the concert's name on the poster could be dynamic or based on user input.
 // For demonstration purposes and due to lack of specific x,y coordinates in request,
 // we are using CSS custom properties (variables) which can later be set dynamically if needed.

 const styleRoot = document.documentElement;

 // Default values for positioning - these would ideally come from user input or another source.
 styleRoot.style.setProperty('--name-position-x', '50px'); 
 styleRoot.style.setProperty('--name-position-y', '100px');

});
```
~~~