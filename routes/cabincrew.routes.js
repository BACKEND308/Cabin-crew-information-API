const express = require('express');
const CabinCrew = require('../models/CabinCrew'); // Import the updated CabinCrew model

const router = express.Router();

// GET route to retrieve all cabin crew members
router.get('/', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.find();
        res.json(cabinCrew);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// GET route to retrieve a cabin crew member by ID
router.get('/:id', async (req, res) => {
    try {
        const cabinCrew = await cabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });
        res.json(cabinCrew);
    }catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// POST route to create a new cabin crew member
router.post('/', async (req, res) => {
    const cabinCrew = new CabinCrew({
        CrewID: req.body.CrewID,
        Role: req.body.Role,
        MemberName: req.body.MemberName,
        AssignedSeat: req.body.AssignedSeat
    });
    try {
        const newCabinCrew = await cabinCrew.save();
        res.status(201).json(newCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// PATCH route to update a cabin crew member's name
router.patch('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        cabinCrew.MemberName = req.body.MemberName;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// PATCH route to update a cabin crew member's role
router.patch('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        cabinCrew.Role = req.body.Role;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// PATCH route to update a cabin crew member's assigned seat
router.patch('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        cabinCrew.AssignedSeat = req.body.AssignedSeat;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// DELETE route to delete a cabin crew member by ID
router.delete('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        await cabinCrew.remove();
        res.json({ message: 'Cabin crew member deleted' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

module.exports = router;