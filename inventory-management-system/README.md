# Inventory Management System

A simple RESTful API for managing an inventory of products. You can add, remove, update, and list products with details such as name, price, and quantity.

## Features

- Add new products to the inventory
- Remove existing products from the inventory
- Update product details (name, price, quantity)
- List all products in the inventory
- Retrieve a single product by ID

## Project Structure

```
inventory-management-system
├── src
│   ├── app.ts                  # Entry point of the application
│   ├── controllers
│   │   └── productController.ts # Handles product-related operations
│   ├── models
│   │   └── product.ts          # Defines the Product model
│   ├── routes
│   │   └── productRoutes.ts     # Sets up product management routes
│   └── types
│       └── index.ts            # Defines application types
├── package.json                 # npm configuration file
├── tsconfig.json                # TypeScript configuration file
└── README.md                    # Project documentation
```

## Prerequisites

- [Node.js](https://nodejs.org/) (v14 or higher recommended)
- [npm](https://www.npmjs.com/)

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   ```

2. **Navigate to the project directory:**
   ```sh
   cd inventory-management-system
   ```

3. **Install the dependencies:**
   ```sh
   npm install
   ```

## Usage

1. **Start the application:**
   ```sh
   npm start
   ```
   The server will run on [http://localhost:3000](http://localhost:3000) by default.

2. **API Endpoints:**

   - **Add a new product**
     - `POST /products`
     - **Body Example:**
       ```json
       {
         "name": "Laptop",
         "price": 999.99,
         "quantity": 10
       }
       ```
     - **Response:**
       ```json
       {
         "id": 1,
         "name": "Laptop",
         "price": 999.99,
         "quantity": 10
       }
       ```

   - **List all products**
     - `GET /products`
     - **Response:**
       ```json
       [
         {
           "id": 1,
           "name": "Laptop",
           "price": 999.99,
           "quantity": 10
         }
       ]
       ```

   - **Get a product by ID**
     - `GET /products/:id`
     - **Response:**
       ```json
       {
         "id": 1,
         "name": "Laptop",
         "price": 999.99,
         "quantity": 10
       }
       ```

   - **Update a product by ID**
     - `PUT /products/:id`
     - **Body Example:**
       ```json
       {
         "name": "Laptop Pro",
         "price": 1299.99,
         "quantity": 5
       }
       ```
     - **Response:** Updated product object

   - **Remove a product by ID**
     - `DELETE /products/:id`
     - **Response:**
       ```json
       { "message": "Product deleted successfully." }
       ```

## Example with curl

- **Add a product:**
  ```sh
  curl -X POST http://localhost:3000/products \
    -H "Content-Type: application/json" \
    -d '{"name":"Phone","price":499.99,"quantity":20}'
  ```

- **List products:**
  ```sh
  curl http://localhost:3000/products
  ```

- **Update a product:**
  ```sh
  curl -X PUT http://localhost:3000/products/1 \
    -H "Content-Type: application/json" \
    -d '{"name":"Phone X","price":599.99,"quantity":15}'
  ```

- **Delete a product:**
  ```sh
  curl -X DELETE http://localhost:3000/products/1
  ```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.