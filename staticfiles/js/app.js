let addBtn = document.getElementById('add-item-btn');
let tbody = document.getElementById('tb-body');
let counter = 1;
let newRowCount = 0;


function updateFormFields(selectElement) {
    // let productSelect = document.getElementById('id_sale_item_formset-0-product');
    let sellingPriceInput = document.querySelector('#id_sale_item_formset-0-price');

    let xhr = new XMLHttpRequest();
    xhr.open('GET', `/sale/getproductdetails/${selectElement.value}/`, true);

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                let productDetails = JSON.parse(xhr.responseText);
                // Update form fields with the received data
                sellingPriceInput.value = productDetails.selling_price;
                // Add other fields as needed
            } else {
                console.error('Failed to retrieve product details. Status:', xhr.status);
            }
        }
    };

    xhr.send();
}




function addRowtoTable() {
    // Get the last row in the table
    let lastRow = tbody.lastElementChild;
            
    // Clone the last row, including its attributes and content
    let newRow = lastRow.cloneNode(true);

    // Update the data-id attribute to make it unique //optional choice ann
    let newRowId = parseInt(newRow.getAttribute('data-id')) + 1;
    newRow.setAttribute('data-id', newRowId);

    counter++;
    newRow.querySelector('td:first-child').textContent = counter;

    // Clear any user-entered values in the new row except for buttons
    newRow.querySelectorAll('input, select').forEach(function(input) {
        if (input.type !== 'button') {
            input.value = '';
        }
    });

    newRow.querySelector('[name="sale_item_formset-0-qty"]').value = 1;
    newRow.querySelector('[name="sale_item_formset-0-tax"]').value = 15;

    tbody.appendChild(newRow);
}


// function msgDisplay(data) {
//     alert(data.value)
// }

