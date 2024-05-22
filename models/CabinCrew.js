const mongoose = require('mongoose');

const CabinCrewSchema = new mongoose.Schema({
    CrewID: {type: Number, required: true, unique: true, default:'-'},
    Role: {type: String, required: true, enum:['chief', 'regular', 'chef', '-'] , default:'-'},
    MemberName: {type: String, required: true, default:'-'},
    AssignedSeat:{type: String, required: true, default:'-'},
});

const CabinCrew=mongoose.model('CabinCrew', CabinCrewSchema);
module.exports=CabinCrew;