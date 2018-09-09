try {
    document.getElementById('login_button').addEventListener('click', function() {
        openForms();
    });
} catch (err) {}
try {
    document.getElementById('close').addEventListener('click', function() {
        closeForms();
    });

} catch (err) {}

try {
    document.getElementById('create_account').addEventListener('click', function() {
        document.getElementById("signup-form").style.display = "none";
        document.getElementById("login-form").style.display = "block";
    });
} catch (err) {}

try {
    document.getElementById('create_account_form').addEventListener('click', function() {
        document.getElementById("login-form").style.display = "none";
        document.getElementById("signup-form").style.display = "block";
    });
} catch (err) {}
try {
    document.getElementById('fast-orders').addEventListener('click', function(e) {

        if (e.target && isInArray(e.target.classList, "order-button")) {
            var element = document.getElementById("dialog-view");
            element.classList.toggle("show");
            element.classList.toggle("hide");
        }
    });
} catch (err) {}

try {
    document.getElementById('add-final').onclick = function() {
        var element = document.getElementById("dialog-view");
        element.classList.toggle("show");
        element.classList.toggle("hide");
    };
} catch (err) {}
try {
    document.getElementById('login_now').onclick = function() {
        window.location.href = "orders.html";
    };
} catch (err) {}




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

function isInArray(array, search) {
    var found = false;
    for (var i = 0; i < array.length; i++) {
        if (array[i] == search) {
            found = true;
            return found;
        }
    }
    return found;
}