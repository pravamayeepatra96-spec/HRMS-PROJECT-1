document.getElementById('signupForm').addEventListener('submit', function(event) {
    const password = document.getElementById('id_password').value;
    const confirmPassword = document.getElementById('id_confirm_password').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        event.preventDefault();
    }
});