// Frontend script: handles invoice image upload, preview, and API call

// DOM Elements
const fileInput = document.getElementById('invoice-image');
const preview = document.getElementById('preview');
const emptyPreview = document.getElementById('empty-preview');
const uploadForm = document.getElementById('upload-form');
const processButton = document.getElementById('process');

const uploadMessageElement = document.getElementById('upload-message')
const statusIcon = document.getElementById('status-icon');
const statusSpinner = document.getElementById('status-spinner');
const statusElement = document.getElementById('status-text');

const dateElement = document.getElementById('date');
const referenceElement = document.getElementById('reference_number');
const nameElement = document.getElementById('name');
const amountElement = document.getElementById('amount');

// Functions
function setLoadingStatus() {
  statusIcon.hidden = true;
  statusSpinner.hidden = false;
  statusElement.textContent = "Extracting invoice using AI...";
  processButton.disabled = true;
}

function setSuccessStatus() {
  statusSpinner.hidden = true;
  statusIcon.hidden = false;
  statusIcon.textContent = "check_circle";
  statusElement.textContent = "Invoice processed successfully.";
  processButton.disabled = false;
}

function setErrorStatus() {
  statusSpinner.hidden = true;
  statusIcon.hidden = false;
  statusIcon.textContent = "error";
  statusElement.textContent = "Failed to process invoice.";
  processButton.disabled = false;
}

fileInput.addEventListener('change', function (event) {
  const file = event.target.files[0];
  if (file) {
    console.log(`File Name: ${file.name}`);
    const imageUrl = URL.createObjectURL(file);
    preview.src = imageUrl;
    preview.hidden = false;
    emptyPreview.hidden = true;
    uploadMessageElement.innerText = file.name;
  }
});

uploadForm.addEventListener('submit', async function (event) {
  event.preventDefault();

  const file = fileInput.files[0];

  if (!file) {
    alert('Please select an invoice image first.');
    return;
  }

  const formData = new FormData();
  formData.append('file', file);

  try {
    setLoadingStatus();
    const response = await fetch('http://127.0.0.1:8000/invoice/process', {
      method: 'POST',
      body: formData,
    });

    if (!response) {
      throw new Error("Failed to process invoice.");
    }

    const data = await response.json();
    // console.log(data);
    dateElement.textContent = data.invoice.date;
    referenceElement.textContent = data.invoice.reference_number;
    nameElement.textContent = data.invoice.name;
    amountElement.textContent = data.invoice.amount;
    
    setSuccessStatus();
  } catch (error) {
    console.error(error);
    setErrorStatus();
  }
});
