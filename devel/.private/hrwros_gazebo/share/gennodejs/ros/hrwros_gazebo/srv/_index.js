
"use strict";

let GetMaterialLocations = require('./GetMaterialLocations.js')
let SubmitTray = require('./SubmitTray.js')
let AGVControl = require('./AGVControl.js')
let PopulationControl = require('./PopulationControl.js')
let ConveyorBeltControl = require('./ConveyorBeltControl.js')
let VacuumGripperControl = require('./VacuumGripperControl.js')

module.exports = {
  GetMaterialLocations: GetMaterialLocations,
  SubmitTray: SubmitTray,
  AGVControl: AGVControl,
  PopulationControl: PopulationControl,
  ConveyorBeltControl: ConveyorBeltControl,
  VacuumGripperControl: VacuumGripperControl,
};
