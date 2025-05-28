class Product {
    id: string;
    name: string;
    price: number;
    quantity: number;

    constructor(id: string, name: string, price: number, quantity: number) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
}

class ProductController {
    private products: Product[] = [];
    private nextId: number = 1;

    addProduct(name: string, price: number, quantity: number): Product {
        const product = new Product(this.nextId.toString(), name, price, quantity);
        this.products.push(product);
        this.nextId++;
        return product;
    }

    removeProduct(productId: string): boolean {
        const index = this.products.findIndex(product => product.id === productId);
        if (index !== -1) {
            this.products.splice(index, 1);
            return true;
        }
        return false;
    }

    updateProduct(productId: string, name?: string, price?: number, quantity?: number): Product | null {
        const product = this.products.find(product => product.id === productId);
        if (product) {
            if (name !== undefined) product.name = name;
            if (price !== undefined) product.price = price;
            if (quantity !== undefined) product.quantity = quantity;
            return product;
        }
        return null;
    }
}

export { ProductController, Product };