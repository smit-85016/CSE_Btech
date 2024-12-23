// Example using Node.js (Express framework)
const express = require('express');
const app = express();

// Define a route
app.get('/', (req, res) => {
  res.send('Hello, this is server-side JavaScript!');
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
