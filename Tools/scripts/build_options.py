'''
Provide structured data understood by the CustomBuild server app.py

AP_FLAKE8_CLEAN

'''


class Feature:
    '''defines a feature which can be built into the firmware, along with
    its dependencies'''
    def __init__(self,
                 category,
                 label,
                 define,
                 description,
                 default,
                 dependency):
        self.category = category
        self.label = label
        self.define = define
        self.description = description
        self.default = default
        self.dependency = dependency

    def config_option(self):
        '''the name of the configure option to be used by waf'''
        return "enable-" + self.label.replace(" ", "-")


# list of build options to offer NOTE: the dependencies must be
# written as a single string with commas and no spaces,
# eg. 'dependency1,dependency2'
BUILD_OPTIONS = [
    Feature('AHRS', 'navekf3', 'HAL_NAVEKF3_AVAILABLE', 'Enable EKF3', 1, None),
    Feature('AHRS', 'navekf2', 'HAL_NAVEKF2_AVAILABLE', 'Enable EKF2', 0, None),
    Feature('AHRS', 'external-ahrs', 'AP_EXTERNAL_AHRS_ENABLED', 'Enable External AHRS', 0, None),
    Feature('AHRS', 'external-ahrs-microstrain5', 'AP_EXTERNAL_AHRS_MICROSTRAIN5_ENABLED', 'Enable MICROSTRAIN 5-series external AHRS', 0, "external-ahrs"),  # noqa: E501
    Feature('AHRS', 'external-ahrs-microstrain7', 'AP_EXTERNAL_AHRS_MICROSTRAIN7_ENABLED', 'Enable MICROSTRAIN 7-series external AHRS', 0, "external-ahrs"),  # noqa: E501
    Feature('AHRS', 'external-ahrs-vectornav', 'AP_EXTERNAL_AHRS_VECTORNAV_ENABLED', 'Enable VectorNav external AHRS', 0, "external-ahrs"),  # noqa
    Feature('AHRS', 'external-ahrs-inertiallabs', 'AP_EXTERNAL_AHRS_INERTIALLABS_ENABLED', 'Enable InertialLabs external AHRS', 0, "external-ahrs"),  # noqa
    Feature('AHRS', 'external-ahrs-sbg', 'AP_EXTERNAL_AHRS_SBG_ENABLED', 'Enable SBG external AHRS', 0, "external-ahrs"),
    Feature('AHRS', 'visualodom', 'HAL_VISUALODOM_ENABLED', 'Enable Visual Odometry', 0, None),
    Feature('AHRS', 'ek3-feature-external-nav', 'EK3_FEATURE_EXTERNAL_NAV', 'Enable External navigation for EKF3', 0, 'navekf3'),  # noqa: E501
    Feature('AHRS', 'ek3-feature-drag-fusion', 'EK3_FEATURE_DRAG_FUSION', 'Enable Wind estimation for EKF3', 0, 'navekf3'),
    Feature('AHRS', 'ek3-feature-optflow-fusion', 'EK3_FEATURE_OPTFLOW_FUSION', 'Enable OpticalFlow fusion for EKF3', 0, 'navekf3,opticalflow'),  # noqa: E501
    Feature('AHRS', 'ek3-feature-optflow-srtm', 'EK3_FEATURE_OPTFLOW_SRTM', 'Enable OpticalFlow using SRTM for EKF3', 0, 'ek3-feature-optflow-fusion'),  # noqa: E501
    Feature('AHRS', 'baro-wind-comp', 'HAL_BARO_WIND_COMP_ENABLED', 'Enable Baro wind compensation', 0, None),

    Feature('Safety', 'parachute', 'HAL_PARACHUTE_ENABLED', 'Enable Parachute', 0, None),
    Feature('Safety', 'fence', 'AP_FENCE_ENABLED', 'Enable Geofences', 2, None),
    Feature('Safety', 'rally', 'HAL_RALLY_ENABLED', 'Enable Rally points', 0, None),  # noqa
    Feature('Safety', 'avoidance', 'AP_AVOIDANCE_ENABLED', 'Enable Object Avoidance', 0, 'fence'),
    Feature('Safety', 'oapathplanner', 'AP_OAPATHPLANNER_ENABLED', 'Enable Object Avoidance Path Planner', 0, 'fence'),

    Feature('Battery', 'battery-fuelflow', 'AP_BATTERY_FUELFLOW_ENABLED', 'Enable Fuel flow battery monitor', 0, None),
    Feature('Battery', 'battery-fuellevel-pwm', 'AP_BATTERY_FUELLEVEL_PWM_ENABLED', 'Enable PWM Fuel level battery monitor', 0, None),  # noqa: E501
    Feature('Battery', 'battery-fuellevel-analog', 'AP_BATTERY_FUELLEVEL_ANALOG_ENABLED', 'Enable Analog Fuel level battry monitor', 0, None),  # noqa: E501
    Feature('Battery', 'battery-smbus', 'AP_BATTERY_SMBUS_ENABLED', 'Enable SMBUS battery monitor', 0, None),
    Feature('Battery', 'battery-ina2xx', 'AP_BATTERY_INA2XX_ENABLED', 'Enable INA2XX battery monitor', 0, None),
    Feature('Battery', 'battery-ina3221', 'AP_BATTERY_INA3221_ENABLED', 'Enable INA3221 battery monitor', 0, None),
    Feature('Battery', 'battery-synthetic-current', 'AP_BATTERY_SYNTHETIC_CURRENT_ENABLED', 'Enable Synthetic Current monitor', 0, None), # noqa: E501
    Feature('Battery', 'battery-esc-telem-outbound', 'AP_BATTERY_ESC_TELEM_OUTBOUND_ENABLED', 'Enable Ability to put battery monitor data into ESC telem stream', 0, None), # noqa: E501
    Feature('Battery', 'battery-sum', 'AP_BATTERY_SUM_ENABLED', 'Enable Synthetic sum-of-other-batteries backend', 0, None), # noqa: E501
    Feature('Battery', 'battery-watt-max', 'AP_BATTERY_WATT_MAX_ENABLED', 'Enable BATT_WATT_MAX parameter', 0, None), # noqa: E501


    Feature('Ident', 'adsb', 'HAL_ADSB_ENABLED', 'Enable ADSB', 0, None),
    Feature('Ident', 'adsb-sagetech', 'HAL_ADSB_SAGETECH_ENABLED', 'Enable Sagetech ADSB', 0, 'adsb'),
    Feature('Ident', 'adsb-sagetech-mxs', 'HAL_ADSB_SAGETECH_MXS_ENABLED', 'Enable Sagetech MXS ADSB', 0, 'adsb'),
    Feature('Ident', 'adsb-uavionix-mavlink', 'HAL_ADSB_UAVIONIX_MAVLINK_ENABLED', 'Enable UAvionix ADSB', 0, 'adsb'),
    Feature('Ident', 'adsb-ucp', 'HAL_ADSB_UCP_ENABLED', 'Enable uAvionix UCP ADSB', 0 , 'adsb'),
    Feature('Ident', 'ais', 'AP_AIS_ENABLED', 'Enable AIS', 0, None),
    Feature('Ident', 'opendroneid', 'AP_OPENDRONEID_ENABLED', 'Enable OpenDroneID (Remote ID)', 0, None),

    Feature('Telemetry', 'crsf-telem', 'HAL_CRSF_TELEM_ENABLED', 'Enable CRSF telemetry', 0, 'frsky-sport-passthrough,frsky-telem,frsky-sport-telem,rcprotocol-crsf'),  # noqa
    Feature('Telemetry', 'crsf-telem-text-selection', 'HAL_CRSF_TELEM_TEXT_SELECTION_ENABLED', 'Enable CRSF text param selection', 0, 'crsf-telem,osd-param,frsky-sport-passthrough,frsky-telem,frsky-sport-telem'),  # NOQA: E501
    Feature('Telemetry', 'crsf-scripting', 'AP_CRSF_SCRIPTING_ENABLED', 'Enable CRSF Menu Scripting', 0, 'crsf-telem-text-selection,scripting,crsf-telem,osd-param,frsky-sport-passthrough,frsky-telem,frsky-sport-telem'),  # noqa
    Feature('Telemetry', 'hott-telem', 'HAL_HOTT_TELEM_ENABLED', 'Enable HOTT telemetry', 0, None),
    Feature('Telemetry', 'spektrum-telem', 'HAL_SPEKTRUM_TELEM_ENABLED', 'Enable Spektrum telemetry', 0, None),
    Feature('Telemetry', 'ltm-telem', 'AP_LTM_TELEM_ENABLED', 'Enable LTM telemetry', 0, None),
    Feature('Telemetry', 'rc-channel-aux-function-strings', 'AP_RC_CHANNEL_AUX_FUNCTION_STRINGS_ENABLED', 'Enable Auxiliary function activation text messages', 0, None),  # noqa
    Feature('Telemetry', 'frsky-telem', 'AP_FRSKY_TELEM_ENABLED', 'Enable FrSky telemetry', 0, None),
    Feature('Telemetry', 'frsky-d-telem', 'AP_FRSKY_D_TELEM_ENABLED', 'Enable FrSkyD telemetry', 0, 'frsky-telem'),
    Feature('Telemetry', 'frsky-sport-telem', 'AP_FRSKY_SPORT_TELEM_ENABLED', 'Enable FrSkySPort telemetry', 0, 'frsky-telem'),  # noqa
    Feature('Telemetry', 'frsky-sport-passthrough', 'AP_FRSKY_SPORT_PASSTHROUGH_ENABLED', 'Enable FrSkySPort pass-through telemetry', 0, 'frsky-sport-telem,frsky-telem'),  # noqa
    Feature('Telemetry', 'with-frsky-telem-bidirectional', 'HAL_WITH_FRSKY_TELEM_BIDIRECTIONAL', 'Enable bidirectional FrSky telemetry', 0, 'frsky-sport-telem'),  # noqa
    Feature('Telemetry', 'ghst-telem', 'AP_GHST_TELEM_ENABLED', 'Enable Ghost telemetry', 0, "rcprotocol-ghst"), # noqa
    Feature('Telemetry', 'ibus-telem', 'AP_IBUS_TELEM_ENABLED', 'Enable i-BUS telemetry', 0, None),

    Feature('Notify', 'notify-mavlink-play-tune-support', 'AP_NOTIFY_MAVLINK_PLAY_TUNE_SUPPORT_ENABLED', 'Enable MAVLink Play Tune command', 0, None),  # noqa
    Feature('Notify', 'notify-tonealarm', 'AP_NOTIFY_TONEALARM_ENABLED', 'Enable PWM tone alarm', 0, None),  # noqa
    Feature('Notify', 'notify-mavlink-led-control-support', 'AP_NOTIFY_MAVLINK_LED_CONTROL_SUPPORT_ENABLED', 'Enable MAVLink LED control', 0, None),  # noqa
    Feature('Notify', 'notify-ncp5623', 'AP_NOTIFY_NCP5623_ENABLED', 'Enable NCP5623 LED', 0, None),  # noqa
    # Feature('Notify', 'notify-pca9685', 'AP_NOTIFY_PCA9685_ENABLED', 'Enable PCA9685 LED', 0, None),  # noqa  linux-only
    Feature('Notify', 'notify-profiled', 'AP_NOTIFY_PROFILED_ENABLED', 'Enable ProfiLED', 0, None),  # noqa
    Feature('Notify', 'display', 'HAL_DISPLAY_ENABLED', 'Enable I2C Displays', 0, None),
    Feature('Notify', 'notify-profiled-spi', 'AP_NOTIFY_PROFILED_SPI_ENABLED', 'Enable ProfiLED (SPI)', 0, None),  # noqa
    Feature('Notify', 'notify-neopixel', 'AP_NOTIFY_NEOPIXEL_ENABLED', 'Enable NeoPixel LED strings', 0, None),  # noqa

    Feature('MSP', 'msp', 'HAL_MSP_ENABLED', 'Enable MSP telemetry and MSP OSD', 0, 'osd'),
    Feature('MSP', 'msp-sensors', 'HAL_MSP_SENSORS_ENABLED', 'Enable MSP sensors', 0, 'msp-gps,baro-msp,compass-msp,airspeed-msp,msp,msp-opticalflow,msp-rangefinder,osd'),   # NOQA: E501
    Feature('MSP', 'msp-gps', 'HAL_MSP_GPS_ENABLED', 'Enable MSP GPS', 0, 'msp,osd'),
    Feature('MSP', 'compass-msp', 'AP_COMPASS_MSP_ENABLED', 'Enable MSP compass', 0, 'msp,osd'),
    Feature('MSP', 'msp-opticalflow', 'HAL_MSP_OPTICALFLOW_ENABLED', 'Enable MSP OpticalFlow', 0, 'msp,osd,opticalflow'), # also OPTFLOW dep   # NOQA: E501
    Feature('MSP', 'msp-rangefinder', 'HAL_MSP_RANGEFINDER_ENABLED', 'Enable MSP rangefinder', 0, 'msp,osd,rangefinder'),
    Feature('MSP', 'with-msp-displayport', 'HAL_WITH_MSP_DISPLAYPORT', 'Enable MSP DisplayPort OSD (aka CANVAS MODE)', 0, 'msp,osd'),   # NOQA: E501
    Feature('MSP', 'msp-inav-fonts', 'AP_MSP_INAV_FONTS_ENABLED', 'Enable INAV Fonts Translation for DisplayPort', 0, 'with-msp-displayport,msp,osd'),  # NOQA: E501

    Feature('ICE', 'icengine', 'AP_ICENGINE_ENABLED', 'Enable Internal combustion engine support', 0, 'rpm'),
    Feature('ICE', 'efi', 'HAL_EFI_ENABLED', 'Enable EFI monitoring', 0, None),
    Feature('ICE', 'efi-serial-ms', 'AP_EFI_SERIAL_MS_ENABLED', 'Enable MegaSquirt EFI', 0, 'efi'),
    Feature('ICE', 'efi-serial-lutan', 'AP_EFI_SERIAL_LUTAN_ENABLED', 'Enable Lutan EFI', 0, 'efi'),
    Feature('ICE', 'efi-nwpwu', 'AP_EFI_NWPWU_ENABLED', 'Enable NMPMU EFI', 0, 'efi'),
    Feature('ICE', 'efi-currawong-ecu', 'AP_EFI_CURRAWONG_ECU_ENABLED', 'Enable Currawong ECU', 0, 'efi'),
    Feature('ICE', 'efi-serial-hirth', 'AP_EFI_SERIAL_HIRTH_ENABLED', 'Enable Hirth ECU', 0, 'efi'),
    Feature('ICE', 'efi-dronecan', 'AP_EFI_DRONECAN_ENABLED', 'Enable DroneCAN EFI', 0, 'efi,dronecan-drivers'),
    Feature('ICE', 'efi-mav', 'AP_EFI_MAV_ENABLED', 'Enable MAVLink EFI', 0, 'efi'),

    Feature('Generator', 'generator', 'HAL_GENERATOR_ENABLED', 'Enable Generator', 0, None),
    Feature('Generator', 'generator-richenpower', 'AP_GENERATOR_RICHENPOWER_ENABLED', 'Enable Richenpower generator', 0, "generator"),  # noqa
    Feature('Generator', 'generator-ie-2400', 'AP_GENERATOR_IE_2400_ENABLED', 'Enable IntelligentEnergy 2400', 0, "generator"),  # noqa
    Feature('Generator', 'generator-ie-650-800', 'AP_GENERATOR_IE_650_800_ENABLED', 'Enable IntelligentEnergy 650 and 800', 0, "generator"),  # noqa
    Feature('Generator', 'generator-loweheiser', 'AP_GENERATOR_LOWEHEISER_ENABLED', 'Enable Loweheiser generator', 0, "generator,efi"),  # noqa
    Feature('Generator', 'generator-cortex', 'AP_GENERATOR_CORTEX_ENABLED', 'Enable Currawong Engineering Cortex generator', 0, "generator,piccolo-can"),  # noqa

    Feature('OSD', 'osd', 'OSD_ENABLED', 'Enable OSD', 0, None),
    Feature('OSD', 'pluscode', 'HAL_PLUSCODE_ENABLE', 'Enable PlusCode', 0, 'osd'),
    Feature('OSD', 'osd-param', 'OSD_PARAM_ENABLED', 'Enable OSD param', 0, None),
    Feature('OSD', 'osd-sidebar', 'HAL_OSD_SIDEBAR_ENABLE', 'Enable Scrolling sidebars', 0, 'osd'),
    Feature('OSD', 'osd-link-stats-extensions', 'AP_OSD_LINK_STATS_EXTENSIONS_ENABLED', 'Enable OSD panels with extended link stats data', 0, "osd,rcprotocol-crsf,msp"),  # noqa

    Feature('VTX', 'videotx', 'AP_VIDEOTX_ENABLED', 'Enable VideoTX control', 0, None),
    Feature('VTX', 'smartaudio', 'AP_SMARTAUDIO_ENABLED', 'Enable SmartAudio VTX contol', 0, "videotx"),
    Feature('VTX', 'tramp', 'AP_TRAMP_ENABLED', 'Enable IRC Tramp VTX control', 0, "videotx"),

    Feature('ESC', 'piccolo-can', 'HAL_PICCOLO_CAN_ENABLE', 'Enable PiccoloCAN', 0, 'dronecan-drivers'),
    Feature('ESC', 'torqeedo', 'HAL_TORQEEDO_ENABLED', 'Enable Torqeedo motors', 0, None),

    Feature('ESC', 'extended-esc-telem', 'AP_EXTENDED_ESC_TELEM_ENABLED', 'Enable Extended ESC telemetry', 0, 'dronecan-drivers'),  # noqa: E501

    Feature('AP_Periph', 'periph-support-long-can-printf', 'HAL_PERIPH_SUPPORT_LONG_CAN_PRINTF', 'Enable extended length text strings', 0, None),  # noqa: E501
    Feature('AP_Periph', 'periph-device-temperature', 'AP_PERIPH_DEVICE_TEMPERATURE_ENABLED', 'Emit DroneCAN Temperature Messages for AP_Temperature sensors', 0, 'temperature-sensor'), # noqa
    Feature('AP_Periph', 'periph-msp', 'AP_PERIPH_MSP_ENABLED', 'Emit MSP protocol messages from AP_Periph', 0, 'msp'),
    Feature('AP_Periph', 'periph-notify', 'AP_PERIPH_NOTIFY_ENABLED', 'Handle DroneCAN messages for notification equipment (e.g. buzzers, lights etc.)', 0, None), # noqa
    Feature('AP_Periph', 'periph-serial-options', 'AP_PERIPH_SERIAL_OPTIONS_ENABLED', 'Enable Serial Options on AP_Periph', 0, None), # noqa
    Feature('AP_Periph', 'periph-battery', 'AP_PERIPH_BATTERY_ENABLED', 'Emit DroneCAN battery info messages using AP_BattMonitor', 0, None), # noqa
    Feature('AP_Periph', 'periph-relay', 'AP_PERIPH_RELAY_ENABLED', 'Handle DroneCAN hardpoint command', 0, 'relay'),
    Feature('AP_Periph', 'periph-battery-balance', 'AP_PERIPH_BATTERY_BALANCE_ENABLED', 'Emit DroneCAN BatteryInfoAux messages for monitoring Battery Balance', 0, None), # noqa
    Feature('AP_Periph', 'periph-battery-tag', 'AP_PERIPH_BATTERY_TAG_ENABLED', 'Emit DroneCAN BatteryTag messages', 0, None), # noqa
    Feature('AP_Periph', 'periph-proximity', 'AP_PERIPH_PROXIMITY_ENABLED', 'Emit DroneCAN Proximity Messages for AP_Proximity sensors', 0, 'proximity'), # noqa
    Feature('AP_Periph', 'periph-gps', 'AP_PERIPH_GPS_ENABLED', 'Emit DroneCAN GNSS Messages for AP_GPS sensors', 0, None), # noqa
    Feature('AP_Periph', 'periph-adsb', 'AP_PERIPH_ADSB_ENABLED', 'Emit DroneCAN TrafficReport Messages for ADSB_VEHICLE MAVLink messages', 0, None), # noqa
    Feature('AP_Periph', 'periph-mag', 'AP_PERIPH_MAG_ENABLED', 'Emit DroneCAN MagneticFieldStrength Messages ', 0, None), # noqa
    Feature('AP_Periph', 'periph-baro', 'AP_PERIPH_BARO_ENABLED', 'Emit DroneCAN StaticTemperature and StaticPressure Messages for AP_Baro Sensors', 0, None), # noqa
    Feature('AP_Periph', 'periph-rangefinder', 'AP_PERIPH_RANGEFINDER_ENABLED', 'Emit DroneCAN range_sensor_Measurement Messages ', 0, 'rangefinder'), # noqa
    Feature('AP_Periph', 'periph-imu', 'AP_PERIPH_IMU_ENABLED', 'Emit DroneCAN ahrs_RawIMU Messages ', 0, None),
    Feature('AP_Periph', 'periph-rc-out', 'AP_PERIPH_RC_OUT_ENABLED', 'Emit DroneCAN actuator_Status Messages', 0, None),
    Feature('AP_Periph', 'periph-efi', 'AP_PERIPH_EFI_ENABLED', 'Emit DroneCAN ice_reciprocating_Status Messages', 0, 'efi'),
    Feature('AP_Periph', 'periph-rcin', 'AP_PERIPH_RCIN_ENABLED', 'Emit DroneCAN RCInput Messages', 0, 'rcprotocol'),
    Feature('AP_Periph', 'periph-rpm', 'AP_PERIPH_RPM_ENABLED', 'Emit DroneCAN RPM messages for AP_RPM sensors', 0, 'rpm'),
    Feature('AP_Periph', 'periph-airspeed', 'AP_PERIPH_AIRSPEED_ENABLED', 'Emit DroneCAN air_data_RawAirData messages for AP_Airspeed sensors', 0, 'airspeed'), # noqa

    Feature('Camera', 'camera', 'AP_CAMERA_ENABLED', 'Enable Camera trigger', 0, None),
    Feature('Camera', 'camera-mavlink', 'AP_CAMERA_MAVLINK_ENABLED', 'Enable MAVLink camera ', 0, 'camera'),
    Feature('Camera', 'camera-mavlinkcamv2', 'AP_CAMERA_MAVLINKCAMV2_ENABLED', 'Enable MAVLink CameraV2', 0, 'camera'),
    Feature('Camera', 'camera-mount', 'AP_CAMERA_MOUNT_ENABLED', 'Enable Camera-in-Mount ', 0, 'camera,mount'),
    Feature('Camera', 'camera-relay', 'AP_CAMERA_RELAY_ENABLED', 'Enable Relay camera trigger', 0, 'camera,relay'),
    Feature('Camera', 'camera-servo', 'AP_CAMERA_SERVO_ENABLED', 'Enable Servo camera trigger', 0, 'camera'),
    Feature('Camera', 'camera-sologimbal', 'AP_CAMERA_SOLOGIMBAL_ENABLED', 'Enable Solo gimbal', 0, 'camera'),
    Feature('Camera', 'camera-send-fov-status', 'AP_CAMERA_SEND_FOV_STATUS_ENABLED', 'Enable GCS camera FOV status', 0, 'camera,mount'),  # noqa: E501
    Feature('Camera', 'camera-send-thermal-range', 'AP_CAMERA_SEND_THERMAL_RANGE_ENABLED', 'Enable GCS camera thermal range', 0, 'camera,mount'),  # noqa: E501
    Feature('Camera', 'camera-info-from-script', 'AP_CAMERA_INFO_FROM_SCRIPT_ENABLED', 'Enable Camera information messages via Lua script', 0, 'camera,scripting'), # noqa

    Feature('Camera', 'camera-runcam', 'AP_CAMERA_RUNCAM_ENABLED', 'Enable RunCam control', 0, 'camera'),

    Feature('Copter', 'mode-zigzag', 'MODE_ZIGZAG_ENABLED', 'Enable Mode ZigZag', 0, None),
    Feature('Copter', 'mode-systemid', 'MODE_SYSTEMID_ENABLED', 'Enable Mode SystemID', 0, 'logging'),
    Feature('Copter', 'mode-sport', 'MODE_SPORT_ENABLED', 'Enable Mode Sport', 0, None),
    Feature('Copter', 'mode-follow', 'MODE_FOLLOW_ENABLED', 'Enable Mode Follow', 0, 'avoidance,follow'),
    Feature('Copter', 'mode-turtle', 'MODE_TURTLE_ENABLED', 'Enable Mode Turtle', 0, None),
    Feature('Copter', 'mode-guided-nogps', 'MODE_GUIDED_NOGPS_ENABLED', 'Enable Mode Guided NoGPS', 0, None),
    Feature('Copter', 'mode-flowhold', 'MODE_FLOWHOLD_ENABLED', 'Enable Mode Flowhold', 0, "opticalflow"),
    Feature('Copter', 'mode-flip', 'MODE_FLIP_ENABLED', 'Enable Mode Flip', 0, None),
    Feature('Copter', 'mode-brake', 'MODE_BRAKE_ENABLED', 'Enable Mode Brake', 0, None),
    Feature('Copter', 'copter-advanced-failsafe', 'AP_COPTER_ADVANCED_FAILSAFE_ENABLED', 'Enable Advanced Failsafe', 0, "advancedfailsafe"),  # NOQA: 501
    Feature('Copter', 'copter-ahrs-auto-trim', 'AP_COPTER_AHRS_AUTO_TRIM_ENABLED', 'Enable Copter AHRS AutoTrim', 0, None),  # noqa

    Feature('Rover', 'rover-advanced-failsafe', 'AP_ROVER_ADVANCED_FAILSAFE_ENABLED', 'Enable Advanced Failsafe', 0, "advancedfailsafe"),  # NOQA: 501
    Feature('Rover', 'rover-auto-arm-once', 'AP_ROVER_AUTO_ARM_ONCE_ENABLED', 'Make Auto-Arm-Once functionality available', 0, None),  # NOQA: 501

    Feature('Mission', 'mission-nav-payload-place', 'AP_MISSION_NAV_PAYLOAD_PLACE_ENABLED', 'Enable NAV_PAYLOAD_PLACE', 0, None),  # noqa
    Feature('Copter', 'ac-payload-place', 'AC_PAYLOAD_PLACE_ENABLED', 'Enable Copter Payload Place', 0, 'mission-nav-payload-place'),  # noqa

    Feature('Compass', 'compass-ak09916', 'AP_COMPASS_AK09916_ENABLED', 'Enable AK0991x compasses', 1, None),
    Feature('Compass', 'compass-ak8963', 'AP_COMPASS_AK8963_ENABLED', 'Enable AK8963 compasses', 1, None),
    Feature('Compass', 'compass-bmm150', 'AP_COMPASS_BMM150_ENABLED', 'Enable BMM150 compasses', 1, None),
    Feature('Compass', 'compass-bmm350', 'AP_COMPASS_BMM350_ENABLED', 'Enable BMM350 compasses', 1, None),
    Feature('Compass', 'compass-externalahrs', 'AP_COMPASS_EXTERNALAHRS_ENABLED', 'Enable ExternalAHRS compasses', 0, "external-ahrs"),  # noqa
    Feature('Compass', 'compass-hmc5843', 'AP_COMPASS_HMC5843_ENABLED', 'Enable HMC5843 compasses', 1, None),
    Feature('Compass', 'compass-icm20948', 'AP_COMPASS_ICM20948_ENABLED', 'Enable AK0991x on ICM20948 compasses', 1, "compass-ak09916"),  # noqa: E501
    Feature('Compass', 'compass-ist8308', 'AP_COMPASS_IST8308_ENABLED', 'Enable IST8308 compasses', 1, None),
    Feature('Compass', 'compass-iis2mdc', 'AP_COMPASS_IIS2MDC_ENABLED', 'Enable IIS2MDC compasses', 0, None),
    Feature('Compass', 'compass-ist8310', 'AP_COMPASS_IST8310_ENABLED', 'Enable IST8310 compasses', 1, None),
    Feature('Compass', 'compass-lis3mdl', 'AP_COMPASS_LIS3MDL_ENABLED', 'Enable LIS3MDL compasses', 1, None),
    Feature('Compass', 'compass-lsm303d', 'AP_COMPASS_LSM303D_ENABLED', 'Enable LSM303D compasses', 1, None),
    Feature('Compass', 'compass-lsm9ds1', 'AP_COMPASS_LSM9DS1_ENABLED', 'Enable LSM9DS1 compasses', 1, None),
    Feature('Compass', 'compass-mag3110', 'AP_COMPASS_MAG3110_ENABLED', 'Enable MAG3110 compasses', 1, None),
    Feature('Compass', 'compass-mmc3416', 'AP_COMPASS_MMC3416_ENABLED', 'Enable MMC3416 compasses', 1, None),
    Feature('Compass', 'compass-mmc5xx3', 'AP_COMPASS_MMC5XX3_ENABLED', 'Enable MMC5XX3 compasses', 1, None),
    Feature('Compass', 'compass-qmc5883l', 'AP_COMPASS_QMC5883L_ENABLED', 'Enable QMC5883L compasses', 1, None),
    Feature('Compass', 'compass-qmc5883p', 'AP_COMPASS_QMC5883P_ENABLED', 'Enable QMC5883P compasses', 1, None),
    Feature('Compass', 'compass-rm3100', 'AP_COMPASS_RM3100_ENABLED', 'Enable RM3100 compasses', 1, None),
    Feature('Compass', 'compass-dronecan', 'AP_COMPASS_DRONECAN_ENABLED', 'Enable DroneCAN compasses', 0, "dronecan-drivers"),
    Feature('Compass', 'compass-dronecan-hires', 'AP_COMPASS_DRONECAN_HIRES_ENABLED', 'Enable DroneCAN HiRes compasses for survey logging', 0, "dronecan-drivers,compass-dronecan"), # noqa
    Feature('Compass', 'compass-calibration-fixed-yaw', 'AP_COMPASS_CALIBRATION_FIXED_YAW_ENABLED', 'Enable Fixed-Yaw Compass Calibration', 1, None),  # noqa
    Feature('Compass', 'compass-learn', 'COMPASS_LEARN_ENABLED', 'Enable In-Flight compass learning', 1, "compass-calibration-fixed-yaw"),  # noqa: E501

    Feature('Gimbal', 'mount', 'HAL_MOUNT_ENABLED', 'Enable Camera Mounts', 0, None),
    Feature('Gimbal', 'mount-alexmos', 'HAL_MOUNT_ALEXMOS_ENABLED', 'Enable Alexmos gimbal', 0, "mount"),
    Feature('Gimbal', 'mount-caddx', 'HAL_MOUNT_CADDX_ENABLED', 'Enable CADDX gimbal', 0, "mount"),
    Feature('Gimbal', 'mount-gremsy', 'HAL_MOUNT_GREMSY_ENABLED', 'Enable Gremsy gimbal', 0, "mount"),
    Feature('Gimbal', 'mount-servo', 'HAL_MOUNT_SERVO_ENABLED', 'Enable Servo gimbal', 0, "mount"),
    Feature('Gimbal', 'mount-siyi', 'HAL_MOUNT_SIYI_ENABLED', 'Enable Siyi gimbal', 0, "mount"),
    Feature('Gimbal', 'solo-gimbal', 'HAL_SOLO_GIMBAL_ENABLED', 'Enable Solo gimbal', 0, "mount"),
    Feature('Gimbal', 'mount-storm32mavlink', 'HAL_MOUNT_STORM32MAVLINK_ENABLED', 'Enable SToRM32 MAVLink gimbal', 0, "mount"),
    Feature('Gimbal', 'mount-storm32serial', 'HAL_MOUNT_STORM32SERIAL_ENABLED', 'Enable SToRM32 Serial gimbal', 0, "mount"),
    Feature('Gimbal', 'mount-topotek', 'HAL_MOUNT_TOPOTEK_ENABLED', 'Enable Topotek gimbal', 0, "mount"),
    Feature('Gimbal', 'mount-xacti', 'HAL_MOUNT_XACTI_ENABLED', 'Enable Xacti gimbal', 0, "mount,dronecan-drivers"),
    Feature('Gimbal', 'mount-xfrobot', 'HAL_MOUNT_XFROBOT_ENABLED', 'Enable XFRobot gimbal', 0, "mount"),
    Feature('Gimbal', 'mount-viewpro', 'HAL_MOUNT_VIEWPRO_ENABLED', 'Enable Viewpro gimbal', 0, "mount"),

    Feature('VTOL Frame', 'motors-tri', 'AP_MOTORS_TRI_ENABLED', 'TriCopters', 0, None),
    Feature('VTOL Frame', 'motors-frame-quad', 'AP_MOTORS_FRAME_QUAD_ENABLED', 'QUAD', 1, None),
    Feature('VTOL Frame', 'motors-frame-hexa', 'AP_MOTORS_FRAME_HEXA_ENABLED', 'HEXA', 0, None),
    Feature('VTOL Frame', 'motors-frame-octa', 'AP_MOTORS_FRAME_OCTA_ENABLED', 'OCTA', 0, None),
    Feature('VTOL Frame', 'motors-frame-deca', 'AP_MOTORS_FRAME_DECA_ENABLED', 'DECA', 0, None),
    Feature('VTOL Frame', 'motors-frame-dodecahexa', 'AP_MOTORS_FRAME_DODECAHEXA_ENABLED', 'DODECAHEXA', 0, None),
    Feature('VTOL Frame', 'motors-frame-y6', 'AP_MOTORS_FRAME_Y6_ENABLED', 'Y6', 0, None),
    Feature('VTOL Frame', 'motors-frame-octaquad', 'AP_MOTORS_FRAME_OCTAQUAD_ENABLED', 'OCTAQUAD', 0, None),

    Feature('Payload', 'gripper', 'AP_GRIPPER_ENABLED', 'Enable Gripper', 0, None),
    Feature('Payload', 'sprayer', 'HAL_SPRAYER_ENABLED', 'Enable Sprayer', 0, None),
    Feature('Payload', 'landinggear', 'AP_LANDINGGEAR_ENABLED', 'Enable Landing Gear', 0, None),
    Feature('Payload', 'winch', 'AP_WINCH_ENABLED', 'Enable Winch', 0, None),
    Feature('Payload', 'winch-daiwa', 'AP_WINCH_DAIWA_ENABLED', 'Enable DAIWA Winch', 0, 'winch'),
    Feature('Payload', 'winch-pwm', 'AP_WINCH_PWM_ENABLED', 'Enable PWM Winch', 0, 'winch'),

    Feature('Payload', 'relay', 'AP_RELAY_ENABLED', 'Enable Relays', 0, None),
    Feature('Payload', 'servorelayevents', 'AP_SERVORELAYEVENTS_ENABLED', 'Enable Servo/Relay Event', 0, None),

    Feature('Plane', 'advancedfailsafe', 'AP_ADVANCEDFAILSAFE_ENABLED', 'Enable Advanced Failsafe', 0, None),
    Feature('Plane', 'quadplane', 'HAL_QUADPLANE_ENABLED', 'Enable QuadPlane', 0, None),
    Feature('Plane', 'soaring', 'HAL_SOARING_ENABLED', 'Enable Soaring', 0, None),
    Feature('Plane', 'landing-deepstall', 'HAL_LANDING_DEEPSTALL_ENABLED', 'Enable Deepstall landing', 0, None),
    Feature('Plane', 'qautotune', 'QAUTOTUNE_ENABLED', 'Enable QuadPlane AUTOTUNE', 0, "quadplane"),
    Feature('Plane', 'plane-blackbox-logging', 'AP_PLANE_BLACKBOX_LOGGING', 'Enable Blackbox logging', 0, None),
    Feature('Plane', 'tuning', 'AP_TUNING_ENABLED', 'Enable TX-based tuning parameter adjustments', 0, None),
    Feature('Plane', 'plane-offboard-guided-slew', 'AP_PLANE_OFFBOARD_GUIDED_SLEW_ENABLED', 'Enable Offboard-guided slew commands', 0, None),  # noqa:401
    Feature('Plane', 'plane-glider-pullup', 'AP_PLANE_GLIDER_PULLUP_ENABLED', 'Enable Glider pullup support', 0, None),
    Feature('Plane', 'quicktune', 'AP_QUICKTUNE_ENABLED', 'Enable VTOL quicktune', 0, None),
    Feature('Plane', 'mode-autoland', 'MODE_AUTOLAND_ENABLED', 'Enable Fixed Wing Autolanding mode', 0, None),
    Feature('Plane', 'plane-systemid', 'AP_PLANE_SYSTEMID_ENABLED', 'Enable systemID support', 0, 'quadplane,logging'),  # NOQA:E501

    Feature('RC', 'rcprotocol', 'AP_RCPROTOCOL_ENABLED', "Enable Serial RC Protocols", 0, None),   # NOQA: E501
    Feature('RC', 'rcprotocol-crsf', 'AP_RCPROTOCOL_CRSF_ENABLED', "Enable CRSF", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rcprotocol-ibus', 'AP_RCPROTOCOL_IBUS_ENABLED', "Enable IBus", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rcprotocol-sbus', 'AP_RCPROTOCOL_SBUS_ENABLED', "Enable SBUS", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rcprotocol-ppmsum', 'AP_RCPROTOCOL_PPMSUM_ENABLED', "Enable PPMSum", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rcprotocol-srxl', 'AP_RCPROTOCOL_SRXL_ENABLED', "Enable SRXL", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rcprotocol-srxl2', 'AP_RCPROTOCOL_SRXL2_ENABLED', "Enable SRXL2", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rcprotocol-st24', 'AP_RCPROTOCOL_ST24_ENABLED', "Enable ST24", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rcprotocol-sumd', 'AP_RCPROTOCOL_SUMD_ENABLED', "Enable SUMD", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rcprotocol-ghst', 'AP_RCPROTOCOL_GHST_ENABLED', "Enable Ghost", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rcprotocol-mavlink-radio', 'AP_RCPROTOCOL_MAVLINK_RADIO_ENABLED', "Enable MAVLink", 0, "rcprotocol"),   # NOQA: E501
    Feature('RC', 'rssi', 'AP_RSSI_ENABLED', 'RSSI', 0, None),

    Feature('RC', 'rc-transmitter-tuning', 'AP_RC_TRANSMITTER_TUNING_ENABLED', "Enable knob-based transmitter tuning", 0, None),  # NOQA:E501

    Feature('Rangefinder', 'rangefinder', 'AP_RANGEFINDER_ENABLED', "Enable Rangefinders", 0, None),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-analog', 'AP_RANGEFINDER_ANALOG_ENABLED', "Enable Rangefinder - Analog", 0, "rangefinder"),   # NOQA: E501
    # Feature('Rangefinder', 'rangefinder-bbb-pru', 'AP_RANGEFINDER_BBB_PRU_ENABLED', "Enable Rangefinder - BBB PRU", 0, "rangefinder"),   # NOQA: E501
    # Feature('Rangefinder', 'rangefinder-bebop', 'AP_RANGEFINDER_BEBOP_ENABLED', "Enable Rangefinder - Bebop", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-benewake-can', 'AP_RANGEFINDER_BENEWAKE_CAN_ENABLED', "Enable Rangefinder - Benewake (CAN)", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-benewake-tf02', 'AP_RANGEFINDER_BENEWAKE_TF02_ENABLED', "Enable Rangefinder - Benewake -TF02", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-benewake-tf03', 'AP_RANGEFINDER_BENEWAKE_TF03_ENABLED', "Enable Rangefinder - Benewake - TF03", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-benewake-tfmini', 'AP_RANGEFINDER_BENEWAKE_TFMINI_ENABLED', "Enable Rangefinder - Benewake - TFMini", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-benewake-tfminiplus', 'AP_RANGEFINDER_BENEWAKE_TFMINIPLUS_ENABLED', "Enable Rangefinder - Benewake - TFMiniPlus", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-blping', 'AP_RANGEFINDER_BLPING_ENABLED', "Enable Rangefinder - BLPing", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-gyus42v2', 'AP_RANGEFINDER_GYUS42V2_ENABLED', "Enable Rangefinder - GYUS42V2", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-hc-sr04', 'AP_RANGEFINDER_HC_SR04_ENABLED', "Enable Rangefinder - HC_SR04", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-jre-serial', 'AP_RANGEFINDER_JRE_SERIAL_ENABLED', "Enable Rangefinder - JRE_SERIAL", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-lanbao', 'AP_RANGEFINDER_LANBAO_ENABLED', "Enable Rangefinder - Lanbao", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-leddarone', 'AP_RANGEFINDER_LEDDARONE_ENABLED', "Enable Rangefinder - LeddarOne", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-leddarvu8', 'AP_RANGEFINDER_LEDDARVU8_ENABLED', "Enable Rangefinder - LeddarVU8", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-lightware-serial', 'AP_RANGEFINDER_LIGHTWARE_SERIAL_ENABLED', "Enable Rangefinder - Lightware (serial)", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-lua', 'AP_RANGEFINDER_LUA_ENABLED', "Enable Rangefinder - Lua Scripting", 0, "rangefinder,scripting"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-lwi2c', 'AP_RANGEFINDER_LWI2C_ENABLED', "Enable Rangefinder - Lightware (i2c)", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-mavlink', 'AP_RANGEFINDER_MAVLINK_ENABLED', "Enable Rangefinder - MAVLink", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-maxbotix-serial', 'AP_RANGEFINDER_MAXBOTIX_SERIAL_ENABLED', "Enable Rangefinder - MaxBotix (serial)", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-maxsonari2cxl', 'AP_RANGEFINDER_MAXSONARI2CXL_ENABLED', "Enable Rangefinder - MaxSonarI2CXL", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-nmea', 'AP_RANGEFINDER_NMEA_ENABLED', "Enable Rangefinder - NMEA", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-nooploop', 'AP_RANGEFINDER_NOOPLOOP_ENABLED', "Enable Rangefinder - Nooploop TOF P/F", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-nra24-can', 'AP_RANGEFINDER_NRA24_CAN_ENABLED', "Enable Rangefinder - NRA24 CAN", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-pulsedlightlrf', 'AP_RANGEFINDER_PULSEDLIGHTLRF_ENABLED', "Enable Rangefinder - PulsedLightLRF", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-pwm', 'AP_RANGEFINDER_PWM_ENABLED', "Enable Rangefinder - PWM", 0, "rangefinder"),   # NOQA: E501
    # Feature('Rangefinder', 'rangefinder-sim', 'AP_RANGEFINDER_SIM_ENABLED', "Enable Rangefinder - SIM", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-tofsensef-i2c', 'AP_RANGEFINDER_TOFSENSEF_I2C_ENABLED', "Enable Rangefinder - ToFSense-F I2C", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-tofsensep-can', 'AP_RANGEFINDER_TOFSENSEP_CAN_ENABLED', "Enable Rangefinder - ToFSense-P CAN", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-tri2c', 'AP_RANGEFINDER_TRI2C_ENABLED', "Enable Rangefinder - TeraRangerI2C", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-teraranger-serial', 'AP_RANGEFINDER_TERARANGER_SERIAL_ENABLED', "Enable Rangefinder - TeraRanger Serial", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-dronecan', 'AP_RANGEFINDER_DRONECAN_ENABLED', "Enable Rangefinder - DroneCAN", 0, "rangefinder,dronecan-drivers"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-usd1-can', 'AP_RANGEFINDER_USD1_CAN_ENABLED', "Enable Rangefinder - USD1 (CAN)", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-usd1-serial', 'AP_RANGEFINDER_USD1_SERIAL_ENABLED', "Enable Rangefinder - USD1 (SERIAL)", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-vl53l0x', 'AP_RANGEFINDER_VL53L0X_ENABLED', "Enable Rangefinder - VL53L0X", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-vl53l1x', 'AP_RANGEFINDER_VL53L1X_ENABLED', "Enable Rangefinder - VL53L1X", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-wasp', 'AP_RANGEFINDER_WASP_ENABLED', "Enable Rangefinder - Wasp", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-rds02uf', 'AP_RANGEFINDER_RDS02UF_ENABLED', "Enable Rangefinder - RDS02UF", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-hexsoonradar', 'AP_RANGEFINDER_HEXSOONRADAR_ENABLED', "Enable Rangefinder - Hexsoon Radar", 0, "rangefinder"),   # NOQA: E501
    Feature('Rangefinder', 'rangefinder-ainstein-lr-d1', 'AP_RANGEFINDER_AINSTEIN_LR_D1_ENABLED', "Enable Rangefinder - Ainstein LRD1", 0, "rangefinder"),   # NOQA: E501

    Feature('Sensors', 'opticalflow', 'AP_OPTICALFLOW_ENABLED', 'Enable Optical Flow', 0, None),
    Feature('Sensors', 'opticalflow-cxof', 'AP_OPTICALFLOW_CXOF_ENABLED', 'Enable Optical flow CXOF Sensor', 0, "opticalflow"),
    Feature('Sensors', 'opticalflow-hereflow', 'AP_OPTICALFLOW_HEREFLOW_ENABLED', 'Enable Optical flow HereFlow Sensor', 0, "opticalflow,dronecan-drivers"),   # NOQA: E501
    Feature('Sensors', 'opticalflow-mav', 'AP_OPTICALFLOW_MAV_ENABLED', 'Enable Optical flow MAVLink Sensor', 0, "opticalflow"),   # NOQA: E501
    Feature('Sensors', 'opticalflow-onboard', 'AP_OPTICALFLOW_ONBOARD_ENABLED', 'Enable Optical flow ONBOARD Sensor', 0, "opticalflow"),   # NOQA: E501
    Feature('Sensors', 'opticalflow-px4flow', 'AP_OPTICALFLOW_PX4FLOW_ENABLED', 'Enable Optical flow PX4FLOW Sensor', 0, "opticalflow"),   # NOQA: E501
    Feature('Sensors', 'opticalflow-pixart', 'AP_OPTICALFLOW_PIXART_ENABLED', 'Enable Optical flow PIXART Sensor', 0, "opticalflow"),   # NOQA: E501
    Feature('Sensors', 'opticalflow-upflow', 'AP_OPTICALFLOW_UPFLOW_ENABLED', 'Enable Optical flow UPFLOW Sensor', 0, "opticalflow"),   # NOQA: E501

    Feature('Proximity', 'proximity', 'HAL_PROXIMITY_ENABLED', 'Enable Proximity', 0, None),
    Feature('Proximity', 'proximity-cygbot', 'AP_PROXIMITY_CYGBOT_ENABLED', 'Enable Cygbot D1 Proximity Sensors', 0, "proximity"),  # noqa
    Feature('Proximity', 'proximity-dronecan', 'AP_PROXIMITY_DRONECAN_ENABLED', 'Enable DroneCAN Proximity Sensors', 0, "proximity,dronecan-drivers"),  # noqa
    Feature('Proximity', 'proximity-lightware-sf40c', 'AP_PROXIMITY_LIGHTWARE_SF40C_ENABLED', 'Enable LightWare SF40C Proximity Sensors', 0, "proximity"),  # noqa
    Feature('Proximity', 'proximity-lightware-sf45b', 'AP_PROXIMITY_LIGHTWARE_SF45B_ENABLED', 'Enable LightWare SF45B Proximity Sensors', 0, "proximity"),  # noqa
    Feature('Proximity', 'proximity-mav', 'AP_PROXIMITY_MAV_ENABLED', 'Enable MAVLink Proximity Sensors', 0, "proximity"),  # noqa
    Feature('Proximity', 'proximity-rangefinder', 'AP_PROXIMITY_RANGEFINDER_ENABLED', 'Use RangeFinders as proximity sensors', 0, "proximity,rangefinder"),  # noqa
    Feature('Proximity', 'proximity-rplidara2', 'AP_PROXIMITY_RPLIDARA2_ENABLED', 'Enable RPLidarA2 Proximity Sensors', 0, "proximity"),  # noqa
    Feature('Proximity', 'proximity-terarangertower', 'AP_PROXIMITY_TERARANGERTOWER_ENABLED', 'Enable TerraRangerTower Proximity Sensors', 0, "proximity"),  # noqa
    Feature('Proximity', 'proximity-terarangertowerevo', 'AP_PROXIMITY_TERARANGERTOWEREVO_ENABLED', 'Enable TerraRangerTower Evo Proximity Sensors', 0, "proximity"),  # noqa
    Feature('Proximity', 'proximity-mr72', 'AP_PROXIMITY_MR72_ENABLED', 'Enable NanoRadar MR72 Proximity Sensors', 0, "proximity"),  # noqa
    Feature('Proximity', 'proximity-hexsoonradar', 'AP_PROXIMITY_HEXSOONRADAR_ENABLED', 'Enable Hexsoon Radar Proximity Sensors', 0, "proximity"),  # noqa

    Feature('Baro', 'baro-bmp085', 'AP_BARO_BMP085_ENABLED', 'Enable BMP085 Barometric Sensor', 1, None),
    Feature('Baro', 'baro-bmp280', 'AP_BARO_BMP280_ENABLED', 'Enable BMP280 Barometric Sensor', 1, None),
    Feature('Baro', 'baro-bmp388', 'AP_BARO_BMP388_ENABLED', 'Enable BMP388 Barometric Sensor', 1, None),
    Feature('Baro', 'baro-bmp581', 'AP_BARO_BMP581_ENABLED', 'Enable BMP581 Barometric Sensor', 1, None),
    Feature('Baro', 'baro-dps280', 'AP_BARO_DPS280_ENABLED', 'Enable DPS280/DPS310 Barometric Sensor', 1, None),
    # Feature('Baro', 'baro-dummy', 'AP_BARO_DUMMY_ENABLED', 'Enable DUMMY Barometric Sensor', 0, None),
    Feature('Baro', 'baro-externalahrs', 'AP_BARO_EXTERNALAHRS_ENABLED', 'Enable EXTERNALAHRS Barometric Sensor', 0, 'external-ahrs'),  # NOQA
    Feature('Baro', 'baro-fbm320', 'AP_BARO_FBM320_ENABLED', 'Enable FBM320 Barometric Sensor', 1, None),
    # Feature('Baro', 'baro-icm20789', 'AP_BARO_ICM20789_ENABLED', 'Enable ICM20789 Barometric Sensor', 1, None),
    Feature('Baro', 'baro-kellerld', 'AP_BARO_KELLERLD_ENABLED', 'Enable KELLERLD Barometric Sensor', 1, None),
    Feature('Baro', 'baro-lps2xh', 'AP_BARO_LPS2XH_ENABLED', 'Enable LPS2XH Barometric Sensor', 1, None),
    Feature('Baro', 'baro-ms5607', 'AP_BARO_MS5607_ENABLED', 'Enable MS5607 Barometric Sensor', 1, None),
    Feature('Baro', 'baro-ms5611', 'AP_BARO_MS5611_ENABLED', 'Enable MS5611 Barometric Sensor', 1, 'baro-ms5607'),  # MS5611 has an option to be treated as 5607  # NOQA:E501
    Feature('Baro', 'baro-ms5637', 'AP_BARO_MS5637_ENABLED', 'Enable MS5637 Barometric Sensor', 1, None),
    Feature('Baro', 'baro-ms5837', 'AP_BARO_MS5837_ENABLED', 'Enable MS5837 Barometric Sensor', 1, None),
    Feature('Baro', 'baro-msp', 'AP_BARO_MSP_ENABLED', 'Enable MSP Barometric Sensor', 0, 'msp'),
    Feature('Baro', 'baro-spl06', 'AP_BARO_SPL06_ENABLED', 'Enable SPL06 Barometric Sensor', 1, None),
    Feature('Baro', 'baro-dronecan', 'AP_BARO_DRONECAN_ENABLED', 'Enable DroneCAN Barometric Sensor', 0, "dronecan-drivers"),
    # Feature('Baro', 'baro-icp101xx', 'AP_BARO_ICP101XX_ENABLED', 'Enable ICP101XX Barometric Sensor', 0, None),
    # Feature('Baro', 'baro-icp201xx', 'AP_BARO_ICP201XX_ENABLED', 'Enable ICP201XX Barometric Sensor', 0, None),
    Feature('Baro', 'tempcalibration', 'AP_TEMPCALIBRATION_ENABLED', 'Enable Baro Temperature Calibration', 0, None),
    Feature('Baro', 'baro-probe-external-i2c-buses', 'AP_BARO_PROBE_EXTERNAL_I2C_BUSES', 'Enable Probing of External i2c buses', 0, None),  # noqa: E501
    Feature('Baro', 'baro-thst-comp', 'AP_BARO_THST_COMP_ENABLED', 'Enable thrust compensation on BARO1', 0, None),

    Feature('Sensors', 'rpm', 'AP_RPM_ENABLED', 'Enable RPM sensors', 0, None),
    Feature('Sensors', 'rpm-efi', 'AP_RPM_EFI_ENABLED', 'Enable RPM EFI sensors', 0, 'rpm,efi'),
    Feature('Sensors', 'rpm-esc-telem', 'AP_RPM_ESC_TELEM_ENABLED', 'Enable RPM ESC Telemetry sensors', 0, 'rpm'),
    Feature('Sensors', 'rpm-harmonicnotch', 'AP_RPM_HARMONICNOTCH_ENABLED', 'Enable RPM Harmonic Notch sensors', 0, 'rpm,inertialsensor-harmonicnotch'),  # noqa
    Feature('Sensors', 'rpm-pin', 'AP_RPM_PIN_ENABLED', 'Enable RPM Pin-based sensors', 0, 'rpm'),
    Feature('Sensors', 'rpm-generator', 'AP_RPM_GENERATOR_ENABLED', 'Enable Generator RPM sensors', 0, 'rpm,generator'),
    Feature('Sensors', 'rpm-dronecan', 'AP_RPM_DRONECAN_ENABLED', 'Enable DroneCAN-based RPM sensors', 0, 'rpm,generator,dronecan-drivers'),  # noqa

    Feature('Sensors', 'temperature-sensor', 'AP_TEMPERATURE_SENSOR_ENABLED', 'Enable Temperature Sensors', 0, None),
    Feature('Sensors', 'temperature-sensor-tsys01', 'AP_TEMPERATURE_SENSOR_TSYS01_ENABLED', 'Enable Temp Sensor - TSYS01', 0, "temperature-sensor"),  # noqa: E501
    Feature('Sensors', 'temperature-sensor-mcp9600', 'AP_TEMPERATURE_SENSOR_MCP9600_ENABLED', 'Enable Temp Sensor - MCP9600', 0, "temperature-sensor"),  # noqa: E501
    Feature('Sensors', 'temperature-sensor-tsys03', 'AP_TEMPERATURE_SENSOR_TSYS03_ENABLED', 'Enable Temp Sensor - TSYS03', 0, "temperature-sensor"),  # noqa: E501
    Feature('Sensors', 'temperature-sensor-mlx90614', 'AP_TEMPERATURE_SENSOR_MLX90614_ENABLED', 'Enable Temp Sensor - MLX90614', 0, "temperature-sensor"),  # noqa: E501
    Feature('Sensors', 'temperature-sensor-sht3x', 'AP_TEMPERATURE_SENSOR_SHT3X_ENABLED', 'Enable Temp Sensor - SHT3x', 0, "temperature-sensor"),  # noqa: E501

    Feature('Sensors', 'airspeed', 'AP_AIRSPEED_ENABLED', 'Enable Airspeed Sensors', 1, None),    # Default to enabled to not annoy Plane users   # NOQA: E501
    Feature('Sensors', 'beacon', 'AP_BEACON_ENABLED', 'Enable Beacon', 0, None),
    Feature('Sensors', 'gps-moving-baseline', 'GPS_MOVING_BASELINE', 'Enable GPS Moving Baseline', 0, None),
    Feature('Sensors', 'serialmanager-imuout', 'AP_SERIALMANAGER_IMUOUT_ENABLED', 'Enable Send raw IMU data on a serial port', 0, None), # NOQA: E501

    Feature('IMU', 'ins-temperature-cal', 'HAL_INS_TEMPERATURE_CAL_ENABLE', 'Enable IMU Temperature calibration', 0, None),
    Feature('IMU', 'inertialsensor-harmonicnotch', 'AP_INERTIALSENSOR_HARMONICNOTCH_ENABLED', 'Enable InertialSensor harmonic notch filters', 0, None),  # noqa
    Feature('IMU', 'inertialsensor-batchsampler', 'AP_INERTIALSENSOR_BATCHSAMPLER_ENABLED', 'Enable Batch sampler', 0, None),  # noqa

    Feature('Other', 'inertialsensor-fast-sample-window', 'AP_INERTIALSENSOR_FAST_SAMPLE_WINDOW_ENABLED', 'Enable Rate Loop Thread', 0, 'inertialsensor-harmonicnotch'),  # noqa
    Feature('Other', 'gyrofft', 'HAL_GYROFFT_ENABLED', 'Enable In-Flight gyro FFT calculations', 0, None),
    Feature('Other', 'nmea-output', 'HAL_NMEA_OUTPUT_ENABLED', 'Enable NMEA output', 0, None),
    Feature('Other', 'filesystem-format', 'AP_FILESYSTEM_FORMAT_ENABLED', 'Enable Formatting of microSD cards', 0, None),
    Feature('Other', 'bootloader-flashing', 'AP_BOOTLOADER_FLASHING_ENABLED', 'Enable Bootloader flashing', 0, "filesystem-romfs"),  # noqa
    Feature('Other', 'serialmanager-register', 'AP_SERIALMANAGER_REGISTER_ENABLED', 'Enable Serial device registration', 0, None), # noqa

    Feature('Scripting', 'scripting', 'AP_SCRIPTING_ENABLED', 'Enable Lua Scripting', 0, None),
    Feature('Scripting', 'scripting-serialdevice', 'AP_SCRIPTING_SERIALDEVICE_ENABLED', 'Enable Lua serial device simulation', 0, "scripting,serialmanager-register"), # noqa
    Feature('Scripting', 'scripting-binding-motors', 'AP_SCRIPTING_BINDING_MOTORS_ENABLED', 'Enable bindings for AP_Motors', 0, "scripting"), # noqa
    Feature('Scripting', 'scripting-binding-vehicle', 'AP_SCRIPTING_BINDING_VEHICLE_ENABLED', 'Enable bindings for AP_Vehicle', 0, "scripting"), # noqa

    Feature('Other', 'can-slcan', 'AP_CAN_SLCAN_ENABLED', 'Enable SLCAN serial protocol', 0, None),
    Feature('Other', 'sdcard-storage', 'AP_SDCARD_STORAGE_ENABLED', 'Enable Storing mission on microSD cards', 0, None),
    Feature('Other', 'compass-cal', 'COMPASS_CAL_ENABLED', 'Enable "Tumble" compass calibration', 0, None),
    Feature('Other', 'dronecan-serial', 'AP_DRONECAN_SERIAL_ENABLED', 'Enable DroneCAN virtual serial ports', 0, "dronecan-drivers,serialmanager-register"),  # NOQA: E501
    Feature('Other', 'button', 'HAL_BUTTON_ENABLED', 'Enable Buttons', 0, None),
    Feature('Other', 'logging', 'HAL_LOGGING_ENABLED', 'Enable Logging', 0, None),
    Feature('Other', 'customrotations', 'AP_CUSTOMROTATIONS_ENABLED', 'Enable Custom  sensor rotations', 0, None),
    Feature('Other', 'filter', 'AP_FILTER_ENABLED', 'Enable PID filtering', 0, None),
    Feature('Other', 'ac-polyfence-circle-int-support', 'AC_POLYFENCE_CIRCLE_INT_SUPPORT_ENABLED', 'Fence circle compatability', 0, None),  # NOQA:E501
    Feature('Other', 'adsb-avoidance', 'AP_ADSB_AVOIDANCE_ENABLED', 'Enable "ADSB" Avoidance', 0, 'adsb'),
    Feature('Other', 'cpu-idle-stats', 'AP_CPU_IDLE_STATS_ENABLED', 'Enable CPU idle stats', 0, None), # NOQA:E501

    # MAVLink section for mavlink features and/or message handling,
    # rather than for e.g. mavlink-based sensor drivers
    Feature('MAVLink', 'high-latency2', 'HAL_HIGH_LATENCY2_ENABLED', 'Enable HighLatency2 Support', 0, None),
    Feature('MAVLink', 'ac-polyfence-fence-point-protocol-support', 'AC_POLYFENCE_FENCE_POINT_PROTOCOL_SUPPORT', 'Enable Old MAVLink fence points protocol', 0, "fence"),  # noqa
    Feature('MAVLink', 'mavlink-rally-point-protocol', 'AP_MAVLINK_RALLY_POINT_PROTOCOL_ENABLED', 'Enable Old MAVLink rally points protocol', 0, "rally"),  # noqa
    Feature('MAVLink', 'mavlink-autopilot-version-request', 'AP_MAVLINK_AUTOPILOT_VERSION_REQUEST_ENABLED', 'Enable Old AUTOPILOT_VERSION_REQUEST mesage', 0, None),  # noqa
    Feature('MAVLink', 'mavlink-mav-cmd-request-autopilot-capabilities', 'AP_MAVLINK_MAV_CMD_REQUEST_AUTOPILOT_CAPABILITIES_ENABLED', 'Enable Old REQUEST_AUTOPILOT_CAPABILITIES command', 0, None),  # noqa
    Feature('MAVLink', 'mavlink-msg-relay-status', 'AP_MAVLINK_MSG_RELAY_STATUS_ENABLED', 'Enable Send RELAY_STATUS message', 0, 'relay'),  # noqa
    Feature('MAVLink', 'mavlink-msg-device-op', 'AP_MAVLINK_MSG_DEVICE_OP_ENABLED', 'Enable DeviceOp MAVLink messages', 0, None),  # noqa
    Feature('MAVLink', 'mavlink-servo-relay', 'AP_MAVLINK_SERVO_RELAY_ENABLED', 'Enable ServoRelay MAVLink messages', 0, 'servorelayevents'),  # noqa
    Feature('MAVLink', 'mavlink-msg-serial-control', 'AP_MAVLINK_MSG_SERIAL_CONTROL_ENABLED', 'Enable Serial Control MAVLink messages', 0, None),  # noqa
    Feature('MAVLink', 'mavlink-msg-mission-request', 'AP_MAVLINK_MSG_MISSION_REQUEST_ENABLED', 'Enable MISSION_REQUEST MAVLink messages', 0, None),  # noqa
    Feature('MAVLink', 'mavlink-msg-rc-channels-raw', 'AP_MAVLINK_MSG_RC_CHANNELS_RAW_ENABLED', 'Enable RC_CHANNELS_RAW MAVLink messages', 0, None),  # noqa
    Feature('MAVLink', 'mavlink-ftp', 'AP_MAVLINK_FTP_ENABLED', 'Enable MAVLink FTP protocol', 0, None),  # noqa
    Feature('MAVLink', 'mavlink-mav-cmd-set-hagl', 'AP_MAVLINK_MAV_CMD_SET_HAGL_ENABLED', 'Enable MAVLink HAGL command', 0, None),  # noqa
    Feature('MAVLink', 'mavlink-msg-video-stream-information', 'AP_MAVLINK_MSG_VIDEO_STREAM_INFORMATION_ENABLED', 'Enable MAVLink VIDEO_STREAM_INFORMATION message', 0, "camera"), # noqa
    Feature('Other', 'follow', 'AP_FOLLOW_ENABLED', 'Enable Follow library', 0, None),
    Feature('MAVLink', 'mavlink-msg-flight-information', 'AP_MAVLINK_MSG_FLIGHT_INFORMATION_ENABLED', 'Enable FLIGHT_INFORMATION MAVLink message', 0, None),  # noqa
    Feature('MAVLink', 'mavlink-msg-rangefinder-sending', 'AP_MAVLINK_MSG_RANGEFINDER_SENDING_ENABLED', 'Enable sending of RANGEFINDER mavlink message', 0, "rangefinder"),  # noqa
    Feature('MAVLink', 'mavlink-signing', 'AP_MAVLINK_SIGNING_ENABLED', 'Enable MAVLink2 packet signing and validation', 0, "rangefinder"),  # noqa

    Feature('Developer', 'inertialsensor-kill-imu', 'AP_INERTIALSENSOR_KILL_IMU_ENABLED', 'Allow IMUs to be disabled at runtime', 0, None),  # noqa: E501
    Feature('Developer', 'crashdump', 'AP_CRASHDUMP_ENABLED', 'Enable CrashCatcher', 0, None),

    Feature('GPS Drivers', 'gps-ublox', 'AP_GPS_UBLOX_ENABLED', 'Enable U-blox GPS', 1, None),
    Feature('GPS Drivers', 'gps-sbp2', 'AP_GPS_SBP2_ENABLED', 'Enable SBP2 GPS', 0, 'gps-sbp'),
    Feature('GPS Drivers', 'gps-sbp', 'AP_GPS_SBP_ENABLED', 'Enable SBP GPS', 0, None),
    Feature('GPS Drivers', 'gps-erb', 'AP_GPS_ERB_ENABLED', 'Enable ERB GPS', 0, None),
    Feature('GPS Drivers', 'gps-gsof', 'AP_GPS_GSOF_ENABLED', 'Enable GSOF GPS', 0, None),
    Feature('GPS Drivers', 'gps-nmea', 'AP_GPS_NMEA_ENABLED', 'Enable NMEA GPS', 0, None),
    Feature('GPS Drivers', 'gps-nmea-unicore', 'AP_GPS_NMEA_UNICORE_ENABLED', 'Enable NMEA Unicore GPS', 0, "gps-nmea"),
    Feature('GPS Drivers', 'gps-mav', 'AP_GPS_MAV_ENABLED', 'Enable MAVLink GPS', 0, None),
    Feature('GPS Drivers', 'gps-nova', 'AP_GPS_NOVA_ENABLED', 'Enable NOVA GPS', 0, None),
    Feature('GPS Drivers', 'gps-sbf', 'AP_GPS_SBF_ENABLED', 'Enable SBF GPS', 0, None),
    Feature('GPS Drivers', 'gps-sirf', 'AP_GPS_SIRF_ENABLED', 'Enable SiRF GPS', 0, None),
    Feature('GPS Drivers', 'dronecan-send-gps', 'AP_DRONECAN_SEND_GPS', 'Enable Sending GPS data from Autopilot', 0, "dronecan-drivers"),  # noqa:401
    Feature('GPS Drivers', 'gps-blended', 'AP_GPS_BLENDED_ENABLED', 'Enable GPS Blending', 0, None),


    Feature('Airspeed Drivers', 'airspeed-analog', 'AP_AIRSPEED_ANALOG_ENABLED', 'Enable Analog Airspeed', 0, 'airspeed'),
    Feature('Airspeed Drivers', 'airspeed-asp5033', 'AP_AIRSPEED_ASP5033_ENABLED', 'Enable ASP5033 AIRSPEED', 0, 'airspeed'),  # NOQA: E501
    Feature('Airspeed Drivers', 'airspeed-dlvr', 'AP_AIRSPEED_DLVR_ENABLED', 'Enable DLVR AIRSPEED', 0, 'airspeed'),
    Feature('Airspeed Drivers', 'airspeed-ms4525', 'AP_AIRSPEED_MS4525_ENABLED', 'Enable MS4525 AIRSPEED', 0, 'airspeed'),
    Feature('Airspeed Drivers', 'airspeed-ms5525', 'AP_AIRSPEED_MS5525_ENABLED', 'Enable MS5525 AIRSPEED', 0, 'airspeed'),
    Feature('Airspeed Drivers', 'airspeed-msp', 'AP_AIRSPEED_MSP_ENABLED', 'Enable MSP AIRSPEED', 0, 'airspeed,msp,osd'),
    Feature('Airspeed Drivers', 'airspeed-nmea', 'AP_AIRSPEED_NMEA_ENABLED', 'Enable NMEA AIRSPEED', 0, 'airspeed'),
    Feature('Airspeed Drivers', 'airspeed-sdp3x', 'AP_AIRSPEED_SDP3X_ENABLED', 'Enable SDP3X AIRSPEED', 0, 'airspeed'),
    Feature('Airspeed Drivers', 'airspeed-dronecan', 'AP_AIRSPEED_DRONECAN_ENABLED', 'Enable DroneCAN AIRSPEED', 0, 'airspeed,dronecan-drivers'),   # NOQA: E501
    Feature('Airspeed Drivers', 'airspeed-auav', 'AP_AIRSPEED_AUAV_ENABLED', 'ENABLE AUAV AIRSPEED', 0, 'airspeed'),

    Feature('Actuators', 'servo-telem', 'AP_SERVO_TELEM_ENABLED', 'Enable servo telemetry library', 0, None),
    Feature('Actuators', 'volz', 'AP_VOLZ_ENABLED', 'Enable Volz Protocol', 0, None),
    Feature('Actuators', 'dronecan-volz-feedback', 'AP_DRONECAN_VOLZ_FEEDBACK_ENABLED', 'Enable Volz DroneCAN Feedback', 0, "dronecan-drivers,volz,servo-telem"),  # noqa: E501
    Feature('Actuators', 'robotisservo', 'AP_ROBOTISSERVO_ENABLED', 'Enable RobotisServo protocol', 0, None),
    Feature('Actuators', 'sbusoutput', 'AP_SBUSOUTPUT_ENABLED', 'Enable SBUS output on serial ports', 0, None),
    Feature('Actuators', 'fettec-onewire', 'AP_FETTEC_ONEWIRE_ENABLED', 'Enable FETTec OneWire ESCs', 0, None),
    Feature('Actuators', 'kdecan', 'AP_KDECAN_ENABLED', 'KDE Direct KDECAN ESC', 0, None),
    Feature('Actuators', 'dronecan-himark-servo-support', 'AP_DRONECAN_HIMARK_SERVO_SUPPORT', 'Enable Himark DroneCAN servos', 0, "dronecan-drivers"),  # noqa: E501
    Feature('Actuators', 'dronecan-hobbywing-esc-support', 'AP_DRONECAN_HOBBYWING_ESC_SUPPORT', 'Enable Hobbywing DroneCAN ESCs', 0, "dronecan-drivers"),  # noqa: E501

    Feature('Precision Landing', 'ac-precland', 'AC_PRECLAND_ENABLED', 'Enable Precision landing support', 0, None),
    Feature('Precision Landing', 'ac-precland-mavlink', 'AC_PRECLAND_MAVLINK_ENABLED', 'Enable MAVLink precision landing support', 0, "ac-precland"),  # noqa
    Feature('Precision Landing', 'ac-precland-irlock', 'AC_PRECLAND_IRLOCK_ENABLED', 'Enable IRLock precision landing support', 0, "ac-precland"),  # noqa

    #    Feature('Filesystem', 'filesystem-esp32', 'AP_FILESYSTEM_ESP32_ENABLED', 'Enable ESP32 Filesystem', 0, None),
    # Feature('Filesystem', 'filesystem-fatfs', 'AP_FILESYSTEM_FATFS_ENABLED', 'Enable FATFS Filesystem', 0, None),
    Feature('Filesystem', 'filesystem-mission', 'AP_FILESYSTEM_MISSION_ENABLED', 'Enable @MISSION/ filesystem', 0, None),
    Feature('Filesystem', 'filesystem-param', 'AP_FILESYSTEM_PARAM_ENABLED', 'Enable @PARAM/ filesystem', 0, None),
    #    Feature('Filesystem', 'filesystem-posix', 'AP_FILESYSTEM_POSIX_ENABLED', 'Enable POSIX filesystem', 0, None),
    Feature('Filesystem', 'filesystem-romfs', 'AP_FILESYSTEM_ROMFS_ENABLED', 'Enable @ROMFS/ filesystem', 0, None),
    Feature('Filesystem', 'filesystem-sys', 'AP_FILESYSTEM_SYS_ENABLED', 'Enable @SYS/ filesystem', 0, None),
    Feature('Filesystem', 'force-apj-default-parameters', 'FORCE_APJ_DEFAULT_PARAMETERS', 'Enable apj_tool parameter area', 0, None),  # noqa: E501

    Feature('Networking', 'networking', 'AP_NETWORKING_ENABLED', 'Enable networking', 0, None),
    Feature('Networking', 'networking-backend-ppp', 'AP_NETWORKING_BACKEND_PPP', 'Enable PPP networking', 0, "networking"),
    Feature('Networking', 'networking-can-mcast', 'AP_NETWORKING_CAN_MCAST_ENABLED', 'Enable CAN multicast bridge', 0, "networking,dronecan-drivers"), # noqa
    Feature('Networking', 'networking-capture', 'AP_NETWORKING_CAPTURE_ENABLED', 'Enable network capture', 0, "networking"),

    Feature('CAN', 'dronecan-drivers', 'HAL_ENABLE_DRONECAN_DRIVERS', 'Enable DroneCAN support', 0, None),
    Feature('CAN', 'can-logging', 'AP_CAN_LOGGING_ENABLED', 'Enable CAN logging support', 0, 'logging'),

    Feature('DDS', 'dds', 'AP_DDS_ENABLED', 'Enable MicroXRCE DDS support for ROS 2', 0, None),

]

BUILD_OPTIONS.sort(key=lambda x: (x.category + x.label))

# sanity check the list to ensure names don't get too long.  These are
# used in various displays, so a good English "name" for the feature
# makes sense:
sanity_check_failed = False
for x in BUILD_OPTIONS:
    if len(x.label) > 64:
        sanity_check_failed = True
        print(f"{x.label} is too long")
        sanity_check_failed = True

if sanity_check_failed:
    raise ValueError("Bad labels in Feature list")
