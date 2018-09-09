document.getElementById('login_button').addEventListener('click', function() {
    openForms();
});

document.getElementById('close').addEventListener('click', function() {
    closeForms();
});

function openForms() {
    // Opens view for forms
    const mq = window.matchMedia("(max-width: 620px)");
    if (mq.matches) {
        document.getElementById("all-forms").style.width = "95vw";
    } else {
        document.getElementById("all-forms").style.width = "40vw";
    }
}

function closeForms() {
    // closes view for forms
    document.getElementById("all-forms").style.width = "0";
}