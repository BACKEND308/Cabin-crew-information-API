const mongoose = require('mongoose');

const cabinCrewSchema = new mongoose.Schema({
  CrewID: { type: Number, required: true, unique: true },
  Role: { type: String, required: true, enum: ['chief', 'regular', 'chef'], default: '-' },
  MemberName: { type: String, required: true, default: '-' },
  Assigned_Seat: { type: String, required: true, default: '-' },
  Age: { type: Number, required: true, default: 0 },
  Aircraft_Restrictions: { type: [String], required: true, default: [] },
  Gender: { type: String, required: true, enum: ['Female', 'Male'], default: '-' },
  Known_Languages: { type: [String], required: true, default: [] },
  Nationality: { type: String, required: true, default: '-' },
}, { collection: 'cabin_crew' });

const CabinCrew = mongoose.model('CabinCrew', cabinCrewSchema);
module.exports = CabinCrew;
