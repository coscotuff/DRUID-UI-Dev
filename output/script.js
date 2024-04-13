document.addEventListener('DOMContentLoaded', function() {
  const bandNameInput = document.getElementById('bandName');
  const concertDateInput = document.getElementById('concertDate');
  const imageUploadInput = document.getElementById('imageUpload');
  const imagePreview = document.getElementById('imagePreview');
  const textColorInput = document.getElementById('textColor');
  const colorPreview = document.getElementById('colorPreview');
  const form = document.getElementById('posterForm');

  // Prevent past dates from being selected
  const today = new Date().toISOString().split('T')[0];
  concertDateInput.setAttribute('min', today);

  // Image upload preview
  imageUploadInput.addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        imagePreview.style.backgroundImage = `url(${e.target.result})`;
      };
      reader.readAsDataURL(file);
    }
  });

  // Update color preview
  textColorInput.addEventListener('input', function() {
    colorPreview.style.backgroundColor = this.value;
  });

  // Form submission
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    // Validate inputs
    if (bandNameInput.value.trim() === '') {
      alert('Please enter the band name.');
      return;
    }
    if (!concertDateInput.value) {
      alert('Please select a concert date.');
      return;
    }
    // More validation can be added as needed

    // Form submission logic here
    console.log('Form submitted!');
    // For demonstration purposes, we'll just clear the form
    form.reset();
    imagePreview.style.backgroundImage = '';
    colorPreview.style.backgroundColor = '#ffffff';
  });
});