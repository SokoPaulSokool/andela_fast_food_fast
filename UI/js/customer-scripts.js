var token = getToken();
fetchCustomerMenu();
var selected = {};


if (token == undefined) {
    window.location.href = "index.html";
} else {

}

function select(item) {
    selected = item;

}

function fetchCustomerMenu() {
    // gets all items on the menu
    getdata('menu', token).then(res => res.json()).then(res => {
        var ii = '';
        res.forEach((element, key) => {
            ii += `  <div class="order-item shadow">
            <div class="order-tittle">${element.item_name}</div>
            <div class="order-image order-${key}"></div>
            <div class="order-decription">${element.item_description}</div>
            <div class="order-price">${element.item_price}</div>
            <input onclick="${select(element)}" class="sokool-secondary-background  order-button" type="image" src="./img/add_shopping_cart.png" alt="close">
        </div>`;
        });
        document.getElementById('fast-orders').innerHTML = ii;

    });

}

try {
    document.getElementById('fast-orders').addEventListener('click', function(e) {
        // open add quantity dialog

        if (e.target && isInArray(e.target.classList, "order-button")) {

            var element = document.getElementById("dialog-view");

            document.getElementById('d-tittle').innerHTML = selected.item_name;
            document.getElementById('d-description').innerHTML = selected.item_description;
            document.getElementById('d-price').innerHTML = selected.item_price;

            element.classList.toggle("show");
            element.classList.toggle("hide");
        }
    });
} catch (err) {}

try {
    document.getElementById('add-final').addEventListener('click', function(e) {
        // adds item to menu
        e.preventDefault();
        formElements = document.getElementById("make-order-form");
        var location = formElements.getElementsByTagName('input')[0].value;

        endpoint = 'users/orders';
        data = {
            "delivery_location": location,
            "item_id": parseInt(selected.item_id)
        };
        postdata(endpoint, data, token).then(res => res.json())
            .then(res => {
                console.log(res);
                var element = document.getElementById("dialog-view");
                element.classList.toggle("show");
                element.classList.toggle("hide");


            });

    });
} catch (err) {}