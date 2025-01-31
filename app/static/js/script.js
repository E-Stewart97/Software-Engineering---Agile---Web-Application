function confirmDelete(itemName) {
    return confirm(`Are you sure you want to delete this ${itemName}?`); // Use itemName in the message
}


// JavaScript for dynamic table updates (not fully implemented, needs adaptation)
// Example: Attach to an Add User form with id "addUserForm"

document.addEventListener('DOMContentLoaded', function () {
    const forms = ['addUserForm', 'addCustomerForm', 'addProductForm', 'addCustomerProductForm']; //add id string here

    forms.forEach(formId => {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent normal form submission

                const formData = new FormData(form);
                const url = form.action;

                fetch(url, {
                    method: 'POST',
                    body: formData,  // No need to convert to JSON for FormData
                })
                .then(response => response.text()) // Get the response text (can also use json() if sending JSON data)
                .then(data => {
                    // Update the table with the new data. 
                    // This part needs to be adapted based on your HTML structure
                    // For example, you might replace the table's innerHTML or specific rows
                    console.log(data);
                    //Example update user table:
                    const tableBody = document.querySelector('#userTable tbody'); // Get the table body
                    if (tableBody) {
                      tableBody.innerHTML = data; // Replace with the server-returned HTML
                    }
                })
                .catch(error => console.error('Error:', error)); 

                
            });
        }
    });
});

