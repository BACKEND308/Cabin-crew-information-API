const mongoose = require('mongoose');

const CabinCrewSchema = new mongoose.Schema({
    CrewID: {type: Number, required: true, unique: true, default:'-'},
    Role: {type: String, required: true, enum:['chief', 'regular', 'chef', '-'] , default:'-'},
    MemberName: {type: String, required: true, default:'-'},
    AssignedSeat:{type: String, required: true, default:'-'},
    Age: {type: Number, required: true, default:0},
    AircraftRestrictions: {type: Array, required: true, default:[]},
    Assigned_Seat: {type: String, required: true, default:'-'},
    Gender: {type:String, required: true, enum:['female', 'male', '-'], default:'-'},
    Known_Languages: {type: Array, required: true, default:[]},
    Nationality: {typr:String, required: true, default:'-'}
});

const CabinCrew=mongoose.model('CabinCrew', CabinCrewSchema);
module.exports=CabinCrew;