
function toggleAccordion() {
    var targetId = this.getAttribute('data-target');
    var target = document.getElementById(targetId);
    var chevron = this.querySelector('.chevron');
    target.classList.toggle('hidden');
    chevron.classList.toggle('rotate-90');
}

function validateField(field) {
    let isValid = field.checkValidity();
    console.log(`Field: ${field.name}, isValid: ${isValid}`);
    
    if (field.type === "email" && !validateEmail(field.value)) {
        isValid = false; // Additional email validation
    } 
    
    toggleErrorDisplay(field, isValid);
    
    return isValid;
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

function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function validateForm(form) {
    let isFormValid = true;
    form.querySelectorAll("input[required], select[required], textarea[required]").forEach(input => {
        if (!validateField(input)) {
            isFormValid = false;
        }
    });

    return isFormValid;
}

function initializeFormValidation() {
    document.querySelectorAll(".container form").forEach(form => {

        form.addEventListener("input", function (event) {
            console.log("input event fired on form");
            let formIsValid = form.checkValidity();
            let nextBtn = form.querySelector("button.next-btn");
            if (formIsValid) {
                nextBtn.removeAttribute("disabled");
                nextBtn.classList.remove("bg-gray-300", "text-gray-500");
                nextBtn.classList.add("bg-purple-500", "text-white", "hover:bg-purple-700");
            } else {
                nextBtn.setAttribute("disabled", "disabled");
                nextBtn.classList.remove("bg-purple-500", "text-white", "hover:bg-purple-700");
                nextBtn.classList.add("bg-gray-300", "text-gray-500");
            }
        });


        const inputs = form.querySelectorAll("input[required], select[required], textarea[required]");

        inputs.forEach(input => {
            input.addEventListener("blur", function () {
                validateField(this);
            });
        });

        htmx.on(form, "htmx:beforeRequest", function (event) {
            if (!validateForm(this)) {
                console.log("in beforeRequest, form is invalid");
                htmx.trigger(this, 'htmx:abort');
            }
        });
        
    });
}


document.addEventListener('DOMContentLoaded', function () {

    // Initialize accordions
    const sections = document.querySelectorAll('.section');
    sections.forEach(function (section) {
        if (section.classList.contains('completed')) {
            var targetId = section.querySelector('.accordion-toggle').getAttribute('data-target');
            var target = document.getElementById(targetId);
            var chevron = section.querySelector('.chevron');
            chevron.classList.toggle('rotate-90');
            target.classList.toggle('hidden');
        } 
    });
    
    var toggleButtons = document.querySelectorAll('.accordion-toggle');

    toggleButtons.forEach(function (button) {
        button.addEventListener('click', toggleAccordion);
    });
});

htmx.onLoad(function () {
    console.log("htmx:onLoad event fired. Re-initializing form validation.");
    initializeFormValidation();

    var toggleButtons = document.querySelectorAll('.accordion-toggle');
    toggleButtons.forEach(function (button) {
        button.addEventListener('click', toggleAccordion);
    });

    // htmx.on('#checkout-form-container', 'billing-form-completed', function (e) {
    //     console.log('billing-form-completed event fired and received by #checkout-form-container');
    //     document.getElementById('shippingSectionContent').classList.remove('hidden');
    //     const button = document.getElementById('shippingSection').querySelector('.accordion-toggle');
    //     button.removeAttribute('disabled');
    //     const header = document.getElementById('shippingSectionHeader');
    //     header.querySelector('h2').classList.remove('text-gray-400');
    //     header.querySelector('h2').classList.add('text-indigo-800');
    //     header.querySelector('.chevron').classList.remove('stroke-gray-400');
    //     header.querySelector('.chevron').classList.add('stroke-violet-600', 'rotate-90');
    // });
});

