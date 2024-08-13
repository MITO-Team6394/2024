import wpilib
import math
import constants

from wpimath.geometry import Translation2d
from wpimath.kinematics import SwerveDrive4Kinematics
from wpimath.kinematics import ChassisSpeeds

from phoenix6 import hardware, signals, controls

class Swerve:
    # TODO: update these values # Done (Jim Mei)
    trackwidthMeters = 0.52705
    wheelbaseMeters = 0.52705

    frontLeftLocation = Translation2d(trackwidthMeters/2, wheelbaseMeters/2)
    frontRightLocation = Translation2d(trackwidthMeters/2, -wheelbaseMeters/2)
    backLeftLocation = Translation2d(-trackwidthMeters/2, wheelbaseMeters/2)
    backRightLocation = Translation2d(-trackwidthMeters/2, -wheelbaseMeters/2)

    def __init__(self):
        module_can_ids = constants.CHASSIS_DATA["swerve_modules"]
        # frontLeft, frontRight, backLeft, backRight
        self.modules = [
            SwerveModule(module_can_ids["LF"]),
            SwerveModule(module_can_ids["RF"]),
            SwerveModule(module_can_ids["LB"]),
            SwerveModule(module_can_ids["RB"]),
        ]

        self.kinematics = SwerveDrive4Kinematics(
            self.frontLeftLocation, self.frontRightLocation, self.backLeftLocation, self.backRightLocation
        )

    def robotInit(self):
        for module in self.modules:
            module.robotInit()

    def autonomousInit(self):
        for module in self.modules:
            module.autonomousInit()

    def autonomousPeriodic(self):
        for module in self.modules:
            module.autonomousPeriodic()

    def teleopInit(self):
        for module in self.modules:
            module.teleopInit()

    def teleopPeriodic(self, x, y, rotation):
        # Example chassis speeds: 1 meter per second forward, 3 meters
        # per second to the left, and rotation at 1.5 radians per second
        # counterclockwise.
        # speeds = ChassisSpeeds(1.0, 3.0, 1.5)
        speeds = ChassisSpeeds(y, x, rotation)

        # Convert to module states
        moduleStates = self.kinematics.toSwerveModuleStates(speeds) # frontLeft, frontRight, backLeft, backRight
        for state, module in zip(moduleStates, self.modules):
            module.teleopPeriodic(state)

    def testInit(self):
        for module in self.modules:
            module.testInit()

    def testPeriodic(self):
        for module in self.modules:
            module.testPeriodic()

class SwerveModule:
    def __init__(self, drive_id, steer_id, encoder_id):
        self.drive_id = drive_id
        self.steer_id = steer_id
        self.encoder_id = encoder_id

        # Deadbanding constants
        self.deadband_x = 0.1
        self.deadband_y = 0.1
        self.deadband_rotation = 0.1

        # Velocity limiting constants
        self.max_velocity = 1.0

        # Angle limiting constants
        self.max_angle = math.pi / 2

        # Motor acceleration limiting constants
        self.max_acceleration = 0.5

    def robotInit(self):
        self.encoder.reset()
        self.gyro.reset()

        self.drive_motor = hardware.TalonFX(self.drive_id, "*")
        self.steer_motor = hardware.TalonFX(self.steer_id, "*")

        # TODO: initialize the encoders # Done
        self.drive_encoder = self.drive_id         # hardware.Encoder(self.encoder_id) speed encoder
        self.steer_encoder = self.steer_id          # .... position encoder

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self, state):
        speed = state.speed
        angle = state.angle

        # Applyu deadband
        if abs(speed) < self.deadband_x:
            speed = 0

        # TODO: control self.steer motor to reach "angle" (angle->position closed loop)
        

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