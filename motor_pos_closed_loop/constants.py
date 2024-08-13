# SWERVE Base
CHASSIS_DATA = {
    # These current limit parameters are per-motor in the swerve modules
    "drive_continuous_current_limit": 40,
    "azimuth_continuous_current_limit": 30,
    "drive_peak_current_limit": 60,
    "azimuth_peak_current_limit": 40,

    # Talon FX motor controllers can set peak_current_duration.
    # SparkMAX motor controllers can't.
    "drive_peak_current_duration": 0.01,
    "azimuth_peak_current_duration": 0.01,

    # time in seconds for propulsion motors to ramp up to full speed
    # reference: https://codedocs.revrobotics.com/java/com/revrobotics/cansparkmax
    "open_loop_ramp_rate": 0.5,
    "closed_loop_ramp_rate": 0.5,

    # TODO: update these values   # Jim Done 
    "swerve_modules": {
        "RF": {
            "steer_id": 12, # Done
            "drive_id": 10, # Done
            "encoder_id": 21 # Done
        },
        "RB": {
            "steer_id": 7, # Done
            "drive_id": 6, # Done
            "encoder_id": 8 # Done
        },
        "LB": {
            "steer_id": 4, # Done 
            "drive_id": 3, # Done
            "encoder_id": 5 # Done
        },
        "LF": {
            "steer_id": 1, # Done
            "drive_id": 0, # Done 
            "encoder_id": 20 # Done 
        }
    },
}