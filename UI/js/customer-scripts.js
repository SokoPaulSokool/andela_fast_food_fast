var token = getToken();

fetchCustomerMenu();
get_user_order_history();
check_auth();
var selected = {};


function check_auth() {
    token = getToken();
    if (token == undefined) {
        back_home();
    } else {

    }
}

function back_home() {
    window.location.href = "index.html";
}

function select(item) {
    // adds selected item to global
    selected = item;
}



function fetchCustomerMenu() {
    // gets all items on the menu
    check_auth();
    getdata('menu', token).then(res => {
            return res.json();
        })
        .then(res => {
            var ii = '';
            if (res.msg == 'Token has expired') {
                back_home();
            } else {
                res.reverse().forEach((element, key) => {
                    ii += ` <div class="order-item shadow">
                            <div class="order-tittle">${element.item_name}</div>
                            <div class="order-image order-${key}"></div>
                            <div class="order-decription">${element.item_description}</div>
                            <div class="order-price">${element.item_price}</div>
                            <input onclick="${select(element)}" class="sokool-secondary-background  order-button" type="image" src="./img/add_shopping_cart.png" alt="close">
                            </div>`;
                });

                if (ii == "") {
                    document.getElementById('fast-orders').innerHTML = ` <div class="order-item ">
                <div class="order-tittle">No Items on menu</div></div>`;
                } else {
                    document.getElementById('fast-orders').innerHTML = ii;
                }
            }
        });
}



try {
    document.getElementById('fast-orders').addEventListener('click', function(e) {
        // open add order dialog

        if (e.target && isInArray(e.target.classList, "order-button")) {

            var element = document.getElementById("dialog-view");

            document.getElementById('d-tittle').innerHTML = selected.item_name;
            document.getElementById('d-description').innerHTML = selected.item_description;
            document.getElementById('d-price').innerHTML = selected.item_price;

            element.classList.toggle("show");
            element.classList.toggle("hide");
            document.getElementById('place_order_message').innerHTML = "";
        }
    });
} catch (err) {}



try {
    document.getElementById('add-final').addEventListener('click', function(e) {
        // places order
        e.preventDefault();
        formElements = document.getElementById("make-order-form");
        var location = formElements.getElementsByTagName('input')[0].value;

        endpoint = 'users/orders';
        data = {
            "delivery_location": location,
            "item_id": parseInt(selected.item_id)
        };
        postdata(endpoint, data, token).then(res => {
                return res.json();
            })
            .then(res => {
                if (res.message.delivery_location == location) {
                    var element = document.getElementById("dialog-view");
                    element.classList.toggle("show");
                    element.classList.toggle("hide");
                } else {
                    document.getElementById('place_order_message').innerHTML = res.message;
                }
                get_user_order_history();
            });

    });
} catch (err) {}



function get_user_order_history() {
    // Gets users order history
    check_auth();
    endpoint = 'users/orders';

    getdata(endpoint, token).then(res => {
            return res.json();
        })
        .then(res => {
            if (res.msg == 'Token has expired') {
                back_home();
            } else {
                var ii = '';
                res.reverse().forEach((element, key) => {
                    ii += `<div class="order-item shadow">
                            <div class="order-tittle">${element.item_name}</div>
                            <div class="order-image order-9"></div>
                            <div class="order-decription">${element.item_description}</div>
                            <div class="order-price">${element.item_price} UGX</div>
                            <div class="order-decription">${element.created_at}</div>
                            <div class="order-price">${element.order_status}</div>
                        <!-- <input class="sokool-secondary-background  order-button" type="image" src="./img/remove_circle_outline.png" alt="close"> -->
                        </div>`;
                });

                if (ii == "") {
                    document.getElementById('user-orders-list').innerHTML = ` <div class="order-item ">
                    <div class="order-tittle">No Orders made</div></div>`;
                } else {

                    document.getElementById('user-orders-list').innerHTML = ii;
                }
            }
        });
}


try {
    document.getElementById('show_all_orders').addEventListener('click', function() {
        // switch to customers list
        fetchCustomerMenu();
        get_user_order_history();
    });
} catch (err) {}



try {
    document.getElementById('show_my_orders').addEventListener('click', function() {
        // switch to cusomers list
        fetchCustomerMenu();
        get_user_order_history();
    });
} catch (err) {}