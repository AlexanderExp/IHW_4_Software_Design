// Add event listener to the show-order-button
document.addEventListener('DOMContentLoaded', function () {
    const showOrderButton = document.getElementById('show-order-button');
    showOrderButton.addEventListener('click', () => {
        showOrderButton.style.display = "none";
        showMenuButton.style.display = "flex";
        showOrder();
    });
    const showMenuButton = document.getElementById('show-menu-button');
    showMenuButton.addEventListener('click', () => {
        showOrderButton.style.display = "flex";
        showMenuButton.style.display = "none";
        showMenu();
    });
});

function showOrder() {
// Make a POST request to the Flask route to get the menu data
    console.log("asdad");
    fetch('/get_current_user_order', {
        method: 'GET',
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.length !== 0) {
                const menuContainer = document.getElementById('menu-container');

                // Get the menu container element
                menuContainer.innerHTML = "";
                // Create a section for the menu
                const menuSection = document.createElement('section');
                menuSection.classList.add('menu-section');

                // Create a heading for the menu
                const menuHeading = document.createElement('h2');
                menuHeading.innerText = 'Your Order';

                // Append the heading to the menu section
                menuSection.appendChild(menuHeading);

                // Create a grid container for the dishes
                const dishesContainer = document.createElement('div');
                dishesContainer.classList.add('dishes-container');

                // Create HTML elements for each dish in the menu data
                data.forEach(dish => {
                    if (dish.quantity != 0) {
                        // Create a container div for the dish
                        const dishContainer = document.createElement('div');
                        dishContainer.classList.add('dish');

                        // Create HTML elements for the dish details
                        const nameElement = document.createElement('h3');
                        nameElement.innerText = dish.dish_name;

                        const priceElement = document.createElement('p');
                        priceElement.innerText = 'Price: $' + dish.price.toFixed(2);

                        const quantityElement = document.createElement('p');
                        quantityElement.innerText = 'Quantity in order: ' + dish.quantity;

                        // Create a button for ordering the dish
                        const removeButton = document.createElement('button');
                        removeButton.innerText = 'remove from order';
                        removeButton.classList.add('remove-button');
                        // Add event listener to handle ordering the dish
                        removeButton.addEventListener('click', () => {
                            // Call a function to add the dish to the user's current order
                            removeFromOrder(dish);
                        });

                        // Append the dish details and order button to the dish container
                        dishContainer.appendChild(nameElement);
                        dishContainer.appendChild(priceElement);
                        dishContainer.appendChild(quantityElement);
                        dishContainer.appendChild(removeButton);

                        // Append the dish container to the dishes container
                        dishesContainer.appendChild(dishContainer);
                    }
                });

                // Append the dishes container to the menu section
                menuSection.appendChild(dishesContainer);

                // Append the menu section to the menu container
                menuContainer.appendChild(menuSection);
            } else {
                const menuContainer = document.getElementById('menu-container');

                let emptyOrderMessage = document.createElement('div');

                emptyOrderMessage.id = "empty-order-message";
                emptyOrderMessage.classList.add("active");
                menuContainer.appendChild(emptyOrderMessage);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function removeFromOrder(dish) {
    // Make a POST request to the Flask route to get the menu data
    console.log("removeFromOrder");
    let data = {
        order_dish_id: dish.id,
    }
    fetch('/remove_from_order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.text())
        .then(result => {
            console.log(result);
            showOrder();
            // Handle the response or perform any necessary actions
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle the error
        });
}