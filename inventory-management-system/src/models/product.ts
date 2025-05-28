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

    updateDetails(name?: string, price?: number, quantity?: number) {
        if (name) this.name = name;
        if (price !== undefined) this.price = price;
        if (quantity !== undefined) this.quantity = quantity;
    }
}