#import sys
#import random
#import time
#import cryptography
import datetime

from opcua import Server
import socket
product_uri = "OPCUA EnergyTrain"
manufacture_name = "LLC mine S.D.Tihova"
product_name = "shearer-mb450"
version = 0.01
build_number = 10
build_date = datetime.datetime.today()
URL = "opc.tcp://0.0.0.0:4840"

TCP_IP = '192.168.11.91'
TCP_PORT = 1500
BUFFER_SIZE = 4096
j = 0

if __name__ == "__main__":
    server = Server()
    server.set_endpoint(URL)
    server.set_build_info(product_uri, manufacture_name, product_name, version, build_number, build_date)

    ns = server.register_namespace("tic1")
    objects = server.get_objects_node()
    shearer = objects.add_object(ns, "shearer")
    shearer_status = objects.add_object(ns, "shearer_status")
    shearer_time = objects.add_object(ns, "shearer_time")

    shearer_data_status = shearer_status.add_variable(ns, "data_status", 0)
    shearer_software_version = shearer_status.add_variable(ns, "software_version", 0.0)
    shearer_motor_status_m1 = shearer_status.add_variable(ns, "motor_sensor_status_m1", 0)
    shearer_motor_status_m2 = shearer_status.add_variable(ns, "motor_sensor_status_m2", 0)
    shearer_motor_status_m3 = shearer_status.add_variable(ns, "motor_sensor_status_m3", 0)
    shearer_motor_status_m4 = shearer_status.add_variable(ns, "motor_sensor_status_m4", 0)
    shearer_motor_status_m5 = shearer_status.add_variable(ns, "motor_sensor_status_m5", 0)
    shearer_speed_status = shearer_status.add_variable(ns, "speed_sensor_status", 0)
    shearer_position_status = shearer_status.add_variable(ns, "position_status", 0)
    shearer_time_work_status = shearer_status.add_variable(ns, "time_work_status", 0)
    shearer_speed_regulation_status = shearer_status.add_variable(ns, "speed_regulation_status", 0)
    shearer_postion_number_section_status = shearer_status.add_variable(ns, "position_number_section_status", 0)
    shearer_voltage_status = shearer_status.add_variable(ns, "voltage_status", 0)
    shearer_status = shearer_status.add_variable(ns, "status", 0)
    shearer_level_defence_status_m1 = shearer_status.add_variable(ns, "level_defence_status_m1", 0)
    shearer_level_defence_status_m2 = shearer_status.add_variable(ns, "level_defence_status_m2", 0)
    shearer_level_defence_status_m3 = shearer_status.add_variable(ns, "level_defence_status_m3", 0)
    shearer_level_defence_status_m4 = shearer_status.add_variable(ns, "level_defence_status_m4", 0)
    shearer_level_defence_status_m5 = shearer_status.add_variable(ns, "level_defence_status_m5", 0)

    shearer_current_year = shearer_time.add_variable(ns, "year", 0)
    shearer_current_mounth = shearer_time.add_variable(ns, "mounth", 0)
    shearer_current_day = shearer_time.add_variable(ns, "day", 0)
    shearer_current_hour = shearer_time.add_variable(ns, "hour", 0)
    shearer_current_minute = shearer_time.add_variable(ns, "minute", 0)
    shearer_current_sec = shearer_time.add_variable(ns, "second", 0)
    shearer_time_work = shearer_time.add_variable(ns, "time_work", 0)

    shearer_motor_current_m1 = shearer.add_variable(ns, "motor_current_m1", 0)
    shearer_motor_current_m2 = shearer.add_variable(ns, "motor_current_m2", 0)
    shearer_motor_current_m3 = shearer.add_variable(ns, "motor_current_m3", 0)
    shearer_motor_current_m4 = shearer.add_variable(ns, "motor_current_m4", 0)
    shearer_motor_current_m5 = shearer.add_variable(ns, "motor_current_m5", 0)
    shearer_speed = shearer.add_variable(ns, "speed", 0.0)
    shearer_management_rele = shearer.add_variable(ns, "management_rele", 0)
    shearer_management_command_panel = shearer.add_variable(ns, "management_command_panel", 0)
    shearer_electro_hydro_valve = shearer.add_variable(ns, "electro_hydro_valve", 0)
    shearer_management_drobilka = shearer.add_variable(ns, "management_drobilka", 0)
    shearer_sensor_speed = shearer.add_variable(ns, "sensor_speed", 0)
    shearer_sensor_pologenie = shearer.add_variable(ns, "sensor_pologenie", 0)
    shearer_operation_mode = shearer.add_variable(ns, "operation_mode", 0)
    shearer_type = shearer.add_variable(ns, "shearer_type", 0)
    shearer_reason_off = shearer.add_variable(ns, "reason_off", 0)
    shearer_traversed_path = shearer.add_variable(ns, "traversed_path", 0)
    shearer_traversed_path_status = shearer.add_variable(ns, "traversed_path_status", 0)
    shearer_postion = shearer.add_variable(ns, "position", 0)
    shearer_speed_regulation = shearer.add_variable(ns, "speed_regulation", 0.0)
    shearer_postion_number_section = shearer.add_variable(ns, "position_number_section", 0)
    shearer_voltage = shearer.add_variable(ns, "voltage", 0)
    shearer_error = shearer.add_variable(ns, "error", 0)
    shearer_level_defence_m1 = shearer.add_variable(ns, "level_defence_m1", 0)
    shearer_level_defence_m2 = shearer.add_variable(ns, "level_defence_m2", 0)
    shearer_level_defence_m3 = shearer.add_variable(ns, "level_defence_m3", 0)
    shearer_level_defence_m4 = shearer.add_variable(ns, "level_defence_m4", 0)
    shearer_level_defence_m5 = shearer.add_variable(ns, "level_defence_m5", 0)
    shearer_serial_number = shearer.add_variable(ns, "serial_number", 0)

    server.start()

    class Shearer:
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
        voltage = ""  # Reg[57,58], uint, 0 - 1500
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
            self.data_status =  data[17]
            self.software_version = float(str(data[19]) + "." + str(data[20]))
            self.motor_current_m1 = data[22]
            self.motor_status_m1 = data[23]
            self.motor_current_m2 = data[30]
            self.motor_status_m2 = data[31]
            self.motor_current_m3 = data[33]
            self.motor_status_m3 = data[34]
            self.motor_current_m4 = data[41]
            self.motor_status_m4 = data[42]
            self.motor_current_m5 = data[44]
            self.motor_status_m5 = data[45]
            self.speed = data[47]/10  # 0-250, 0.1m/min
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
            self.operation_mode = data[71]
            self.reason_off = data[78]
            self.traversed_path = str(data[80]) + str(data[81]) + str(data[82]) + str(data[83])
            self.traversed_path_status = data[89]
            self.position = str(data[90]) + str(data[91]) + str(data[92]) + str(data[93])
            self.position_status = data[94]
            self.time_work = str(data[95]) + str(data[101]) + str(data[102]) + str(data[103])
            self.time_work_status = data[104]
            self.speed_regulation = data[105]
            self.speed_regulation_status = data[106]
            self.position_number_section = data[107]
            self.position_number_section_status = data[113]
            self.voltage = str(data[114]) + str(data[115])
            print(hex(data[114]) + hex(data[115]))
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

    sh = Shearer()

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        data = s.recv(BUFFER_SIZE)
        s.close()

        if data[9] == 16 and data[10] == 16:
            sh.shearer_data(data)
            shearer_data_status.set_value(sh.data_status)
            shearer_voltage.set_value(sh.voltage)
            shearer_software_version.set_value(sh.software_version)
            shearer_motor_current_m1.set_value(sh.motor_current_m1)
            shearer_motor_status_m1.set_value(sh.motor_status_m1)
            shearer_motor_current_m2.set_value(sh.motor_current_m2)
            shearer_motor_status_m2.set_value(sh.motor_current_m2)
            shearer_motor_current_m3.set_value(sh.motor_current_m3)
            shearer_motor_status_m3.set_value(sh.motor_current_m3)
            shearer_motor_current_m4.set_value(sh.motor_current_m4)
            shearer_motor_status_m4.set_value(sh.motor_current_m4)
            shearer_motor_current_m5.set_value(sh.motor_current_m5)
            shearer_motor_status_m5.set_value(sh.motor_current_m5)
            shearer_speed.set_value(sh.speed)
            shearer_speed_status.set_value(sh.speed_status)
            shearer_current_year.set_value(sh.current_year)
            shearer_current_mounth.set_value(sh.current_mounth)
            shearer_current_day.set_value(sh.current_day)
            shearer_current_hour.set_value(sh.current_hour)
            shearer_current_minute.set_value(sh.current_minute)
            shearer_current_sec.set_value(sh.current_sec)
            shearer_management_rele.set_value(sh.management_rele)
            shearer_management_command_panel.set_value(sh.management_command_panel)
            shearer_electro_hydro_valve.set_value(sh.electro_hydro_valve)
            shearer_management_drobilka.set_value(sh.management_drobilka)
            shearer_sensor_speed.set_value(sh.sensor_speed)
            shearer_sensor_pologenie.set_value(sh.sensor_pologenie)
            shearer_operation_mode.set_value(sh.operation_mode)
            shearer_type.set_value(sh.shearer_type)
            shearer_reason_off.set_value(sh.reason_off)
            shearer_traversed_path.set_value(sh.traversed_path)
            shearer_traversed_path_status.set_value(sh.traversed_path_status)
            shearer_postion.set_value(sh.position)
            shearer_position_status.set_value(sh.position_status)
            shearer_time_work.set_value(sh.time_work)
            shearer_time_work_status.set_value(sh.time_work_status)
            shearer_speed_regulation.set_value(sh.speed_regulation)
            shearer_speed_regulation_status.set_value(sh.speed_regulation_status)
            shearer_postion_number_section.set_value(sh.position_number_section)
            shearer_postion_number_section_status.set_value(sh.position_number_section_status)
            shearer_voltage.set_value(sh.voltage)
            shearer_voltage_status.set_value(sh.voltage_status)
            shearer_error.set_value(sh.error)
            shearer_status.set_value(sh.status)
            shearer_level_defence_m1.set_value(sh.level_defence_m1)
            shearer_level_defence_status_m1.set_value(sh.level_defence_status_m1)
            shearer_level_defence_m2.set_value(sh.level_defence_m2)
            shearer_level_defence_status_m2.set_value(sh.level_defence_status_m2)
            shearer_level_defence_m3.set_value(sh.level_defence_m3)
            shearer_level_defence_status_m3.set_value(sh.level_defence_status_m3)
            shearer_level_defence_m4.set_value(sh.level_defence_m4)
            shearer_level_defence_status_m4.set_value(sh.level_defence_status_m4)
            shearer_level_defence_m5.set_value(sh.level_defence_m5)
            shearer_level_defence_status_m5.set_value(sh.level_defence_status_m5)
            shearer_serial_number.set_value(sh.serial_number)
    server.stop()