// Dashboard JavaScript
let currentEmployeeId = null;
let isEditing = false;

// Get CSRF token
function getCsrfToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

// Modal functions
function openModal() {
    document.getElementById('employeeModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('employeeModal').style.display = 'none';
    document.getElementById('employeeForm').reset();
    currentEmployeeId = null;
    isEditing = false;
    document.getElementById('modalTitle').textContent = 'Add Employee';
}

// Message functions
function showMessage(message, type = 'success') {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = message;
    messageDiv.className = `message ${type}`;
    messageDiv.style.display = 'block';

    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 3000);
}

// Form handling
document.getElementById('employeeForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        phone: formData.get('phone'),
        role: formData.get('role'),
        joining_date: formData.get('joining_date'),
        password: formData.get('password')
    };

    const url = isEditing ? `/update_employee/${currentEmployeeId}/` : '/add_employee/';
    const method = 'POST';

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(result => {
        console.log('Response:', result);
        if (result.success) {
            showMessage(result.message);
            closeModal();
            setTimeout(() => {
                location.reload();
            }, 1000);
        } else {
            showMessage(result.message, 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showMessage('An error occurred. Please try again.', 'error');
    });
});

// Add employee button
document.getElementById('addEmployeeBtn').addEventListener('click', function() {
    isEditing = false;
    document.getElementById('modalTitle').textContent = 'Add Employee';
    document.getElementById('password').required = true;
    openModal();
});

// Edit employee function
function editEmployee(employeeId) {
    isEditing = true;
    currentEmployeeId = employeeId;
    document.getElementById('modalTitle').textContent = 'Edit Employee';
    document.getElementById('password').required = false;

    // Find employee data from table
    const row = document.querySelector(`tr[data-id="${employeeId}"]`);
    const cells = row.querySelectorAll('td');

    document.getElementById('name').value = cells[1].textContent.trim();
    document.getElementById('email').value = cells[2].textContent.trim();
    document.getElementById('phone').value = cells[3].textContent.trim();

    // Get role from badge
    const roleBadge = cells[4].querySelector('.role-badge');
    const roleText = roleBadge.textContent.trim();
    document.getElementById('role').value = roleText;

    // Convert date format
    const dateText = cells[5].textContent.trim();
    const dateParts = dateText.split(' ');
    const monthNames = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
        'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    };
    const month = monthNames[dateParts[0]];
    const day = dateParts[1].replace(',', '').padStart(2, '0');
    const year = dateParts[2];
    const formattedDate = `${year}-${month}-${day}`;
    document.getElementById('joining_date').value = formattedDate;

    openModal();
}

// Delete employee function
function deleteEmployee(employeeId, employeeName) {
    if (confirm(`Are you sure you want to delete ${employeeName}?`)) {
        fetch(`/delete_employee/${employeeId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(result => {
            console.log('Delete Response:', result);
            if (result.success) {
                showMessage(result.message);
                setTimeout(() => {
                    location.reload();
                }, 1000);
            } else {
                showMessage(result.message, 'error');
            }
        })
        .catch(error => {
            console.error('Delete Error:', error);
            showMessage('An error occurred. Please try again.', 'error');
        });
    }
}

// Modal close events
document.querySelector('.close').addEventListener('click', closeModal);

window.addEventListener('click', function(event) {
    const modal = document.getElementById('employeeModal');
    if (event.target === modal) {
        closeModal();
    }
});

// Set default joining date to today
document.addEventListener('DOMContentLoaded', function() {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('joining_date').value = today;
});