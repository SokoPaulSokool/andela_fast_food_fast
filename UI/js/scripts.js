try {
    document.getElementById('login_button').addEventListener('click', function() {
        openForms();
        document.getElementById("signup-form").style.display = "none";
        document.getElementById("login-form").style.display = "block";
    });
} catch (err) {}
try {
    document.getElementById('submit_button').addEventListener('click', function(e) {
        // create account
        e.preventDefault();
        openForms();
        formElements = document.getElementById("signup-form");
        var user_name = formElements.getElementsByTagName('input')[0].value;
        var email = formElements.getElementsByTagName('input')[1].value;
        var password = formElements.getElementsByTagName('input')[2].value;
        console.log(user_name);

        endpoint = 'auth/signup';
        data = {
            "account_type": "customer",
            "email": email,
            "password": password,
            "user_name": user_name
        };
        postdata(endpoint, data, '').then(res => res.json())
            .then(res => {
                if (res.message == undefined) {
                    if (res.user_name == user_name) {
                        document.getElementById('signup_message').innerHTML = "success";
                        document.getElementById("signup-form").style.display = "none";
                        document.getElementById("login-form").style.display = "block";
                    }
                } else {

                    document.getElementById('signup_message').innerHTML = res.message;
                }
            });

    });
} catch (err) {}
try {
    document.getElementById('sign_up_button').addEventListener('click', function(e) {
        e.preventDefault();
        openForms();
        document.getElementById("login-form").style.display = "none";
        document.getElementById("signup-form").style.display = "block";

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

        try {

            document.getElementById("customers-list").style.display = "flex";
            document.getElementById("menu_list").style.display = "none";
        } catch (err) {}
    });
} catch (err) {}
try {
    document.getElementById('show_my_orders').addEventListener('click', function() {
        // switch to cusomers list
        try {


            document.getElementById("customers-list").style.display = "flex";
            document.getElementById("menu_list").style.display = "none";
        } catch (err) {}
    });
} catch (err) {}


try {
    document.getElementById('menu-items').addEventListener('click', function(e) {
        // open add quantity dialog
        e.preventDefault();


        if (e.target && isInArray(e.target.classList, "edit-button")) {

            var element2 = document.getElementById("edit-dialog-view");
            element2.classList.toggle("show");
            element2.classList.toggle("hide");
        }
    });
} catch (err) {}


try {
    document.getElementById('login_now').onclick = function(e) {
        e.preventDefault();
        selection = document.getElementById("select").value;
        formElements = document.getElementById("login-form");
        var email = formElements.getElementsByTagName('input')[0].value;
        var password = formElements.getElementsByTagName('input')[1].value;
        endpoint = 'auth/login';
        data = {
            "email": email,
            "password": password
        };
        postdata(endpoint, data, '').then(res => res.json())
            .then(res => {
                if (res.access_token != undefined) {
                    storeToken(res.access_token);
                    if (res.message.includes(" has been authorised.")) {
                        if (res.account_type == "admin") {
                            window.location.href = "admin.html";
                        } else {
                            window.location.href = "orders.html";
                        }
                    }
                }
                document.getElementById('login_message').innerHTML = res.message;
                console.log(res);


            });


    };
} catch (err) {}
try {
    document.getElementById('title').onclick = function() {
        window.location.href = "index.html";
    };
} catch (err) {}

try {
    document.getElementById('show_my_orders').onclick = function() {
        // shows selected orders for customer or pending orders for admin  when my orders or  pending orders orders button is clicked
        replaceOrAddNewClass(document.getElementById("all-orders"), "show_my_orders", "hide_my_orders");
        replaceOrAddNewClass(document.getElementById("my_orders"), "hide_my_orders", "show_my_orders");

    };
} catch (err) {}
try {
    document.getElementById('show_all_orders').onclick = function() {
        // shows menu for customer or customer orders for admin  when menu or orders button is clicked
        replaceOrAddNewClass(document.getElementById("all-orders"), "hide_my_orders", "show_my_orders");
        replaceOrAddNewClass(document.getElementById("my_orders"), "show_my_orders", "hide_my_orders");
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

function replaceOrAddNewClass(element, oldClass, newClass) {
    // replaces a oldClass with newClass if exists and adds newClass if oldClass does not exist
    var classes;
    classes = element.className.split(" ");
    if (classes.indexOf(oldClass) !== -1) {
        classes[classes.indexOf(oldClass)] = newClass;
        element.className = classes.join(" ");
    } else {
        if (classes.indexOf(newClass) == -1) {
            element.className = classes.join(" ") + " " + newClass;
        }

    }
}

baseUrl = 'http://localhost:5000/api/v1/';

function postdata(endpoint, data, token) {
    return fetch(baseUrl + endpoint, {
        method: 'post',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        },
        body: JSON.stringify(data)
    });
}

function getdata(endpoint, token) {
    return fetch(baseUrl + endpoint, {
        headers: {
            'Authorization': 'Bearer ' + token
        },
        method: 'get',
    });
}

function putdata(endpoint, data, token) {
    return fetch(baseUrl + endpoint, {
        method: 'put',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        },
        body: JSON.stringify(data)
    });
}

function deletedata(endpoint, data, token) {
    return fetch(baseUrl + endpoint, {
        method: 'delete',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        },
        body: JSON.stringify(data)
    });
}

function storeToken(token) {
    if (typeof(Storage) !== "undefined") {
        // Store
        localStorage.setItem("token", token);
        return true;
        // Retrieve
        // document.getElementById("result").innerHTML = localStorage.getItem("lastname");
    } else {
        return false;
        // document.getElementById("result").innerHTML = "Sorry, your browser does not support Web Storage...";
    }
}

function getToken() {
    return localStorage.getItem("token");
}