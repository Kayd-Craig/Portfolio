export interface Product {
    id: string;
    name: string;
    price: number;
    quantity: number;
}

export interface ProductInput {
    name: string;
    price: number;
    quantity: number;
}