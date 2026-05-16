document.getElementById('loginForm').addEventListener('submit', function(event) {
    const email = document.getElementById('id_email').value.trim();
    const password = document.getElementById('id_password').value.trim();

    // Basic validation
    if (!email) {
        alert('Please enter your email address.');
        event.preventDefault();
        return;
    }

    if (!password) {
        alert('Please enter your password.');
        event.preventDefault();
        return;
    }

    // Email validation regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        event.preventDefault();
        return;
    }
});