import socket

TCP_IP = '192.168.11.92'
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
shearer_data_status = 0  # 0 - data valid, 1 - data simulation
shearer_software_version = ""  # 7.11
shearer_motor_current_m1 = 0  # 0-1000 Amper
shearer_motor_status_m1 = 0
shearer_motor_current_m2 = 0  # 0-1000 Amper
shearer_motor_status_m2 = 0
shearer_motor_current_m3 = 0  # 0-1000 Amper
shearer_motor_status_m3 = 0
shearer_motor_current_m4 = 0  # 0-1000 Amper
shearer_motor_status_m4 = 0
shearer_motor_current_m5 = 0  # 0-1000 Amper
shearer_motor_status_m5 = 0
shearer_speed = 0.0  # 0-250, 0.1m/min
shearer_management_rele = 0
shearer_management_command_panel = 0
shearer_electro_hydro_valve = 0
shearer_management_drobilka = 0
shearer_sensor_speed = 0
shearer_operation_mode = 0
shearer_type = 0
shearer_reason_off = 0
shearer_traversed_path = 0  # m
shearer_postion = 0
shearer_time_work = 0
shearer_speed_regulation = 0.0  # 0 - 150, 0.1m/min
shearer_postion_number_section = 0  # 0 - 250
shearer_voltage = 0  # 0 - 1500
shearer_level_defence_m1 = 0  # 0 - 250
shearer_level_defence_status_m1 = 0
shearer_level_defence_m2 = 0  # 0 - 250
shearer_level_defence_status_m2 = 0
shearer_level_defence_m3 = 0  # 0 - 250
shearer_level_defence_status_m3 = 0
shearer_level_defence_m4 = 0  # 0 - 250
shearer_level_defence_status_m4 = 0
shearer_level_defence_m5 = 0  # 0 - 250
shearer_level_defence_status_m5 = 0
shearer_serial_number = 0  # 0 - 99, 000 - 999


def head_dev(i):
    """Îïðåäåëÿåì çàãîëîâîê óñòðîéñòâà"""
    if (i[0] == 28 and i[1] == 236 and i[2] == 255 and i[3] == 145) and i[9] == 16 and i[10] == 16:
        return "Data shearer:"
    elif (i[0] == 28 and i[1] == 236 and i[2] == 255 and i[3] == 145) and i[9] == 18 and i[10] == 16:
        return "Data fequency:"
    else:
        return "Unknown device:"


def head_remove(i):
    """Óäàëÿåì çàãîëîâêè"""
    if (i[0] == 28 and (i[1] == 235 or i[1] == 236) and i[2] == 255 and i[3] == 145):
        i.pop(0)
        i.pop(0)
        i.pop(0)
        i.pop(0)
        i.pop(0)
    return i


def shearer(mstr):
    """Îáðàáîò÷èê èíôîðìàöèè ñ êîìáàéíà"""
    for i in mstr:
        head_remove(i)
        # for j in
        print(i)
    print("shearer_data_status = ", mstr[1][0])
    print("shearer_software_version = ", str(mstr[1][2]) + "." + str(mstr[1][3]))
    print("shearer_motor_current_m1 = ", mstr[1][4] + mstr[1][5])
    print("shearer_motor_status_m1 = ", mstr[1][6])
    print("shearer_motor_current_m2 = ", mstr[2][0] + mstr[2][1])
    print("shearer_motor_status_m2 = ", mstr[2][2])
    print("shearer_motor_current_m3 = ", mstr[2][3] + mstr[2][4])
    print("shearer_motor_status_m3 = ", mstr[2][5])
    print("shearer_motor_current_m4 = ", mstr[2][6] + mstr[3][0])
    print("shearer_motor_status_m4 = ", mstr[3][1])
    print("shearer_motor_current_m5 = ", mstr[3][2] + mstr[3][3])
    print("shearer_motor_status_m5 = ", mstr[3][4])
    print("shearer_speed = ", mstr[3][5] + mstr[3][6] / 10)  # 0-250, 0.1m/min
    print("shearer_management_rele = ", mstr[5][0])
    print("shearer_management_command_panel = ", mstr[5][1])
    print("shearer_electro_hydro_valve = ", mstr[5][2])
    print("shearer_management_drobilka = ", mstr[5][3])
    print("shearer_sensor_speed = ", mstr[5][4])
    print("shearer_operation_mode = ", mstr[5][6])
    print("shearer_type = ", mstr[6][0])
    print("shearer_reason_off = ", mstr[6][1])
    print("shearer_traversed_path = ", mstr[6][3] + mstr[6][4] + mstr[6][5] + mstr[6][6])
    print("shearer_postion = ", mstr[7][2])
    print("shearer_time_work = ", mstr[8][0] + mstr[8][1] + mstr[8][2] + mstr[8][3])
    print("shearer_speed_regulation = ", mstr[8][4] / 10)  # 0 - 150, 0.1m/min
    print("shearer_postion_number_section = ", mstr[8][6])  # 0 - 250
    print("shearer_voltage = ", str(mstr[9][0]) + str(mstr[9][1]))  # 0 - 1500
    print("shearer_level_defence_m1 = ", mstr[11][5])  # 0 - 250
    print("shearer_level_defence_status_m1 = ", mstr[11][6])
    print("shearer_level_defence_m2 = ", mstr[12][0])  # 0 - 250
    print("shearer_level_defence_status_m2 = ", mstr[12][1])
    print("shearer_level_defence_m3 = ", mstr[12][2])
    hello
    world

    print("shearer_level_defence_status_m3 = ", mstr[12][3])
    print("shearer_level_defence_m4 = ", mstr[12][4])
    print("shearer_level_defence_status_m4 = ", mstr[12][5])
    print("shearer_level_defence_m5 = ", mstr[12][6])
    # print("shearer_level_defence_status_m5 = ", mstr[13][0])
    # print("shearer_serial_number = ", mstr[13][1] + " " + mstr[13][2])


def fequency(mstr):
    """Îáðàáîò÷èê èíôîðìàöèè ñ ÷àñòîòíèêà"""
    # for i in mstr:
    print("Fequency message")


for i in data:
    j = j + 1
    fstr.append(i)
    if (j % 12 == 0):
        mstr.append(fstr[:])
        fstr.clear()
if (head_dev(mstr[0]) == "Data shearer:"):
    shearer(mstr)
elif (head_dev(mstr[0]) == "Data fequency:"):
    fequency(mstr)
else:
    print(head_dev(mstr[0]), mstr)

print("Count bytes:", data.__len__())
print("Count messages", mstr.__len__())

# print("{0:X}".format(i), end=" ")
