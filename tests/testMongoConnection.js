const connectMongo = require('../db/connectMongo');

const testConnection = async () => {
  await connectMongo();
  console.log('MongoDB connection test completed.');
};

testConnection();
