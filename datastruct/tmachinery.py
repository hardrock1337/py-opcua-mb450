class Frequency:
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
    error = ""                  # Reg[32-39]
    errorFreelop = ""           # Reg[40-43]
    errorFdrive = ""            # Reg[44-47] UNUSED
    status = ""                 # Reg[48-55]
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
        self.output_frequency = float((data[21] << 8) + data[22])


class Shearer:
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
    speed = 0.0  # Reg[19,20], uint, 0-250, 0.1m/min 20 registr empty?
    speed_status = 0  # Reg[21], Sstat, 0-15
    current_year = ""  # Reg[22], uchar, 0-99 year
    current_mounth = ""  # Reg[23], uchar, 0-12 mounth
    current_day = ""  # Reg[24], uchar, 1-31 day
    current_hour = ""  # Reg[25], uchar, 0-23 hour
    current_minute = ""  # Reg[26], uchar, 0-59 minute
    current_sec = ""  # Reg[27], uchar, 0-59 second
    management_rele = 0  # Reg[28], uchar, 0-SpeedUP, 1-SpeedDown, 2-GetLeft, 3-GetRight, 4-StopConveyer, 5-NormWorkShearer, 6-OnSignalShearer, 7-StopAutomation
    management_command_panel = 0  # Reg[29], uchar, 0-SpeedUP, 1-SpeedDown, 2-GetLeft, 3-GetRight, 4-StopConveyer, 5-StartShearer, 6-StopAutomation, 7-ButtonStart
    electro_hydro_valve = 0  # Reg[30], uchar
    management_drobilka = 0  # Reg[31], uchar
    sensor_speed = 0  # Reg[32], uchar
    sensor_pologenie = 0  # Reg[33], uchar
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
    voltage_status = 0
    error = ""
    status = ""
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
        self.motor_current_m4 = (data[40] << 8) + data[41]
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
        self.management_command_panel = data[66]
        self.electro_hydro_valve = data[67]
        self.management_drobilka = data[68]
        self.sensor_speed = data[69]
        self.sensor_pologenie = data[70]
        self.operation_mode = data[71]
        self.shearer_type = data[72]
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
        self.error = str(data[117]) + str(data[118]) + str(data[119]) + str(data[125]) + str(data[126]) + str(
            data[127]) + str(data[128]) + str(data[129]) + str(data[130]) + str(data[131]) + str(
            data[137]) + str(data[138])
        self.status = str(data[139]) + str(data[140]) + str(data[141]) + str(data[142])
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
        self.serial_number = "FFFF"

class Tmachinery(Shearer, Frequency):
    def mprint(self, data, fstr):
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