class Tmachinery:
    @staticmethod
    def message_print(data, fstr):
        """Print original message in terminal"""
        j = 0
        print("\nMessage count bytes:", len(data))
        for i in data:
            fstr.append(i)
            j = j + 1
            if (j % 12 == 0):
                print("{0}".format(i), end="\n")
            else:
                print("{0}".format(i), end=" ")

    def parserdata(self):
        """Parsing information by bits"""

class Frequency(Tmachinery):
    """The frequency convertor data transmission protocol is based on the Broadcast Announce Message (BAM) protocol according to SAE J1939/21\n
    The difference is in the transmission speed of 125kBd and bypassing the time lag between packets.
    All CAN messages are 29-bit with 8 byte length.\n
    The first message with ID=0x1C, 0xECFF, 0x91 is a header (TP.CM) containing the shearer data ID=0x1012, length 74\n
    Other messages with ID=0x1C, 0xEBFF, 0x91 are data (TP.DT) and contain the following structure by 7 bytes groups:"""
    data_status = 0  # Reg[0], uchar, 0[bit] - if 1:data valid, 1[bit] - if 1:data simulation
    software_version = 0.0  # Reg[2,3] HL, uchar, 50.17
    output_frequency = 0.0  # Reg[4,5], uint, 0-1200, 0.1Hz
    output_amperage = 0.0   # Reg[6,7], uint, 0-10000, 0.1A
    output_voltage = 0      # Reg[8,9], uint, 0-1000 Volt
    voltage_capacitor = 0   # Reg[10,11], uint, 0-2000 Volt
    sensor_status = 0       # Reg[12], Sstat
    voltage_input = 0       # Reg[13,14], uint, 0-1500 Volt
    sensor_voltage_input_status = 0       # Reg[15], Sstat
    temperature_air_shearer = 0     # Reg[16], uchar, 0-100 Celsiy
    temperature_air_shearer_status = 0  # Reg[17], Sstat
    temperature_modem_shearer = 0  # Reg[18], uchar, 0-100 Celsiy
    temperature_modem_shearer_status = 0  # Reg[19], Sstat
    output_amperage_contactor = 0 # Reg[20,21], uint, 0-1000A
    output_amperage_contactor_status = 0 # Reg[22], Sstat
    temperature_air_frequency = 0 # Reg[23],0-100 Celsiy
    temperature_air_icebox_igbt = 0 # Reg[24], 0-100 Celsiy
    temperature_usmemovace = 0  # Reg[25]  UNUSED
    temperature_brzdy_mf = 0  # Reg[26]  UNUSED
    temperature_mf_status = 0 # Reg[27], Sstat
    number_mfk = ""             # Reg[29,30] 25-xxx, Reg[28,29] xx-673
    error_1 = 0                # Reg[32]
    error_can_led0 = 0         # Reg[32:0]
    error_can_mvv = 0         # Reg[32:1]
    error_can_mz = 0          # Reg[32:0]
    error_can_led0 = 0          # Reg[32:1]
    error_2 = 0                # Reg[33]
    error_3 = 0                # Reg[34]
    error_4 = 0                # Reg[35]
    error_5 = 0                # Reg[36] UNUSED
    error_6 = 0                # Reg[37] UNUSED
    error_7 = 0                # Reg[38] UNUSED
    error_8 = 0                # Reg[39] UNUSED
    errorFreelop_1 = 0         # Reg[40]
    errorFreelop_2 = 0         # Reg[42]
    errorFreelop_3 = 0          # Reg[42]
    errorFreelop_4 = 0          # Reg[43]
    errorFdrive = ""            # Reg[44-47] UNUSED
    mfk_status_1 = 0            # Reg[48]
    mfk_status_2 = 0            # Reg[49]
    mfk_status_3 = 0            # Reg[50]
    mfk_status_4 = 0            # Reg[51]
    mfk_status_5 = 0            # Reg[52]
    mfk_status_6 = 0            # Reg[53]
    mfk_status_7 = 0            # Reg[54]
    mfk_status_8 = 0            # Reg[55]
    mfk_concentration_ch4 = 0      # Reg[56], uchar, CH4  UNUSED
    mfk_concentration_ch4_status = 0  # Reg[57], Sstat  UNUSED
    mfk_material_case = 0       # Reg[58], uchar, UNUSED
    language = 0                # Reg[59], uchar
    mfk_year = 0                # Reg[60], uchar, 0-99
    mfk_mounth = 0              # Reg[61], uchar, 1-12
    mfk_day = 0                 # Reg[62], uchar, 1-31
    mfk_hour = 0                # Reg[63], uchar, 0-23
    mfk_minute = 0              # Reg[64], uchar, 0-59
    mfk_second = 0              # Reg[65], uchar, 0-59
    shearer_year = 0            # Reg[66], uchar, 0-99
    shearer_mounth = 0          # Reg[67], uchar, 1-12
    shearer_day = 0             # Reg[68], uchar, 1-31
    shearer_hour = 0            # Reg[69], uchar, 0-23
    shearer_minute = 0          # Reg[70], uchar, 0-59
    shearer_second = 0          # Reg[71], uchar, 0-59
    mfk_number_section = 0      # Reg[72], uchar, 1-250
    mfk_number_section_status = 0  # Reg[73], Sstat

    def mfk400(self, data):
        """MFK400.SNO, CAN data protocol"""
        self.data_status = data[17]
        self.software_version = float(str(data[19]) + "." + str(data[20]))
        self.output_frequency = float((data[21] << 8) + data[22])/10
        self.output_amperage = float((data[23] << 8) + data[29])/10
        self.output_voltage = (data[30] << 8) + data[31]
        self.voltage_capacitor = (data[32] << 8) + data[33]
        self.sensor_status = data[34]
        self.voltage_input = (data[35] << 8) + data[41]
        self.sensor_voltage_input_status = data[42]
        self.temperature_air_shearer = data[43]
        self.temperature_air_shearer_status = data[44]
        self.temperature_modem_shearer = data[45]
        self.temperature_modem_shearer_status = data[46]
        self.output_amperage_contactor = (data[47] << 8) + data[53]
        self.output_amperage_contactor_status = data[54]
        self.temperature_air_frequency = data[55]
        self.temperature_air_icebox_igbt = data[56]
        self.temperature_usmemovace = data[57]
        self.temperature_brzdy_mf = data[58]
        self.temperature_mf_status = data[59]
        self.number_mfk = str((data[65] << 8) + data[66]) + "-" + str((data[67] << 8) + data[68])
        self.error_1 = data[69]
        self.error_2 = data[70]
        self.error_3 = data[71]
        self.error_4 = data[72]
        #self.error_5 = data[77]
        #self.error_6 = data[78]
        #self.error_7 = data[79]
        #self.error_8 = data[80]
        self.errorFreelop_1 = data[82]
        self.errorFreelop_2 = data[83]
        self.errorFreelop_3 = data[89]
        self.errorFreelop_4 = data[90]
        self.errorFdrive = str(data[91]) + str(data[92]) + str(data[93]) +str(data[94])
        self.mfk_status_1 = data[95]
        self.mfk_status_2 = data[101]
        self.mfk_status_3 = data[102]
        self.mfk_status_4 = data[103]
        self.mfk_status_5 = data[104]
        self.mfk_status_6 = data[105]
        self.mfk_status_7 = data[106]
        self.mfk_status_8 = data[107]
        self.mfk_concentration_ch4 = data[113]
        self.mfk_concentration_ch4_status = data[114]
        self.mfk_material_case = data[115]
        self.language = data[116]
        self.mfk_year = data[117]
        self.mfk_mounth = data[118]
        self.mfk_day = data[119]
        self.mfk_hour = data[125]
        self.mfk_minute = data[126]
        self.mfk_second = data[127]
        self.shearer_year = data[128]
        self.shearer_mounth = data[129]
        self.shearer_day = data[130]
        self.shearer_hour = data[131]
        self.shearer_minute = data[137]
        self.shearer_second = data[138]
        self.mfk_number_section = data[139]
        self.mfk_number_section_status = data[140]

class Shearer(Tmachinery):
    """The shearer data transmission protocol is based on the Broadcast Announce Message (BAM) protocol according to SAE J1939/21\n
    The difference is in the transmission speed of 125kBd and bypassing the time lag between packets.
    All CAN messages are 29-bit with 8 byte length.\n
    The first message with ID=0x1C, 0xECFF, 0x91 is a header (TP.CM) containing the shearer data ID=0x1010, length 86 or 92byte (according to SW version)\n
    Other messages with ID=0x1C, 0xEBFF, 0x91 are data (TP.DT) and contain the following structure by 7 bytes groups"""
    data_status = 0  # Reg[0], uchar, 0 - data valid, 1 - data simulation
    software_version = 0.0  # Reg[2,3] HL, uchar, 7.11
    motor_current_m1 = 0  # Reg[4,5], uint, 0-1000 Amper
    motor_status_m1 = 0  # Reg[6], Sstat, 0-15
    motor_current_m2 = 0  # Reg[7,8], uint, 0-1000 Amper
    motor_status_m2 = 0  # Reg[9], Sstat, 0-15
    motor_current_m3 = 0  # Reg[10,11], uint, 0-1000 Amper
    motor_status_m3 = 0  # Reg[12], Sstat, 0-15
    motor_current_m4 = 0  # Reg[13,14], uint, 0-1000 Amper
    motor_status_m4 = 0  # Reg[15], Sstat, 0-15
    motor_current_m5 = 0  # Reg[16,17], uint, 0-1000 Amper
    motor_status_m5 = 0  # Reg[18], Sstat, 0-15
    speed = 0.0  # Reg[19,20], uint, 0-250, 0.1m/min
    speed_status = 0  # Reg[21], Sstat, 0-15
    current_year = ""  # Reg[22], uchar, 0-99 year
    current_mounth = ""  # Reg[23], uchar, 0-12 mounth
    current_day = ""  # Reg[24], uchar, 1-31 day
    current_hour = ""  # Reg[25], uchar, 0-23 hour
    current_minute = ""  # Reg[26], uchar, 0-59 minute
    current_sec = ""  # Reg[27], uchar, 0-59 second
    management_rele = 0  # Reg[28], uchar
    management_rele_Rplus = 0  # Reg[28:0]
    management_rele_Rminus = 0  # Reg[28:1]
    management_rele_SML = 0  # Reg[28:2]
    management_rele_SMP = 0  # Reg[28:3]
    management_rele_stop_konv = 0  # Reg[28:4]
    management_rele_shearer_work_mode = 0  # Reg[28:5]
    management_rele_shearer_signal_on = 0  # Reg[28:6]
    management_rele_stop_auto = 0  # Reg[28:7]
    management_command_panel = 0  # Reg[29], uchar
    management_command_Rplus = 0  # Reg[29:0]
    management_command_Rminus = 0  # Reg[29:1]
    management_command_SML = 0  # Reg[29:2]
    management_command_SMP = 0  # Reg[29:3]
    management_command_stop_konv = 0  # Reg[29:4]
    management_command_shearer_on = 0  # Reg[29:5]
    management_command_stop_auton = 0  # Reg[29:6]
    management_command_start_button = 0  # Reg[29:7]
    electro_hydro_valve = 0  # Reg[30], uchar
    electro_hydro_valve_brz2 = 0  # Reg[30:0]
    electro_hydro_valve_spol = 0  # Reg[30:1]
    electro_hydro_valve_vf1 = 0  # Reg[30:2]
    electro_hydro_valve_vf2 = 0  # Reg[30:3]
    electro_hydro_valve_rpn = 0  # Reg[30:4]
    electro_hydro_valve_rpd = 0  # Reg[30:5]
    electro_hydro_valve_rln = 0  # Reg[30:6]
    electro_hydro_valve_rld = 0  # Reg[30:7]
    management_drobilka = 0  # Reg[31], uchar
    management_drobilka_dn = 0  # Reg[31:0]
    management_drobilka_dd = 0  # Reg[31:1]
    management_drobilka_kn = 0  # Reg[31:2]
    management_drobilka_kd = 0  # Reg[31:3]
    management_drobilka_spp = 0  # Reg[31:4]
    management_drobilka_spl = 0  # Reg[31:5]
    management_drobilka_sll = 0  # Reg[31:6]
    management_drobilka_slp = 0  # Reg[31:7]
    speed_direction = 0  # Reg[32], uchar
    speed_direction_status_sensor_speed = 0  # Reg[32:0]
    speed_direction_status_sensor_direction = 0  # Reg[32:1]
    speed_direction_error_communicate = 0  # Reg[32:2]
    speed_direction_enable = 0  # Reg[32:3]
    speed_direction_move_shearer_left = 0  # Reg[32:4]
    speed_direction_move_shearer_right = 0  # Reg[32:5]
    sensor_pologenie = 0  # Reg[33], uchar
    sensor_pologenie_status_sensor_1 = 0  # Reg[33:0]
    sensor_pologenie_status_sensor_2 = 0  # Reg[33:1]
    sensor_pologenie_error_communicate = 0  # Reg[33:2]
    sensor_pologenie_enable = 0  # Reg[33:3]
    sensor_pologenie_activity_memory = 0  # Reg[33:4]
    sensor_pologenie_extended_status = 0  # Reg[33:5]
    sensor_pologenie_concentrator = 0  # Reg[33:7]
    operation_mode = 0  # Reg[34], uchar
    shearer_type = 0  # Reg[35], uchar
    reason_off = 0  # Reg[36], uchar
    traversed_path = ""  # Reg[38,39,40,41], ulong
    traversed_path_status = 0  # Reg[42], Sstat
    position = ""  # Reg[43, 44, 45, 46], slong
    position_status = 0  # Reg[47], Sstat
    time_work = ""  # Reg[48,49,50,51], ulong
    time_work_status = 0  # Reg[52], Sstat
    speed_regulation = 0.0  # Reg[53], uchar, 0 - 150, 0.1m/min
    speed_regulation_status = 0  # Reg[54], Sstat
    position_number_section = 0  # Reg[55], uchar, 0 - 250
    position_number_section_status = 0  # Reg[56], Sstat
    voltage = 0  # Reg[57,58], uint, 0 - 1500
    voltage_status = 0  # Reg[59], Sstat
    error_1 = 0      # Reg[60]
    error_overload_m1 = 0  # Reg[60:0]
    error_overload_m2 = 0  # Reg[60:1]
    error_overload_m3 = 0  # Reg[60:2]
    error_overload_m4 = 0  # Reg[60:3]
    error_overload_m5 = 0  # Reg[60:4]
    error_overload_m6 = 0  # Reg[60:5] UNUSED
    error_overheat_m1 = 0  # Reg[60:6]
    error_overheat_m2 = 0  # Reg[60:7]
    error_2 = 0      # Reg[61]
    error_overheat_m3 = 0  # Reg[61:0]
    error_overheat_m4 = 0  # Reg[61:1]
    error_overheat_m5 = 0  # Reg[61:2]
    error_2_overheat_m6 = 0  # Reg[61:3] UNUSED
    error_leak_m1 = 0  # Reg[61:4]
    error_leak_m2 = 0  # Reg[61:5]
    error_leak_m5 = 0  # Reg[61:6]
    error_leak_m6 = 0  # Reg[61:7] UNUSED
    error_3 = 0      # Reg[62]
    error_cv1 = 0  # Reg[62:0]
    error_cv2 = 0  # Reg[62:1]
    error_sensor_oil_level = 0  # Reg[62:2]
    error_sensor_dirty_suction_filter = 0  # Reg[62:3]
    error_sensor_pressure_filter = 0  # Reg[62:4]
    error_sensor_drain_filter = 0  # Reg[62:5]
    error_sensor_CH4_TMRK = 0  # Reg[62:6]
    error_brake_failure = 0  # Reg[62:7] UNUSED
    error_4 = 0      # Reg[63]
    error_fail_management = 0  # Reg[63:0]
    error_sensor_amper_lem1 = 0  # Reg[63:1]
    error_sensor_amper_lem2 = 0  # Reg[63:2]
    error_sensor_amper_lem3 = 0  # Reg[63:3]
    error_sensor_amper_lem4 = 0  # Reg[63:4]
    error_sensor_amper_lem5 = 0  # Reg[63:5]
    error_sensor_amper_lem6 = 0  # Reg[63:6] UNUSED
    error_fail_module_can11_vana = 0  # Reg[63:7]
    error_5 = 0      # Reg[64]
    error_fail_module_mcv1 = 0  # Reg[64:0]
    error_fail_module_mcp1 = 0  # Reg[64:1]
    error_fail_module_mcd1 = 0  # Reg[64:2]
    error_fail_module_mco1 = 0  # Reg[64:3]
    error_fail_module_mco2 = 0  # Reg[64:4]
    error_fail_module_mco3 = 0  # Reg[64:5]
    error_fail_module_mco4 = 0  # Reg[64:6]
    error_fail_module_mco5 = 0  # Reg[64:7]
    error_6 = 0      # Reg[65]
    error_fail_module_mco6 = 0  # Reg[65:0] UNUSED
    error_fail_module_memory = 0  # Reg[65:1]
    error_command_stop_from_remote_control_transmission = 0  # Reg[65:2]
    error_fail_module_can_remote_control_transmission = 0  # Reg[65:3]
    error_parameter_failure = 0  # Reg[65:4]
    error_button_stop = 0  # Reg[65:5]
    error_uninhibited = 0  # Reg[65:6]
    error_stop_overload_regulation_m1_m2 = 0  # Reg[65:7]
    error_7 = 0      # Reg[66]
    error_no_direction = 0  # Reg[66:0]
    error_shearer_not_accelerate_overload_regulation_m3_m4 = 0  # Reg[66:1]
    error_off_from_pv5 = 0  # Reg[66:2]
    error_off_from_pv4 = 0  # Reg[66:3]
    error_fail_modem_mdm = 0  # Reg[66:4]
    error_overheat_modem_mdm = 0  # Reg[66:5]
    error_off_m1_from_regulation = 0  # Reg[66:6]
    error_off_m2_from_regulation = 0  # Reg[66:7]
    error_8 = 0      # Reg[67]
    error_feed_block = 0  # Reg[67:0]
    error_9 = 0      # Reg[68]
    error_fail_contactor_m1 = 0  # Reg[68:0]
    error_fail_contactor_m2 = 0  # Reg[68:1]
    error_fail_contactor_m5 = 0  # Reg[68:2]
    error_fail_contactor_m6 = 0  # Reg[68:3] UNUSED
    error_10 = 0     # Reg[69]
    error_no_supply_current = 0  # Reg[69:4]
    error_short_stop = 0  # Reg[69:5]
    error_bad_feed_direction = 0  # Reg[69:6]
    error_not_power_24V_ACV = 0  # Reg[69:7]
    error_11 = 0     # Reg[70]
    error_fail_sensor_amper_1 = 0  # Reg[70:0]
    error_fail_sensor_amper_2 = 0  # Reg[70:1]
    error_fail_sensor_amper_3 = 0  # Reg[70:2]
    error_fail_sensor_amper_4 = 0  # Reg[70:3]
    error_fail_sensor_amper_5 = 0  # Reg[70:4]
    error_fail_sensor_amper_6 = 0  # Reg[70:5] UNUSED
    error_no_variable_cef_mco1 = 0  # Reg[70:6]
    error_no_variable_cef_mco2 = 0  # Reg[70:7]
    error_12 = 0     # Reg[71]
    error_no_variable_cef_mco3 = 0  # Reg[71:0]
    error_no_variable_cef_mco4 = 0  # Reg[71:1]
    error_no_variable_cef_mco5 = 0  # Reg[71:2]
    error_no_variable_cef_mco6 = 0  # Reg[71:3] UNUSED
    error_not_voltage230v_mco1 = 0  # Reg[71:4]
    error_not_voltage230v_mco2 = 0  # Reg[71:5]
    error_not_voltage230v_mco5 = 0  # Reg[71:6]
    error_not_voltage230v_mco6 = 0  # Reg[71:7]
    status_1 = 0     # Reg[72]
    status_start_m1 = 0  # Reg[72:0]
    status_start_m2 = 0  # Reg[72:1]
    status_start_m5 = 0  # Reg[72:2]
    status_start_m6 = 0  # Reg[72:3]
    status_m1_failure_is_over = 0  # Reg[72:4]
    status_m2_failure_is_over = 0  # Reg[72:5]
    status_m5_failure_is_over = 0  # Reg[72:6]
    status_m6_failure_is_over = 0  # Reg[72:7]
    status_2 = 0     # Reg[73]
    status_contactor_1_on = 0  # Reg[73:0]
    status_contactor_2_on = 0  # Reg[73:1]
    status_contactor_3_on = 0  # Reg[73:2]
    status_short_circuit_m1 = 0  # Reg[73:3]
    status_short_circuit_m2 = 0  # Reg[73:4]
    status_short_circuit_m5 = 0  # Reg[73:5]
    status_button_stop_left = 0  # Reg[73:6]
    status_button_stop_right = 0  # Reg[73:7]
    status_3 = 0     # Reg[74]
    status_m1_off_signal_stop = 0  # Reg[74:0]
    status_m2_off_signal_stop = 0  # Reg[74:1]
    status_m5_off_signal_stop = 0  # Reg[74:2]
    status_lower_brake_pressure_sensor_50bar = 0  # Reg[74:3]
    status_upper_brake_pressure_sensor_100bar = 0  # Reg[74:4]
    status_not_power_can12_24v = 0  # Reg[74:5]
    status_4 = 0     # Reg[75]
    status_module_management_mco6_allow = 0  # Reg[75:0]
    status_module_converter_mcp_allow = 0  # Reg[75:1]
    status_module_valve_mcv_allow = 0  # Reg[75:2]
    status_block_move_shearer_pv5 = 0  # Reg[75:5]
    status_block_start_shearer_pv4 = 0  # Reg[75:6]
    status_support_start_button_shearer = 0  # Reg[75:7]
    level_defence_m1 = 0  # Reg[76], uchar, 0 - 250
    level_defence_status_m1 = 0  # Reg[77], Sstat
    level_defence_m2 = 0  # Reg[78], uchar, 0 - 250
    level_defence_status_m2 = 0  # Reg[79], Sstat
    level_defence_m3 = 0  # Reg[80], uchar, 0 - 250
    level_defence_status_m3 = 0  # Reg[81], Sstat
    level_defence_m4 = 0  # Reg[82], uchar, 0 - 250
    level_defence_status_m4 = 0  # Reg[83], Sstat
    level_defence_m5 = 0  # Reg[84], uchar, 0 - 250
    level_defence_status_m5 = 0  # Reg[85], Sstat
    serial_number = 0  # 0 - 99, 000 - 999

    def shearer_data(self, data):
        """MB320, MB450 shearer CAN data protocol"""
        self.data_status = data[17]
        self.software_version = float(str(data[19]) + "." + str(data[20]))
        self.motor_current_m1 = (data[21] << 8) + data[22]
        self.motor_status_m1 = data[23]
        self.motor_current_m2 = (data[29] << 8) + data[30]
        self.motor_status_m2 = data[31]
        self.motor_current_m3 = (data[32] << 8) + data[33]
        self.motor_status_m3 = data[34]
        self.motor_current_m4 = (data[35] << 8) + data[41]
        self.motor_status_m4 = data[42]
        self.motor_current_m5 = (data[43] << 8) + data[44]
        self.motor_status_m5 = data[45]
        self.speed = ((data[46] << 8) + data[47]) / 10
        self.speed_status = data[53]
        self.current_year = data[54]
        self.current_mounth = data[55]
        self.current_day = data[56]
        self.current_hour = data[57]
        self.current_minute = data[58]
        self.current_sec = data[59]
        self.management_rele = data[65]
        self.management_rele_Rplus = 0  # Reg[28:0]
        self.management_rele_Rminus = 0  # Reg[28:1]
        self.management_rele_SML = 0  # Reg[28:2]
        self.management_rele_SMP = 0  # Reg[28:3]
        self.management_rele_stop_konv = 0  # Reg[28:4]
        self.management_rele_shearer_work_mode = 0  # Reg[28:5]
        self.management_rele_shearer_signal_on = 0  # Reg[28:6]
        self.management_rele_stop_auto = 0  # Reg[28:7]
        self.management_command_panel = data[66]
        self.electro_hydro_valve = data[67]
        self.management_drobilka = data[68]
        self.sensor_speed = data[69]
        self.sensor_pologenie = data[70]
        self.operation_mode = data[71]
        self.shearer_type = data[77]
        self.reason_off = data[78]
        self.traversed_path = (data[80] << 24) + (data[81] << 16) + (data[82] << 8) + data[83]
        self.traversed_path_status = data[89]
        self.position = (data[90] << 24) + (data[91] << 16) + (data[92] << 8) + data[93]
        self.position_status = data[94]
        self.time_work = (data[95] << 24) + (data[101] << 16) + (data[102] << 8) + data[103]
        self.time_work_status = data[104]
        self.speed_regulation = data[105]
        self.speed_regulation_status = data[106]
        self.position_number_section = data[107]
        self.position_number_section_status = data[113]
        self.voltage = (data[114] << 8) + data[115]
        self.voltage_status = data[116]
        self.error_1 = data[117]
        self.error_2 = data[118]
        self.error_3 = data[119]
        self.error_4 = data[125]
        self.error_5 = data[126]
        self.error_6 = data[127]
        self.error_7 = data[128]
        self.error_8 = data[129]
        self.error_9 = data[130]
        self.error_10 = data[131]
        self.error_11 = data[137]
        self.error_12 = data[138]
        self.status_1 = data[139]
        self.status_2 = data[140]
        self.status_3 = data[141]
        self.status_4 = data[142]
        self.level_defence_m1 = data[143]
        self.level_defence_status_m1 = data[149]
        self.level_defence_m2 = data[150]
        self.level_defence_status_m2 = data[151]
        self.level_defence_m3 = data[152]
        self.level_defence_status_m3 = data[153]
        self.level_defence_m4 = data[154]
        self.level_defence_status_m4 = data[155]
        self.level_defence_m5 = data[161]
        self.level_defence_status_m5 = data[162]
        self.serial_number = (data[163] << 8) + data[164]

