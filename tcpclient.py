import socket


TCP_IP = '192.168.11.91'
TCP_PORT = 1500
BUFFER_SIZE = 4096
j = 0

fstr = []
mstr = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)
s.close()

"""MB320, MB430, shearer CAN data protocol"""
shearer_data_status = 0         # Reg[0], uchar, 0 - data valid, 1 - data simulation
shearer_software_version = ""   # Reg[2,3] HL, uchar, 7.11
shearer_motor_current_m1 = 0    # Reg[4,5], uint, 0-1000 Amper
shearer_motor_status_m1 = 0     # Reg[6], Sstat, 0-15
shearer_motor_current_m2 = 0    # Reg[7,8], uint, 0-1000 Amper
shearer_motor_status_m2 = 0     # Reg[9], Sstat, 0-15
shearer_motor_current_m3 = 0    # Reg[10,11], uint, 0-1000 Amper
shearer_motor_status_m3 = 0     # Reg[12], Sstat, 0-15
shearer_motor_current_m4 = 0    # Reg[13,14], uint, 0-1000 Amper
shearer_motor_status_m4 = 0     # Reg[15], Sstat, 0-15
shearer_motor_current_m5 = 0    # Reg[16,17], uint, 0-1000 Amper
shearer_motor_status_m5 = 0     # Reg[18], Sstat, 0-15
shearer_speed = 0.0             # Reg[19,20], uint, 0-250, 0.1m/min 20 registr empty?
shearer_speed_status = 0        # Reg[21], Sstat, 0-15
shearer_current_year = ""       # Reg[22], uchar, 0-99 year
shearer_current_mounth = ""     # Reg[23], uchar, 0-12 mounth
shearer_current_day = ""        # Reg[24], uchar, 1-31 day
shearer_current_hour = ""       # Reg[25], uchar, 0-23 hour
shearer_current_minute = ""     # Reg[26], uchar, 0-59 minute
shearer_current_sec = ""        # Reg[27], uchar, 0-59 second
shearer_management_rele = 0     # Reg[28], uchar, 0-SpeedUP, 1-SpeedDown, 2-GetLeft, 3-GetRight, 4-StopConveyer, 5-NormWorkShearer, 6-OnSignalShearer, 7-StopAutomation
shearer_management_command_panel = 0    # Reg[29], uchar, 0-SpeedUP, 1-SpeedDown, 2-GetLeft, 3-GetRight, 4-StopConveyer, 5-StartShearer, 6-StopAutomation, 7-ButtonStart
shearer_electro_hydro_valve = 0 # Reg[30], uchar
shearer_management_drobilka = 0 # Reg[31], uchar
shearer_sensor_speed = 0        # Reg[32], uchar
shearer_sensor_pologenie = 0    # Reg[33], uchar
shearer_operation_mode = 0      # Reg[34], uchar
shearer_type = 0                # Reg[35], uchar
shearer_reason_off = 0          # Reg[36], uchar
shearer_traversed_path = 0      # Reg[38,39,40,41], ulong
shearer_traversed_path_status = 0   # Reg[42], Sstat
shearer_postion = 0             # Reg[43, 44, 45, 46], slong
shearer_position_status = 0     # Reg[47], Sstat
shearer_time_work = 0           # Reg[48,49,50,51], ulong
shearer_time_work_status = 0    # Reg[52], Sstat
shearer_speed_regulation = 0.0  # Reg[53], uchar, 0 - 150, 0.1m/min
shearer_speed_regulation_status = 0 # Reg[54], Sstat
shearer_postion_number_section = 0  # Reg[55], uchar, 0 - 250
shearer_postion_number_section_status= 0 # Reg[56], Sstat
shearer_voltage = 0             # Reg[57,58], uint, 0 - 1500
shearer_level_defence_m1 = 0    # Reg[76], uchar, 0 - 250
shearer_level_defence_status_m1 = 0 # Reg[77], Sstat
shearer_level_defence_m2 = 0    # Reg[78], uchar, 0 - 250
shearer_level_defence_status_m2 = 0 # Reg[79], Sstat
shearer_level_defence_m3 = 0    # Reg[80], uchar, 0 - 250
shearer_level_defence_status_m3 = 0 # Reg[81], Sstat
shearer_level_defence_m4 = 0    # Reg[82], uchar, 0 - 250
shearer_level_defence_status_m4 = 0 # Reg[83], Sstat
shearer_level_defence_m5 = 0    # Reg[84], uchar, 0 - 250
shearer_level_defence_status_m5 = 0 # Reg[85], Sstat
shearer_serial_number = 0    # 0 - 99, 000 - 999

def mprint():
    j = 0
    print("Message count bytes:", len(data))
    for i in data:
        fstr.append(i)
        j = j + 1
        if (j % 12 == 0):
            print("{0}".format(i), end="\n")
        else: print("{0}".format(i), end=" ")

def parser_shearer():
    """TO DO"""
    mprint()
    print("shearer_data_status = ",data[17])
    print("shearer_software_version = ",str(data[19]) + "." + str(data[20]))
    print("shearer_motor_current_m1 = ",str(data[21]) + str(data[22]))
    print("shearer_motor_status_m1 = ",data[23])
    print("shearer_motor_current_m2 = ",str(data[29]) + str(data[30]))
    print("shearer_motor_status_m2 = ", data[31])
    print("shearer_motor_current_m3 = ", str(data[32]) + str(data[33]))
    print("shearer_motor_status_m3 = ", data[34])
    print("shearer_motor_current_m4 = ", str(data[35]) + str(data[41]))
    print("shearer_motor_status_m4 = ", data[42])
    print("shearer_motor_current_m5 = ", str(data[43]) + str(data[44]))
    print("shearer_motor_status_m5 = ", data[45])
    print("shearer_speed = ", str(data[46]) + str(data[47]))  # 0-250, 0.1m/min
    print("shearer_speed_status = ", data[53])
    print("shearer_current_year = ", data[54])
    print("shearer_current_mounth = ", data[55])
    print("shearer_current_day = ", data[56])
    print("shearer_current_hour = ", data[57])
    print("shearer_current_minute = ", data[58])
    print("shearer_current_sec = ", data[59])
    print("shearer_management_rele = ", data[65])
    print("shearer_management_command_panel = ", data[66])
    print("shearer_electro_hydro_valve = ", data[67])
    print("shearer_management_drobilka = ", data[68])
    print("shearer_sensor_speed = ", data[69])
    print("shearer_operation_mode = ", data[70])
#    print("shearer_type = ", data)
#    print("shearer_reason_off = ",  mstr[6][1])
#    print("shearer_traversed_path = ",  mstr[6][3] +  mstr[6][4] +  mstr[6][5] +  mstr[6][6])
#    print("shearer_postion = ", mstr[7][2])
#    print("shearer_time_work = ",  mstr[8][0] + mstr[8][1] + mstr[8][2] + mstr[8][3])
#    print("shearer_speed_regulation = ", mstr[8][4]/10)  # 0 - 150, 0.1m/min
#    print("shearer_postion_number_section = ", mstr[8][6])  # 0 - 250
#    print("shearer_voltage = ", str(mstr[9][0]) + str(mstr[9][1]))  # 0 - 1500
#    print("shearer_level_defence_m1 = ", mstr[11][5])  # 0 - 250
#    print("shearer_level_defence_status_m1 = ", mstr[11][6])
#    print("shearer_level_defence_m2 = ", mstr[12][0]) # 0 - 250
#    print("shearer_level_defence_status_m2 = ", mstr[12][1])
#    print("shearer_level_defence_m3 = ", mstr[12][2])
#    print("shearer_level_defence_status_m3 = ", mstr[12][3])
#    print("shearer_level_defence_m4 = ", mstr[12][4])
#    print("shearer_level_defence_status_m4 = ", mstr[12][5])
#    print("shearer_level_defence_m5 = ", mstr[12][6])
    #print("shearer_level_defence_status_m5 = ", mstr[13][0])
    #print("shearer_serial_number = ", mstr[13][1] + " " + mstr[13][2])

def parser_frequence():
    mprint()

def head_check():
    """From message andsudo """
    if data[9] == 16 and data[10] == 16:
        parser_shearer()
    elif data[9] == 18 and data[10] == 18:
        parser_frequence()
    else:
        mprint()

head_check()
#print("Count messages", mstr.__len__())
