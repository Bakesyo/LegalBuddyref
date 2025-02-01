// server.js

const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON and enable CORS
app.use(express.json());
app.use(cors());

// Connect to MongoDB (use your MongoDB connection string; for local testing, ensure MongoDB is running)
mongoose.connect('mongodb://localhost:27017/legalbuddyDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Define a Mongoose schema for referrals
const referralSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  state: { type: String, required: true },
  practiceArea: { type: String, required: true },
  description: { type: String, required: true },
  submissionDate: { type: Date, default: Date.now },
  status: { type: String, default: 'Pending follow-up' },
});

const Referral = mongoose.model('Referral', referralSchema);

// API endpoint to receive referrals
app.post('/api/referrals', async (req, res) => {
  try {
    const { name, email, state, practiceArea, description } = req.body;
    if (!name || !email || !state || !practiceArea || !description) {
      return res.status(400).json({ error: 'All fields are required.' });
    }
    const newReferral = new Referral({ name, email, state, practiceArea, description });
    await newReferral.save();
    res.json({
      message: 'Thank you for your submission. A representative will contact you soon.',
    });
  } catch (error) {
    console.error('Error saving referral:', error);
    res.status(500).json({ error: 'Server error. Please try again later.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
