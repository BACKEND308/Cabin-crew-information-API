const express = require('express');
const cors = require('cors');
require('dotenv').config();
const connectMongo = require('./db/connectMongo'); // Ensure this properly sets up and exports the MongoDB connection.

const cabinCrewRoutes = require('./routes/cabincrew.routes');

const app = express();

// Middleware
app.use(cors());
app.use(express.json()); //for parsing application/json
//MongoDB connection
connectMongo();

//connect to routes
app.use('/api/cabincrew', cabinCrewRoutes);

//Define a simple route for testing, ping with 1
app.get('/', (req, res) => {
    res.send('Hello World! This is the cabin crew information API.');
});

// Define the routes
// app.use('/api/cabincrew', require('./routes/cabincrew.routes'));

//Set the port and start the server
const port=process.env.PORT || 5003;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});