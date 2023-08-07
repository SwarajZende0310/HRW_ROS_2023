
"use strict";

let PopulationState = require('./PopulationState.js');
let Kit = require('./Kit.js');
let KitObject = require('./KitObject.js');
let VacuumGripperState = require('./VacuumGripperState.js');
let DetectedObject = require('./DetectedObject.js');
let LogicalCameraImage = require('./LogicalCameraImage.js');
let Order = require('./Order.js');
let StorageUnit = require('./StorageUnit.js');
let Model = require('./Model.js');
let TrayContents = require('./TrayContents.js');
let ConveyorBeltState = require('./ConveyorBeltState.js');
let Proximity = require('./Proximity.js');
let KitTray = require('./KitTray.js');

module.exports = {
  PopulationState: PopulationState,
  Kit: Kit,
  KitObject: KitObject,
  VacuumGripperState: VacuumGripperState,
  DetectedObject: DetectedObject,
  LogicalCameraImage: LogicalCameraImage,
  Order: Order,
  StorageUnit: StorageUnit,
  Model: Model,
  TrayContents: TrayContents,
  ConveyorBeltState: ConveyorBeltState,
  Proximity: Proximity,
  KitTray: KitTray,
};
