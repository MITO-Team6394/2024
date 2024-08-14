"""Test Script of Steer Motors"""
import wpilib
import math
import constants

from wpimath.geometry import Translation2d
from wpimath.kinematics import SwerveDrive4Kinematics
from wpimath.kinematics import ChassisSpeeds

from phoenix6 import hardware, signals, controls, configs, StatusCode


class MyRobot(wpilib.TimedRobot):
    """
    Test pos CL control
    """

    def robotInit(self):

        self.steer_motor = hardware.TalonFX(7, "*")
        self.drive_motor = hardware.TalonFX(6, "*")
        # self.encoder


        # Start at position 0, use slot 0
        self.position_voltage = controls.PositionVoltage(0).with_slot(0)
        # Start at position 0, use slot 1
        self.position_torque = controls.PositionTorqueCurrentFOC(0).with_slot(1)
        # Keep a brake request so we can disable the motor
        self.brake = controls.NeutralOut()

        XboxController = wpilib.XboxController
        self.joystick = XboxController(0)
        cfg = configs.TalonFXConfiguration()
        cfg.slot0.k_p = 3; # An error of 1 rotation results in 2.4 V output
        cfg.slot0.k_i = 0; # No output for integrated error
        cfg.slot0.k_d = 0.1; # A velocity of 1 rps results in 0.1 V output  # 0.1

        # cfg.slot0.k_v   转速
        
        # Peak output of 8 V
        cfg.voltage.peak_forward_voltage = 8
        cfg.voltage.peak_reverse_voltage = -8

        # cfg.slot1.k_p = 60; # An error of 1 rotation results in 60 A output
        # cfg.slot1.k_i = 0; # No output for integrated error
        # cfg.slot1.k_d = 6; # A velocity of 1 rps results in 6 A output
        # # Peak output of 120 A
        # cfg.torque_current.peak_forward_torque_current = 120
        # cfg.torque_current.peak_reverse_torque_current = -120

        # Retry config apply up to 5 times, report if failure
        status: StatusCode = StatusCode.STATUS_CODE_NOT_INITIALIZED
        for _ in range(0, 5):
            status = self.steer_motor.configurator.apply(cfg)
            if status.is_ok():
                break
        if not status.is_ok():
            print(f"Could not apply configs, error code: {status.name}")

        # Make sure we start at 0
        self.steer_motor.set_position(0)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # TODO: control self.steer motor to reach "angle" (angle->position closed loop)
        # Go for plus/minus 10 rotations
        desired_rotations = self.joystick.getLeftY() * 10
        if abs(desired_rotations) <= 0.1: # Joystick deadzone
            desired_rotations = 0

        if self.joystick.getLeftBumper():
            # Use position voltage
            self.steer_motor.set_control(self.position_voltage.with_position(desired_rotations))
        # elif self.joystick.getRightBumper():
        #     # Use position torque
        #     self.steer_motor.set_control(self.position_torque.with_position(desired_rotations))
        else:
            # Disable the motor instead
            self.steer_motor.set_control(self.brake)

        # TODO: control self.drive motor to reach "speed" (speed closed loop)

    
    # def 
    #     # Apply deadband
    #     if abs(x) < self.deadband_x:
    #         x = 0
    #     if abs(y) < self.deadband_y:
    #         y = 0
    #     if abs(rotation) < self.deadband_rotation:
    #         rotation = 0

    #     # Calculate velocities and angles
    #     velocity = math.hypot(x, y)
    #     angle = math.atan2(y, x) if x != 0 else 0

    #     # Limit velocity
    #     velocity = min(velocity, self.max_velocity)

    #     # Calculate motor speeds
    #     drive_speed, steer_speed = self.calculate_motor_speeds(velocity, angle)

    #     # Set motor speeds
    #     self.drive_motor.set(drive_speed)
    #     self.steer_motor.set(steer_speed)

    def testInit(self):
        pass

    def testPeriodic(self):
        pass

    # def calculate_motor_speeds(self, velocity, angle):
    #     # Calculate drive and steer motor speeds using the velocity and angle
    #     drive_speed = velocity * math.cos(angle)
    #     steer_speed = velocity * math.sin(angle)

    #     # Limit motor acceleration
    #     drive_speed = max(-self.max_acceleration, min(self.max_acceleration, drive_speed))
    #     steer_speed = max(-self.max_acceleration, min(self.max_acceleration, steer_speed))

    #     return drive_speed, steer_speed

if __name__ == "__main__":
    wpilib.run(MyRobot)