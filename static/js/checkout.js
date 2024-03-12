
document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('.section');

    sections.forEach(function (section) {
        if (section.classList.contains('completed')) {
            var targetId = section.querySelector('.accordion-toggle').getAttribute('data-target');
            var target = document.getElementById(targetId);
            var chevron = section.querySelector('.chevron');
            target.classList.toggle('hidden');
            chevron.classList.toggle('rotate-90');
        } 
    });

    
    var toggleButtons = document.querySelectorAll('.accordion-toggle');

    toggleButtons.forEach(function (button) {
        button.addEventListener('click', toggleAccordion);
    });

   

    const forms = document.querySelectorAll(".container form");

    forms.forEach(form => {
        const inputs = form.querySelectorAll("input[required], select[required], textarea[required]");

        inputs.forEach(input => {
            input.addEventListener("blur", function () { // Validate on blur
                validateField(this);
            });
        });

        form.addEventListener("submit", function (event) {
            console.log("submit event");
            let isFormValid = true;
            inputs.forEach(input => {
                if (!validateField(input)) {
                    isFormValid = false;
                }
            });
        
            if (!isFormValid) {
                console.log("form is invalid");
                event.preventDefault();
            }
        });

    });

    function toggleAccordion() {
        var targetId = this.getAttribute('data-target');
        var target = document.getElementById(targetId);
        var chevron = this.querySelector('.chevron');
        target.classList.toggle('hidden');
        chevron.classList.toggle('rotate-90');
    }

    function validateField(field) {
        let isValid = field.checkValidity();
        console.log("field validity: " + isValid);

        if (field.type === "email" && !validateEmail(field.value)) {
            isValid = false; // Additional email validation
        } 

        toggleErrorDisplay(field, isValid);
        
        return isValid;
    }

    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    function toggleErrorDisplay(field, isValid) {
        if (!isValid) {
            field.classList.add("is-invalid");
            field.classList.add("border-red-500");
            field.nextElementSibling.classList.remove("hidden");
        } else {
            field.classList.remove("is-invalid");
            field.classList.remove("border-red-500");
            field.nextElementSibling.classList.add("hidden");
        }
    }

    
});




