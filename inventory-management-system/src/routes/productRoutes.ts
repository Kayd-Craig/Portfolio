import { Router } from 'express';
import { ProductController } from '../controllers/productController';
import { Application, Request, Response } from 'express';

const router = Router();
const productController = new ProductController();

interface ProductRequestBody {
    name: string;
    price: number;
    quantity: number;
}

// List all products
router.get('/', (req: Request, res: Response) => {
    res.json(productController['products']);
});

// Get a product by ID
router.get('/:id', (req: Request<ProductParams>, res: Response) => {
    const { id } = req.params;
    const product = productController['products'].find((p: any) => p.id === id);
    if (product) {
        res.json(product);
    } else {
        res.status(404).json({ error: 'Product not found' });
    }
});

interface ProductParams {
    id: string;
}

export function setProductRoutes(app: Application): void {
    app.use('/api/products', router);

    router.post(
        '/',
        (req: Request<{}, {}, ProductRequestBody>, res: Response) => {
            const { name, price, quantity } = req.body;
            try {
                const product = productController.addProduct(name, price, quantity);
                res.status(201).json(product);
            } catch (err) {
                const errorMessage = err instanceof Error ? err.message : 'Unknown error';
                res.status(400).json({ error: errorMessage });
            }
        }
    );

    router.delete(
        '/:id',
        (req: Request<ProductParams>, res: Response) => {
            const { id } = req.params;
            try {
                const removed = productController.removeProduct(id);
                if (removed) {
                    res.status(204).send();
                } else {
                    res.status(404).json({ error: 'Product not found' });
                }
            } catch (err) {
                const errorMessage = err instanceof Error ? err.message : 'Unknown error';
                res.status(400).json({ error: errorMessage });
            }
        }
    );

    router.put(
        '/:id',
        (req: Request<ProductParams, {}, ProductRequestBody>, res: Response) => {
            const { id } = req.params;
            const { name, price, quantity } = req.body;
            if (productController) {
                try {
                    const product = productController.updateProduct(id, name, price, quantity);
                    res.status(200).json(product);
                } catch (err) {
                    const errorMessage = err instanceof Error ? err.message : 'Unknown error';
                    res.status(404).json({ error: errorMessage });
                }
            } else {
                res.status(500).json({ error: 'ProductController is not initialized.' });
            }
        }
    );
}