# import sys
# import random
# import time
# import cryptography
import datetime
import threading
import time

from opcua import Server
import socket
import datastruct.tmachinery
import asyncio

product_uri = "OPCUA EnergyTrain"
manufacture_name = "LLC mine S.D.Tihova"
product_name = "tihova-lava"
version = 0.02
build_number = 10
build_date = datetime.datetime.today()
URL = "opc.tcp://0.0.0.0:4840"

ipsrv = '192.168.11.91'
tcpport = 1500
TCP_IP = '192.168.11.91'
TCP_PORT = 1500
TCP_RECONNECT_TIMEOUT = 3      # 3 second
BUFFER_SIZE = 4096
status_drv_connection = False
status_srv_run = False
j = 0
fstr = []

#async def tcp_echo_client(ipsrv, tcpport, loop):
    #reader, writer = await asyncio.open_connection(ipsrv, tcpport, loop=loop)
    #data = await reader.read(255)
    #print(sh.__dict__)
    #print(freq.__dict__)
    #print('Close the socket')
    #writer.close()

def get_data(status_drv_connection):
        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(tcp_echo_client(ipsrv, tcpport, loop))
        while status_drv_connection == False:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((TCP_IP, TCP_PORT))
                s.settimeout(TCP_RECONNECT_TIMEOUT)
                data = s.recv(BUFFER_SIZE)
                status_drv_connection = True
                print("Connect to", TCP_IP, ":", TCP_PORT, " succesfull.")
                while len(data) > 0:
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
                            shearer_position.set_value(sh.position)
                            shearer_position_status.set_value(sh.position_status)
                            shearer_time_work.set_value(sh.time_work)
                            shearer_time_work_status.set_value(sh.time_work_status)
                            shearer_speed_regulation.set_value(sh.speed_regulation)
                            shearer_speed_regulation_status.set_value(sh.speed_regulation_status)
                            shearer_position_number_section.set_value(sh.position_number_section)
                            shearer_position_number_section_status.set_value(sh.position_number_section_status)
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
                    if data[9] == 18 and data[10] == 16:
                            freq.mfk400(data)
                            frequency_data_status.set_value(freq.data_status)
                            frequency_software_version.set_value(freq.software_version)
                            frequency_output_frequency.set_value(freq.output_frequency)
                            frequency_output_amperage.set_value(freq.output_amperage)
                            frequency_output_voltage.set_value(freq.output_voltage)
                            frequency_voltage_capacitor.set_value(freq.voltage_capacitor)
                            frequency_sensor_status.set_value(freq.sensor_status)
                            frequency_voltage_input.set_value(freq.voltage_input)
                            frequency_sensor_voltage_input_status.set_value(freq.sensor_voltage_input_status)
                            frequency_temperature_air_shearer.set_value(freq.temperature_air_shearer)
                            frequency_temperature_air_shearer_status.set_value(freq.temperature_air_shearer_status)
                            frequency_temperature_modem_shearer.set_value(freq.temperature_modem_shearer)
                            frequency_temperature_modem_shearer_status.set_value(freq.temperature_modem_shearer_status)
                            frequency_output_amperage_contactor.set_value(freq.output_amperage_contactor)
                            frequency_output_amperage_contactor_status.set_value(freq.output_amperage_contactor_status)
                            frequency_temperature_air_frequency.set_value(freq.temperature_air_frequency)
                            frequency_temperature_air_icebox_igbt.set_value(freq.temperature_air_icebox_igbt)
                            # frequency_temperature_usmemovace = 0  # Reg[25]  UNUSED
                            # frequency_temperature_brzdy_mf = 0  # Reg[26]  UNUSED
                            frequency_temperature_mf_status.set_value(freq.temperature_mf_status)
                            frequency_number_mfk.set_value(freq.number_mfk)
                            frequency_error.set_value(freq.error)
                            frequency_errorFreelop.set_value(freq.errorFreelop)
                            # frequency_errorFdrive.set_value(freq.errorFdrive)
                            frequency_status.set_value(freq.status)
                            frequency_mfk_concentration_ch4.set_value(freq.mfk_concentration_ch4)
                            frequency_mfk_concentration_ch4_status.set_value(freq.mfk_concentration_ch4_status)
                            # frequency_mfk_material_case.set_value(freq.mfk_material_case)
                            frequency_language.set_value(freq.language)
                            frequency_mfk_year.set_value(freq.mfk_year)
                            frequency_mfk_mounth.set_value(freq.mfk_mounth)
                            frequency_mfk_day.set_value(freq.mfk_day)
                            frequency_mfk_hour.set_value(freq.mfk_hour)
                            frequency_mfk_minute.set_value(freq.mfk_minute)
                            frequency_mfk_second.set_value(freq.mfk_second)
                            frequency_shearer_year.set_value(freq.shearer_year)
                            frequency_shearer_mounth.set_value(freq.shearer_mounth)
                            frequency_shearer_day.set_value(freq.shearer_day)
                            frequency_shearer_hour.set_value(freq.shearer_hour)
                            frequency_shearer_minute.set_value(freq.shearer_minute)
                            frequency_shearer_second.set_value(freq.shearer_second)
                            frequency_mfk_number_section.set_value(freq.mfk_number_section)
                            frequency_mfk_number_section_status.set_value(freq.mfk_number_section_status)
                        # print(sh.__dict__)
                        # print(freq.__dict__)
                    data = s.recv(BUFFER_SIZE)
            except:
                print(TCP_IP, ":", TCP_PORT, " connection not succesfull!")
                status_drv_connection = False
                pass
            finally:
                print("Connection lose!")
                s.close()

if __name__ == "__main__":
    """Add tags in opcua and start server"""
    server = Server()
    server.set_endpoint(URL)
    server.set_build_info(product_uri, manufacture_name, product_name, version, build_number, build_date)

    list_tags = []
    sh = datastruct.tmachinery.Shearer()
    freq = datastruct.tmachinery.Frequency()
    cfg_shearer = sh.get_tags(sh.__dir__())
    cfg_frequency = freq.get_tags(sh.__dir__())


    ns_sh = server.register_namespace("shearer")
    ns_fr = server.register_namespace("frequency")
    objects = server.get_objects_node()
    shearer = objects.add_object(ns_sh, "mb450")
    frequency = objects.add_object(ns_fr, "mfk400")

    def gen_cfg(ns_name, ns_link, obj_link, tags_from_class):
        for i in range(0, len(tags_from_class)):
            s = ns_name + "_" + tags_from_class[i]
            list_tags[i].append(s)
            list_tags[i] = obj_link.add_variable(ns_link, ns_name, 0)
        return list_tags

    print(cfg_shearer)
    #print(gen_cfg("test_sh", ns_sh, shearer, cfg_shearer))
    shearer_data_status = shearer.add_variable(ns_sh, "data_status", 0)
    shearer_software_version = shearer.add_variable(ns_sh, "software_version", 0.0)
    shearer_motor_status_m1 = shearer.add_variable(ns_sh, "motor_sensor_status_m1", 0)
    shearer_motor_status_m2 = shearer.add_variable(ns_sh, "motor_sensor_status_m2", 0)
    shearer_motor_status_m3 = shearer.add_variable(ns_sh, "motor_sensor_status_m3", 0)
    shearer_motor_status_m4 = shearer.add_variable(ns_sh, "motor_sensor_status_m4", 0)
    shearer_motor_status_m5 = shearer.add_variable(ns_sh, "motor_sensor_status_m5", 0)
    shearer_speed_status = shearer.add_variable(ns_sh, "speed_sensor_status", 0)
    shearer_position_status = shearer.add_variable(ns_sh, "position_status", 0)
    shearer_time_work_status = shearer.add_variable(ns_sh, "time_work_status", 0)
    shearer_speed_regulation_status = shearer.add_variable(ns_sh, "speed_regulation_status", 0)
    shearer_position_number_section_status = shearer.add_variable(ns_sh, "position_number_section_status", 0)
    shearer_traversed_path_status = shearer.add_variable(ns_sh, "traversed_path_status", 0)
    shearer_voltage_status = shearer.add_variable(ns_sh, "voltage_status", 0)
    shearer_status = shearer.add_variable(ns_sh, "status", 0)
    shearer_level_defence_status_m1 = shearer.add_variable(ns_sh, "level_defence_status_m1", 0)
    shearer_level_defence_status_m2 = shearer.add_variable(ns_sh, "level_defence_status_m2", 0)
    shearer_level_defence_status_m3 = shearer.add_variable(ns_sh, "level_defence_status_m3", 0)
    shearer_level_defence_status_m4 = shearer.add_variable(ns_sh, "level_defence_status_m4", 0)
    shearer_level_defence_status_m5 = shearer.add_variable(ns_sh, "level_defence_status_m5", 0)

    shearer_current_year = shearer.add_variable(ns_sh, "year", 0)
    shearer_current_mounth = shearer.add_variable(ns_sh, "mounth", 0)
    shearer_current_day = shearer.add_variable(ns_sh, "day", 0)
    shearer_current_hour = shearer.add_variable(ns_sh, "hour", 0)
    shearer_current_minute = shearer.add_variable(ns_sh, "minute", 0)
    shearer_current_sec = shearer.add_variable(ns_sh, "second", 0)
    shearer_time_work = shearer.add_variable(ns_sh, "time_work", 0)

    shearer_motor_current_m1 = shearer.add_variable(ns_sh, "motor_current_m1", 0)
    shearer_motor_current_m2 = shearer.add_variable(ns_sh, "motor_current_m2", 0)
    shearer_motor_current_m3 = shearer.add_variable(ns_sh, "motor_current_m3", 0)
    shearer_motor_current_m4 = shearer.add_variable(ns_sh, "motor_current_m4", 0)
    shearer_motor_current_m5 = shearer.add_variable(ns_sh, "motor_current_m5", 0)
    shearer_speed = shearer.add_variable(ns_sh, "speed", 0.0)
    shearer_management_rele = shearer.add_variable(ns_sh, "management_rele", 0)
    shearer_management_command_panel = shearer.add_variable(ns_sh, "management_command_panel", 0)
    shearer_electro_hydro_valve = shearer.add_variable(ns_sh, "electro_hydro_valve", 0)
    shearer_management_drobilka = shearer.add_variable(ns_sh, "management_drobilka", 0)
    shearer_sensor_speed = shearer.add_variable(ns_sh, "sensor_speed", 0)
    shearer_sensor_pologenie = shearer.add_variable(ns_sh, "sensor_pologenie", 0)
    shearer_operation_mode = shearer.add_variable(ns_sh, "operation_mode", 0)
    shearer_type = shearer.add_variable(ns_sh, "shearer_type", 0)
    shearer_reason_off = shearer.add_variable(ns_sh, "reason_off", 0)
    shearer_traversed_path = shearer.add_variable(ns_sh, "traversed_path", 0)
    shearer_position = shearer.add_variable(ns_sh, "position", 0)
    shearer_speed_regulation = shearer.add_variable(ns_sh, "speed_regulation", 0.0)
    shearer_position_number_section = shearer.add_variable(ns_sh, "position_number_section", 0)
    shearer_voltage = shearer.add_variable(ns_sh, "voltage", 0)
    shearer_error = shearer.add_variable(ns_sh, "error", 0)
    shearer_level_defence_m1 = shearer.add_variable(ns_sh, "level_defence_m1", 0)
    shearer_level_defence_m2 = shearer.add_variable(ns_sh, "level_defence_m2", 0)
    shearer_level_defence_m3 = shearer.add_variable(ns_sh, "level_defence_m3", 0)
    shearer_level_defence_m4 = shearer.add_variable(ns_sh, "level_defence_m4", 0)
    shearer_level_defence_m5 = shearer.add_variable(ns_sh, "level_defence_m5", 0)
    shearer_serial_number = shearer.add_variable(ns_sh, "serial_number", 0)

    frequency_data_status = frequency.add_variable(ns_fr, "data_status", 0)
    frequency_software_version = frequency.add_variable(ns_fr, "software_version", 0)
    frequency_output_frequency = frequency.add_variable(ns_fr, "output_frequency", 0)
    frequency_output_amperage = frequency.add_variable(ns_fr, "output_amperage", 0)
    frequency_output_voltage = frequency.add_variable(ns_fr, "output_voltage", 0)
    frequency_voltage_capacitor = frequency.add_variable(ns_fr, "voltage_capacitor", 0)
    frequency_sensor_status = frequency.add_variable(ns_fr, "sensor_status", 0)
    frequency_voltage_input = frequency.add_variable(ns_fr, "voltage_input", 0)
    frequency_sensor_voltage_input_status = frequency.add_variable(ns_fr, "voltage_input_status", 0)
    frequency_temperature_air_shearer = frequency.add_variable(ns_fr, "temperature_air_shearer", 0)
    frequency_temperature_air_shearer_status = frequency.add_variable(ns_fr, "temperature_air_shearer_status", 0)
    frequency_temperature_modem_shearer = frequency.add_variable(ns_fr, "temperature_modem_shearer", 0)
    frequency_temperature_modem_shearer_status = frequency.add_variable(ns_fr, "temperature_modem_shearer_status", 0)
    frequency_output_amperage_contactor = frequency.add_variable(ns_fr, "output_amperage_contactor", 0)
    frequency_output_amperage_contactor_status = frequency.add_variable(ns_fr, "output_amperage_contactor_status", 0)
    frequency_temperature_air_frequency = frequency.add_variable(ns_fr, "temperature_air_frequency", 0)
    frequency_temperature_air_icebox_igbt = frequency.add_variable(ns_fr, "temperature_air_icebox_igbt", 0)
    frequency_temperature_usmemovace = 0  # Reg[25]  UNUSED
    frequency_temperature_brzdy_mf = 0  # Reg[26]  UNUSED
    frequency_temperature_mf_status = frequency.add_variable(ns_fr, "temperature_mf_status", 0)
    frequency_number_mfk = frequency.add_variable(ns_fr, "number_mfk", 0)
    frequency_error = frequency.add_variable(ns_fr, "error", 0)
    frequency_errorFreelop = frequency.add_variable(ns_fr, "errorFreelop", 0)
    frequency_errorFdrive = ""  # Reg[44-47] UNUSED
    frequency_status = frequency.add_variable(ns_fr, "status", 0)
    frequency_mfk_concentration_ch4 = frequency.add_variable(ns_fr, "mfk_concetration_ch4", 0)
    frequency_mfk_concentration_ch4_status = frequency.add_variable(ns_fr, "mfk_concentration_ch4_status", 0)
    frequency_mfk_material_case = 0  # Reg[58], uchar, UNUSED
    frequency_language = frequency.add_variable(ns_fr, "language", 0)
    frequency_mfk_year = frequency.add_variable(ns_fr, "mfk_year", 0)
    frequency_mfk_mounth = frequency.add_variable(ns_fr, "mfk_mounth", 0)
    frequency_mfk_day = frequency.add_variable(ns_fr, "mfk_day", 0)
    frequency_mfk_hour = frequency.add_variable(ns_fr, "mfk_hour", 0)
    frequency_mfk_minute = frequency.add_variable(ns_fr, "mfk_minute", 0)
    frequency_mfk_second = frequency.add_variable(ns_fr, "mfk_second", 0)
    frequency_shearer_year = frequency.add_variable(ns_fr, "shearer_year", 0)
    frequency_shearer_mounth = frequency.add_variable(ns_fr, "shearer_mounth", 0)
    frequency_shearer_day = frequency.add_variable(ns_fr, "shearer_day", 0)
    frequency_shearer_hour = frequency.add_variable(ns_fr, "shearer_hour", 0)
    frequency_shearer_minute = frequency.add_variable(ns_fr, "shearer_minute", 0)
    frequency_shearer_second = frequency.add_variable(ns_fr, "shearer_second", 0)
    frequency_mfk_number_section = frequency.add_variable(ns_fr, "mfk_number_section", 0)
    frequency_mfk_number_section_status = frequency.add_variable(ns_fr, "mfk_number_section_status", 0)

    try:
        server.start()
        print("Server start at ", datetime.datetime.now())
        status_srv_run = True

        #print(freq.__dict__)
        srv = threading.Thread(target=get_data(status_drv_connection))
        srv.daemon = True
        srv.start()
        #if status_srv_run == True:


    except:
        print("Except server failed ", datetime.datetime.now)
        status_srv_run = False
    finally:
        print("Server stop in ", datetime.datetime.now)
        server.stop()
