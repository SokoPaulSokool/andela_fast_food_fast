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
        // switch to login form
        document.getElementById("signup-form").style.display = "none";
        document.getElementById("login-form").style.display = "block";
    });
} catch (err) {}

try {
    document.getElementById('create_account_form').addEventListener('click', function() {
        // switch to signup form
        document.getElementById("login-form").style.display = "none";
        document.getElementById("signup-form").style.display = "block";
    });
} catch (err) {}

try {
    document.getElementById('show_menu').addEventListener('click', function() {
        // switch to menu list
        document.getElementById("customers-list").style.display = "none";
        document.getElementById("menu_list").style.display = "flex";
    });
} catch (err) {}
try {
    document.getElementById('show_all_orders').addEventListener('click', function() {
        // switch to customers list
        document.getElementById("customers-list").style.display = "flex";
        document.getElementById("menu_list").style.display = "none";
    });
} catch (err) {}
try {
    document.getElementById('show_my_orders').addEventListener('click', function() {
        // switch to cusomers list
        document.getElementById("customers-list").style.display = "flex";
        document.getElementById("menu_list").style.display = "none";
    });
} catch (err) {}

try {
    document.getElementById('fast-orders').addEventListener('click', function(e) {
        // open add quantity dialog

        console.log("l");
        if (e.target && isInArray(e.target.classList, "order-button")) {

            var element = document.getElementById("dialog-view");
            element.classList.toggle("show");
            element.classList.toggle("hide");
        }
    });
} catch (err) {}
try {
    document.getElementById('menu-items').addEventListener('click', function(e) {
        // open add quantity dialog


        if (e.target && isInArray(e.target.classList, "edit-button")) {

            var element2 = document.getElementById("edit-dialog-view");
            element2.classList.toggle("show");
            element2.classList.toggle("hide");
        }
    });
} catch (err) {}

try {
    document.getElementById('add-final').onclick = function() {
        // close add quantity dialog
        var element = document.getElementById("dialog-view");
        element.classList.toggle("show");
        element.classList.toggle("hide");
    };
} catch (err) {}
try {
    document.getElementById('edit-final').onclick = function(e) {
        e.preventDefault();
        // close add quantity dialog
        var element = document.getElementById("edit-dialog-view");
        element.classList.toggle("show");
        element.classList.toggle("hide");
    };
} catch (err) {}
try {
    document.getElementById('add_order').onclick = function(e) {
        e.preventDefault();
        // close add quantity dialog
        var element = document.getElementById("edit-dialog-view");
        element.classList.toggle("show");
        element.classList.toggle("hide");
    };
} catch (err) {}
try {
    document.getElementById('login_now').onclick = function() {
        selection = document.getElementById("select").value;
        if (selection == "admin") {
            window.location.href = "admin.html";
        } else {
            window.location.href = "orders.html";
        }

    };
} catch (err) {}
try {
    document.getElementById('title').onclick = function() {
        window.location.href = "index.html";
    };
} catch (err) {}

try {
    document.getElementById('show_my_orders').onclick = function() {
        // shows all menu and hides selected orders when menu button is clicked
        document.getElementById("my_orders").classList.add("show_my_orders");
        document.getElementById("my_orders").classList.replace("hide_my_orders", "show_my_orders");
        document.getElementById("all-orders").classList.add("hide_my_orders");
        document.getElementById("all-orders").classList.replace("show_my_orders", "hide_my_orders");

    };
} catch (err) {}
try {
    document.getElementById('show_all_orders').onclick = function() {
        // hides all menu and shows selected orders when orders button is clicked
        document.getElementById("my_orders").classList.add("hide_my_orders");
        document.getElementById("my_orders").classList.replace("show_my_orders", "hide_my_orders");
        document.getElementById("all-orders").classList.add("show_my_orders");
        document.getElementById("all-orders").classList.replace("hide_my_orders", "show_my_orders");
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