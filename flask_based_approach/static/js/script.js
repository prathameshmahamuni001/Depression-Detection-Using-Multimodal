// JS to handle form submission events
document.addEventListener("DOMContentLoaded", function () {
    // Add any custom JavaScript functionality if needed
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", function () {
            const submitButton = form.querySelector("button");
            submitButton.textContent = "Predicting...";
            submitButton.disabled = true;
        });
    });
});
