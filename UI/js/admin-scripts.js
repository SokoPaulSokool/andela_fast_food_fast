function removeToken() {
    localStorage.removeItem("token");
}
// removeToken();
var token = getToken();
console.log(token);
fetchMenu();


if (token == undefined) {
    window.location.href = "index.html";
} else {

}

function fetchMenu() {

    getdata('menu', token).then(res => res.json()).then(res => {
        var ii = '';
        res.forEach((element, key) => {
            ii += `  <div class="order-item shadow">
            <div class="order-tittle">${element.item_name}</div>
            <div class="order-image order-${key}"></div>
            <div class="order-decription">${element.item_description}</div>
            <div class="order-price">${element.item_price}</div>
            <input class="sokool-secondary-background  order-button" type="image" src="./img/add_shopping_cart.png" alt="close">
        </div>`;
            console.log(element);
        });
        document.getElementById('menu-items').innerHTML = ii;

    });

}