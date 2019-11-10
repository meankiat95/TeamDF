from registry.registry_module.registry import ip_registry, usb_storage, recent_docs_registry, wireless_evidence_registry, \
    start_up_registry, start_up_particular_user_registry
from registry.registry_module.tabulate_data import *
import json


def regmain():

    with open(r'D:\Downloads\teamDF3\registry\registry_module\config.json') as f:
        config = json.load(f)

    # accessing subkey paths from
    sub_key_path_usb = config['sub_key_path_usb']
    sub_key_path_ip = config['sub_key_path_ip']
    sub_key_path_recent = config['sub_key_path_recent']
    sub_key_path_wireless = config['sub_key_path_wireless']
    sub_key_path_startup_run = config['sub_key_path_startup_run']
    sub_key_path_startup_run_once = config['sub_key_path_startup_run_once']
    sub_key_path_particular_user = config['sub_key_path_particular_user']

    # json_obj data obtained by calling functions from registry module
    json_object_list = [usb_storage(sub_key_path_usb), ip_registry(sub_key_path_ip),recent_docs_registry(sub_key_path_recent),
                        wireless_evidence_registry(sub_key_path_wireless),start_up_registry(sub_key_path_startup_run),
                        start_up_registry(sub_key_path_startup_run_once),
                        start_up_particular_user_registry(sub_key_path_particular_user)]
    # sheet_names length should not exceed 30 or it will throw an error
    sheet_names = ['usb_devices_data','ip_registry','recent_docs_registry','wireless_evidence_registry',
                    'start_up_registry','start_up_registry_run_once','start_up_particular_user']

    data_file_path = config['data_file_path']

    tabulate(json_object_list,sheet_names,data_file_path)

# if __name__ == '__main__':
#     regmain()
