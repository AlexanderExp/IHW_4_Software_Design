function showMenu() {
    // Make a POST request to the Flask route to get the menu data
    fetch('/get_menu', {
        method: 'POST',
    })
        .then(response => response.json())
        .then(data => {
            const menuContainer = document.getElementById('menu-container');

            // Get the menu container element
            menuContainer.innerHTML = "";
            // Create a section for the menu
            const menuSection = document.createElement('section');
            menuSection.classList.add('menu-section');

            // Create a heading for the menu
            const menuHeading = document.createElement('h2');
            menuHeading.innerText = 'Menu';

            // Append the heading to the menu section
            menuSection.appendChild(menuHeading);

            // Create a grid container for the dishes
            const dishesContainer = document.createElement('div');
            dishesContainer.classList.add('dishes-container');

            // Create HTML elements for each dish in the menu data
            data.forEach(dish => {
                // Create a container div for the dish
                const dishContainer = document.createElement('div');
                dishContainer.classList.add('dish');

                // Create HTML elements for the dish details
                const nameElement = document.createElement('h3');
                nameElement.innerText = dish.name;

                const descriptionElement = document.createElement('p');
                descriptionElement.innerText = dish.description;

                const priceElement = document.createElement('p');
                priceElement.innerText = 'Price: $' + dish.price.toFixed(2);

                const quantityElement = document.createElement('p');
                quantityElement.innerText = 'Quantity available: ' + dish.quantity;

                // Create a button for ordering the dish
                const orderButton = document.createElement('button');
                orderButton.innerText = 'Order Now';
                orderButton.classList.add('order-button');
                // Add event listener to handle ordering the dish
                orderButton.addEventListener('click', () => {
                    // Call a function to add the dish to the user's current order
                    addToOrder(dish);
                });

                // Append the dish details and order button to the dish container
                dishContainer.appendChild(nameElement);
                dishContainer.appendChild(descriptionElement);
                dishContainer.appendChild(priceElement);
                dishContainer.appendChild(quantityElement);
                dishContainer.appendChild(orderButton);

                // Append the dish container to the dishes container
                dishesContainer.appendChild(dishContainer);
            });

            // Append the dishes container to the menu section
            menuSection.appendChild(dishesContainer);

            // Append the menu section to the menu container
            menuContainer.appendChild(menuSection);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function addToOrder(dish) {
    console.log('Adding dish to order:', dish);

    // Make a POST request to the server with the dish data
    fetch('/add_to_order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dish)
    })
        .then(response => {
            if (response.ok) {
                console.log('Dish added to order successfully');
                // Handle success scenario
            } else {
                console.error('Error adding dish to order:', response.statusText);
                // Handle error scenario
            }
        })
        .catch(error => {
            console.error('Error adding dish to order:', error);
            // Handle error scenario
        });
}