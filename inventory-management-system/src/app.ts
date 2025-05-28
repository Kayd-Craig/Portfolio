import express from 'express';
import bodyParser from 'body-parser';
import { setProductRoutes } from './routes/productRoutes';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

setProductRoutes(app);

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});