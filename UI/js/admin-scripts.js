function removeToken() {
    localStorage.removeItem("token");
}
// removeToken();
var token = getToken();
fetchMenu();


if (token == undefined) {
    window.location.href = "index.html";
} else {

}

function fetchMenu() {
    // gets all items on the menu 
    getdata('menu', token).then(res => res.json()).then(res => {
        var ii = '';
        res.forEach((element, key) => {
            ii += `  <div class="order-item shadow">
            <div class="order-tittle">${element.item_name}</div>
            <div class="order-image order-${key}"></div>
            <div class="order-decription">${element.item_description}</div>
            <div class="order-price">${element.item_price}</div>
            <input onclick="delete_item(${element.item_id})" class="sokool-secondary-background  order-button" type="image" src="./img/close.png" alt="close">
        </div>`;
        });
        document.getElementById('menu-items').innerHTML = ii;

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
        postdata(endpoint, data, token).then(res => res.json())
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