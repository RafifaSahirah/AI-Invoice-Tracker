// Frontend script: handles invoice image upload, preview, and API call

// DOM Elements
const fileInput = document.getElementById('invoice-image');
const preview = document.getElementById('preview');
const emptyPreview = document.getElementById('empty-preview');
const uploadForm = document.getElementById('upload-form');

const dateElement = document.getElementById('date');
const nameElement = document.getElementById('name');
const amountElement = document.getElementById('amount');


fileInput.addEventListener('change', function (event) {
  const file = event.target.files[0];
  if (file) {
    console.log(`File Name: ${file.name}`);
    const imageUrl = URL.createObjectURL(file);
    preview.src = imageUrl;
    preview.hidden = false;
    emptyPreview.hidden = true
  };
});

uploadForm.addEventListener('submit', async function (event) {
  event.preventDefault();

  const file = fileInput.files[0];
  
  if (!file) {
    alert("Please select an invoice image first.")
    return;
  }

  const formData = new FormData();
  formData.append('file', file);
  try {
    const response = await fetch(
        'http://127.0.0.1:8000/invoice/process',
        {
        method: "POST",
        body: formData
        }
    )
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
    alert('Failed to process invoice.');
  }
});