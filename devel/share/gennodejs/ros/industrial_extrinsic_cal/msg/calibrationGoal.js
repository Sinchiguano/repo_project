// Auto-generated. Do not edit!

// (in-package industrial_extrinsic_cal.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class calibrationGoal {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.allowable_cost_per_observation = null;
    }
    else {
      if (initObj.hasOwnProperty('allowable_cost_per_observation')) {
        this.allowable_cost_per_observation = initObj.allowable_cost_per_observation
      }
      else {
        this.allowable_cost_per_observation = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type calibrationGoal
    // Serialize message field [allowable_cost_per_observation]
    bufferOffset = _serializer.float64(obj.allowable_cost_per_observation, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type calibrationGoal
    let len;
    let data = new calibrationGoal(null);
    // Deserialize message field [allowable_cost_per_observation]
    data.allowable_cost_per_observation = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'industrial_extrinsic_cal/calibrationGoal';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '018b5c6376abafbce2c3211a0d675d06';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Define the goal
    float64 allowable_cost_per_observation
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new calibrationGoal(null);
    if (msg.allowable_cost_per_observation !== undefined) {
      resolved.allowable_cost_per_observation = msg.allowable_cost_per_observation;
    }
    else {
      resolved.allowable_cost_per_observation = 0.0
    }

    return resolved;
    }
};

module.exports = calibrationGoal;
