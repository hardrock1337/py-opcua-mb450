# import sys
# import random
# import time
# import cryptography
import datetime

from opcua import Server
import socket
import datastruct.mb430

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
    """Add tags in opcua and start server"""
    server = Server()
    server.set_endpoint(URL)
    server.set_build_info(product_uri, manufacture_name, product_name, version, build_number, build_date)

    ns = server.register_namespace("tic1")
    objects = server.get_objects_node()
    shearer = objects.add_object(ns, "shearer")
    shearer_stat = objects.add_object(ns, "shearer_status")
    shearer_time = objects.add_object(ns, "shearer_time")

    shearer_data_status = shearer_stat.add_variable(ns, "data_status", 0)
    shearer_software_version = shearer_stat.add_variable(ns, "software_version", 0.0)
    shearer_motor_status_m1 = shearer_stat.add_variable(ns, "motor_sensor_status_m1", 0)
    shearer_motor_status_m2 = shearer_stat.add_variable(ns, "motor_sensor_status_m2", 0)
    shearer_motor_status_m3 = shearer_stat.add_variable(ns, "motor_sensor_status_m3", 0)
    shearer_motor_status_m4 = shearer_stat.add_variable(ns, "motor_sensor_status_m4", 0)
    shearer_motor_status_m5 = shearer_stat.add_variable(ns, "motor_sensor_status_m5", 0)
    shearer_speed_status = shearer_stat.add_variable(ns, "speed_sensor_status", 0)
    shearer_position_status = shearer_stat.add_variable(ns, "position_status", 0)
    shearer_time_work_status = shearer_stat.add_variable(ns, "time_work_status", 0)
    shearer_speed_regulation_status = shearer_stat.add_variable(ns, "speed_regulation_status", 0)
    shearer_postion_number_section_status = shearer_stat.add_variable(ns, "position_number_section_status", 0)
    shearer_traversed_path_status = shearer_stat.add_variable(ns, "traversed_path_status", 0)
    shearer_voltage_status = shearer_stat.add_variable(ns, "voltage_status", 0)
    shearer_status = shearer_stat.add_variable(ns, "status", 0)
    shearer_level_defence_status_m1 = shearer_stat.add_variable(ns, "level_defence_status_m1", 0)
    shearer_level_defence_status_m2 = shearer_stat.add_variable(ns, "level_defence_status_m2", 0)
    shearer_level_defence_status_m3 = shearer_stat.add_variable(ns, "level_defence_status_m3", 0)
    shearer_level_defence_status_m4 = shearer_stat.add_variable(ns, "level_defence_status_m4", 0)
    shearer_level_defence_status_m5 = shearer_stat.add_variable(ns, "level_defence_status_m5", 0)

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

    sh = datastruct.mb430.Shearer()

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
