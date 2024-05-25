

const mongoose = require('mongoose');

const CabinCrewSchema = new mongoose.Schema({
    CrewID: {type: Number, required: true, unique: true, default: '-'},
    Age: {type: Number, required: true},
    Aircraft_Restrictions: {type: [String], required: true, default: []},
    Assigned_Seat: {type: String, required: true, default: '-'},
    Gender: {type: String, required: true, enum: ['female', 'male', '-'], default: '-'},
    Known_Languages: {type: [String], required: true, default: []},
    MemberName: {type: String, required: true, default: '-'},
    Nationality: {type: String, required: true, default: '-'},
    Role: {type: String, required: true, enum: ['chief', 'regular', 'chef', '-'], default: '-'}
    }, {collection: 'cabin_crew'});

const CabinCrew = mongoose.model('cabin_crew', CabinCrewSchema);
module.exports = CabinCrew;