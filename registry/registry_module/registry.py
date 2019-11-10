import os
from winreg import *


def _pad_dict(usb_storage_dict):

    length_of_val_array = []
    for k,v in usb_storage_dict.items():
        length_of_val_array.append(len(v))

    max_length = max(length_of_val_array)

    for k,v in usb_storage_dict.items():
        l = len(v)
        pad_length = max_length-l
        pad_val = v + ['-']*pad_length

        usb_storage_dict[k] = pad_val

    return usb_storage_dict


def usb_storage(sub_key_path):
    aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    aKey = OpenKey(aReg, sub_key_path)
    usb_data_dict = {}
    required_features = ['USB_Devices', 'CompatibleIDs', 'FriendlyName', 'HardwareID']
    for feature in required_features:
        usb_data_dict[feature] = []

    for i in range(QueryInfoKey(aKey)[0]):
        try:
            asubkey_name=EnumKey(aKey,i)

            asubkey=OpenKey(aKey,asubkey_name)
            for j in range(QueryInfoKey(asubkey)[0]):
                usb_data_dict['USB_Devices'].append(asubkey_name)
                sub_sub_key_path = EnumKey(asubkey, j)
                sub_sub_key = OpenKey(asubkey, sub_sub_key_path)

                for feature in required_features[1:]:
                # QueryValueEx returns a tuple with value at first index
                    try:
                        temp_val = QueryValueEx(sub_sub_key, feature)[0]
                        usb_data_dict[feature].append(temp_val)
                    except FileNotFoundError as e:
                        temp_val = "NA"
                        usb_data_dict[feature].append(temp_val)
        except EnvironmentError as e:
            break
    usb_data_dict = _pad_dict(usb_data_dict)
    return usb_data_dict

def ip_registry(sub_key_path):
    """This functions extracts data related to IP address

    from the registry. Parameters:
    :sub_key_path - path(string) to the sub key

    Returns: json object"""

    # First argument of ConnectRegistry function is Computer Name and None implies local computer
    aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    aKey = OpenKey(aReg,sub_key_path)
    ip_data_dict = {}
    required_features = ['Interfaces','DhcpIPAddress','DhcpServer','DhcpSubnetMask','DhcpSubnetMaskOpt']
    # Initialize ip_data_dict with required features as Key and empty List as their value
    # so that lists can be appended with values while iterating over the subkeys.
    for feature in required_features:
        ip_data_dict[feature] = []

    for i in range(QueryInfoKey(aKey)[0]):
        try:
            # EnumKey enumerates the subkeys thus helping us to iterate over them. Here
            # the sub key corresponds to interface values
            asubkey_name=EnumKey(aKey,i)
            # appending subkey_name to interface values
            ip_data_dict['Interfaces'].append(asubkey_name)
            asubkey=OpenKey(aKey,asubkey_name)
            # appending values to ip_data_dict keys except 'Interfaces'
            for feature in required_features[1:]:
                # QueryValueEx returns a tuple with value at first index
                try:
                    temp_val = QueryValueEx(asubkey, feature)[0]
                except FileNotFoundError as e:
                    temp_val = "NA"
                ip_data_dict[feature].append(temp_val)
        except EnvironmentError as e:
            break

    return ip_data_dict

def _data_extraction(recent_doc_data_dict):
    """This function performs data cleaning and extraction of data obtained

    from recent docs registry"""

    for k,v in recent_doc_data_dict.items():
        # v is an array of file names with extenstion k in binary from with text values
        # embedded in between. We will extract the same.
        new_val = []
        for val in v:
            # sample value of val - .....\\x00\\x00\\x00\\x00\\x001801089_HoChengKaiNoah_1.cpp.lnk\\x00\\x00r\\x00\\t\\x00....
            bin_list = val.split("\\x00")
            for elem_val in bin_list:
                # Special case for folder since Folders don't have extension
                if k=='Folder':
                    if '.lnk' in elem_val:
                        new_val.append(elem_val)
                else:
                    if k in elem_val:
                        # appending extracted text file name to the new_val array
                        new_val.append(elem_val)
        # replacing the old binary string array values with new_val array
        recent_doc_data_dict[k] = new_val

    # Padding values - Arrays are of unequal length.We will pad them with '-'
    # this will help in converting them into tabular form
    length_of_val_array = []
    for k,v in recent_doc_data_dict.items():
        length_of_val_array.append(len(v))

    try:
        max_length = max(length_of_val_array)

    except:
        print("Recent docs registry is empty.")

    finally:
        for k,v in recent_doc_data_dict.items():
            l = len(v)
            pad_length = max_length-l
            pad_val = v + ['-']*pad_length

            recent_doc_data_dict[k] = pad_val
        return recent_doc_data_dict


def recent_docs_registry(sub_key_path):
    """This functions extracts data related to recent docs

    from the registry. Parameters:
    :sub_key_path - path(string) to the sub key

    Returns: json object"""
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg,sub_key_path)
    recent_doc_data_dict = {}
    for i in range(QueryInfoKey(aKey)[0]):
        try:
            asubkey_name=EnumKey(aKey,i)
            asubkey=OpenKey(aKey,asubkey_name)
            for j in range(QueryInfoKey(asubkey)[1]):
                # EnumValue enumerates the values of the subkey passed as argument
                temp_val = EnumValue(asubkey,j)
                # We cannot extract any info from MRUListEx data values as they are just binaries
                if temp_val[0] != 'MRUListEx':
                    try:
                        recent_doc_data_dict[asubkey_name].append(str(temp_val[1]))
                    except KeyError:
                        recent_doc_data_dict[asubkey_name] = []
                        recent_doc_data_dict[asubkey_name].append(str(temp_val[1]))
        except FileNotFoundError as e:
            pass
        except EnvironmentError as e:
            print("in")
            break
    recent_doc_data_dict = _data_extraction(recent_doc_data_dict)
    return recent_doc_data_dict

def wireless_evidence_registry(sub_key_path):
    """This functions extracts data related to wireless evidence

    from the registry. Parameters:
    :sub_key_path - path(string) to the sub key

    Returns: json object"""

    aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    aKey = OpenKey(aReg,sub_key_path,access=KEY_READ | KEY_WOW64_64KEY)
    wireless_data_dict = {}
    required_features = ['Profiles','ProfileName','Description']
    for feature in required_features:
        wireless_data_dict[feature] = []
    for i in range(QueryInfoKey(aKey)[0]):
        try:
            asubkey_name=EnumKey(aKey,i)
            wireless_data_dict['Profiles'].append(asubkey_name)
            asubkey=OpenKey(aKey,asubkey_name)
            for feature in required_features[1:]:
                # QueryValueEx returns a tuple with value at first index
                try:
                    temp_val = QueryValueEx(asubkey, feature)[0]
                except FileNotFoundError as e:
                    temp_val = "NA"
                wireless_data_dict[feature].append(temp_val)
        except EnvironmentError as e:
            break
    return wireless_data_dict

def start_up_registry(sub_key_path):
    """This functions extracts data related to startup programs,

    both 'Run' and 'RunOnce' type of programs, from the registry.
    Parameters:
    :sub_key_path - path(string) to the sub key

    Returns: json object"""
    aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    aKey = OpenKey(aReg,sub_key_path,access=KEY_READ | KEY_WOW64_64KEY)
    start_up_dict = {}
    programs = []
    path = []
    for i in range(QueryInfoKey(aKey)[1]):
        try:
            values = EnumValue(aKey,i)
            programs.append(values[0])
            path.append(values[1])
        except FileNotFoundError as e:
            pass
        except EnvironmentError as e:
            break
    start_up_dict['Programs'] = programs
    start_up_dict['Path'] = path
    return start_up_dict

def start_up_particular_user_registry(sub_key_path):
    """This functions extracts data related to startup

    programs for a particular use from the registry.
    Parameters:
    :sub_key_path - path(string) to the sub key

    Returns: json object"""
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg,sub_key_path,access=KEY_READ | KEY_WOW64_64KEY)
    start_up_particular_user = {}
    programs = []
    path = []
    for i in range(QueryInfoKey(aKey)[1]):
        try:
            values = EnumValue(aKey,i)
            programs.append(values[0])
            path.append(values[1])
        except FileNotFoundError as e:
            pass
        except EnvironmentError as e:
            break
    start_up_particular_user['Programs'] = programs
    start_up_particular_user['Path'] = path
    return start_up_particular_user


if __name__ == '__main__':
    pass
