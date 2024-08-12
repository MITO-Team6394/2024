# Go to https://github.com/MITO-Team6394/2024/tree/main/swerve_chassis

## Overall TODOs

1. Test single-motor position closed loop control
    Create a new folder (motor_pos_closed_loop). See phoenix examples for reference.
2. Test single-motor velocity closed loop control
    Create a new folder (motor_vel_closed_loop). See phoenix examples for reference.
3. Add closed loop controllers to swerve_chassis
    Search "TODO" within the swerve_chassis folder. Complete all TODOs.
4. (Optional) Refine swerve kinematics calculations (link)[https://docs.wpilib.org/en/stable/docs/software/kinematics-and-odometry/swerve-drive-kinematics.html].
5. (Optional) Refine motor controllers (link)[] 

6. (Optional) Refine PID Control with fusedCANCoder (link)[https://v6.docs.ctr-electronics.com/en/stable/docs/api-reference/device-specific/talonfx/remote-sensors.html#fusedcancoder]

# Examples, Libraries & Documentations

FRC python examples: https://github.com/robotpy/examples
Phoenix python examples: https://github.com/CrossTheRoadElec/Phoenix6-Examples/tree/main/python
Pigeon API: https://api.ctr-electronics.com/phoenix6/release/python/autoapi/phoenix6/hardware/core/core_pigeon2/index.html#phoenix6.hardware.core.core_pigeon2.CorePigeon2
Phoenix closed loop explanation: https://v6.docs.ctr-electronics.com/en/stable/docs/api-reference/device-specific/talonfx/closed-loop-requests.html