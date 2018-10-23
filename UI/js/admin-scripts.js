function removeToken() {
    localStorage.removeItem("token");
}
// removeToken();
var token = getToken();
fetchMenu();


if (token == undefined) {
    back_home();
} else {

}

function back_home() {
    window.location.href = "index.html";
}

function fetchMenu() {
    // gets all items on the menu 
    getdata('menu', token).then(res => {
        return res.json();
    }).then(res => {
        var ii = '';
        if (res.msg == 'Token has expired') {
            back_home();
        } else {
            res.reverse().forEach((element, key) => {
                ii += `  <div class="order-item shadow">
            <div class="order-tittle">${element.item_name}</div>
            <div class="order-image order-${key}"></div>
            <div class="order-decription">${element.item_description}</div>
            <div class="order-price">${element.item_price}</div>
            <input onclick="delete_item(${element.item_id})" class="sokool-secondary-background  order-button" type="image" src="./img/close.png" alt="close">
        </div>`;
            });


            if (ii == "") {
                document.getElementById('menu-items').innerHTML = ` <div class="order-item ">
                <div class="order-tittle">No Items On Menu</div></div>`;
            } else {

                document.getElementById('menu-items').innerHTML = ii;
            }
        }

    });

}
fetchAllOrders();

function fetchAllOrders() {
    // gets all items on the menu 
    getdata('orders', token).then(res => {
            return res.json();
        })
        .then(res => {

            var incomplete = '';
            var pending = '';
            if (res.msg == 'Token has expired') {
                back_home();
            } else {

                res.reverse().forEach((element, key) => {
                    if (element.order_status == 'incomplete') {
                        incomplete += `<div class="order-item shadow">
                <div class="order-tittle">${element.item_name}</div>
                <div class="order-image order-4"></div>
                <div class="order-decription">${element.item_description}</div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                    <h3 class="text4">Ordered by</h3>
                    <h3 class="text3">${element.user_name}</h3>
                </div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                    <h3 class="text4">At</h3>
                    <h3 class="text3">${element.created_at}</h3>
                </div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                    <h3 class="text4">Quantity</h3>
                    <h3 class="text3">1</h3>
                </div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                    <h3 class="text4">Price</h3>
                    <h3 class="text3">${element.item_price} UGX</h3>
                </div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                <h3 class="text4">Location</h3>
                <h3 class="text3">${element.delivery_location}</h3>
            </div>
                <div class="sokool-flex-row sokool-flex-space-around">
                    <div class="sokool-p-1 sokool-flex-row sokool-flex-center-vert accept">
                        <input onclick="change_status(${element.order_id},'pending')"  class="sokool-secondary-background button-small order-button sokool-m-1" type="image" src="./img/done.png" alt="accept">
                        <p>Accept</p>
                    </div>
                    <div class="sokool-p-1 sokool-flex-row sokool-flex-center-vert decline">
                        <input onclick="change_status(${element.order_id},'cancled')" class="sokool-grey-background button-small order-button sokool-m-1" type="image" src="./img/close.png" alt="accept">
                        <p>Decline</p>
                    </div>
                </div>
            </div>`;
                    }

                    if (element.order_status == 'pending') {
                        pending += `<div class="order-item shadow">
                <div class="order-tittle">${element.item_name}</div>
                <div class="order-image order-4"></div>
                <div class="order-decription">${element.item_description}</div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                    <h3 class="text4">Ordered by</h3>
                    <h3 class="text3">${element.user_name}</h3>
                </div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                    <h3 class="text4">At</h3>
                    <h3 class="text3">${element.created_at}</h3>
                </div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                    <h3 class="text4">Quantity</h3>
                    <h3 class="text3">1</h3>
                </div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                    <h3 class="text4">Price</h3>
                    <h3 class="text3">${element.item_price} UGX</h3>
                </div>
                <div class="sokool-flex-row sokool-w-100 sokool-flex-space-between">
                <h3 class="text4">Location</h3>
                <h3 class="text3">${element.delivery_location}</h3>
            </div>
            <div class="sokool-flex-row sokool-flex-space-around">
            <div class="sokool-p-1 sokool-flex-row sokool-flex-center-vert complete">
                <input onclick="change_status(${element.order_id},'complete')" class="sokool-secondary-background button-small order-button sokool-m-1" type="image" src="./img/done.png" alt="accept">
                <p>Complete Order</p>
            </div>
        </div>
            </div>`;
                    }
                });

                if (incomplete == "") {
                    document.getElementById('fast-orders').innerHTML = ` <div class="order-item ">
                <div class="order-tittle">No Orders made</div></div>`;
                } else {

                    document.getElementById('fast-orders').innerHTML = incomplete;
                }

                if (pending == "") {
                    document.getElementById('pending-list').innerHTML = ` <div class="order-item ">
                <div class="order-tittle">No pending orders</div></div>`;
                } else {

                    document.getElementById('pending-list').innerHTML = pending;
                }

            }

        });

}


function change_status(id, status) {
    endpoint = 'orders/' + parseInt(id);
    data = {
        "order_status": status
    };

    putdata(endpoint, data, token).then(res => {
            return res.json();
        })
        .then(res => {
            console.log(res);

            fetchAllOrders();
        });

}

function delete_item(id) {
    endpoint = 'menu/' + parseInt(id);
    data = {};

    deletedata(endpoint, data, token).then(res => {
            if (res.status == 200) {
                fetchMenu();
            }

        })
        .then(res => {

        });

}
try {
    document.getElementById('edit-final').onclick = function(e) {
        e.preventDefault();
        // close add quantity dialog

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
    document.getElementById('edit-final').addEventListener('click', function(e) {
        // adds item to menu
        e.preventDefault();
        formElements = document.getElementById("add-menu-form");
        var name = formElements.getElementsByTagName('input')[0].value;
        var description = formElements.getElementsByTagName('input')[1].value;
        var price = formElements.getElementsByTagName('input')[2].value;

        endpoint = 'menu';
        data = {
            "item_description": description,
            "item_name": name,
            "item_price": parseInt(price)
        };
        postdata(endpoint, data, token).then(res => {
                return res.json();
            })
            .then(res => {
                if (res.item_name == name) {
                    fetchMenu();
                    var element = document.getElementById("edit-dialog-view");
                    element.classList.toggle("show");
                    element.classList.toggle("hide");
                } else {

                    document.getElementById('add_item_message').innerHTML = res.message;
                }
                console.log(res);

            });

    });
} catch (err) {}