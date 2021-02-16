function validate() {
    let username = document.getElementById('username');
    let email = document.getElementById('email');
    let password = document.getElementById('password');
    let confirmPass = document.getElementById('confirm-password');
    let companyInfo = document.getElementById('companyInfo');
    let companyNumber = document.getElementById('companyNumber');
    let isChecked = false;
    let checkbox = document.getElementById('company').addEventListener('change', (e) => {
        if (e.target.checked) {
            isChecked = true;
            companyInfo.style.display = 'block';
        } else {
            companyInfo.style.display = 'none';
        }
    });
    let submitBtn = document.getElementById('submit').addEventListener('click', (e) => {
        e.preventDefault();
        let formIsValid = true;
        if (!username.value.match(/^[a-zA-Z0-9]{3,20}$/)) {
            formIsValid = false;
            username.style.borderColor = 'red';
        } else {
            username.style.border = 'none';
        }
        if (!email.value.match(/^.*@.*\..*$/)) {
            formIsValid = false;
            email.style.borderColor = 'red';
        } else {
            email.style.border = 'none';
        }
        if (!password.value.match(/^[\w]{5,15}$/) && !confirmPass.value.match(/^[\w]{5,15}$/) || password.value != confirmPass.value) {
            formIsValid = false;
            password.style.borderColor = 'red';
            confirmPass.style.borderColor = 'red';
        } else {
            password.style.border = 'none';
            confirmPass.style.border = 'none';
        }
        if (isChecked) {
            if (!companyNumber.value.match(/^[1-9][0-9]{3}$/)) {
                companyNumber.style.borderColor = 'red';
                formIsValid = false;
            } else {
                companyNumber.style.border = 'none';
            }
        }
        let valid = document.getElementById('valid');
        if (formIsValid) {
            valid.style.display = 'block';
        } else {
            valid.style.display = 'none';
        }
    });
}