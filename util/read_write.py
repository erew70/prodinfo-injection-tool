from binascii import hexlify
from pathlib import Path
from typing import BinaryIO

from .data.offsets import *

from Crypto.Cipher import AES
from Crypto.IO import PEM
from Crypto.Util import Counter

import os


def check_for_prodinfo(filename):
    """
    Check if a file exists in the current directory.

    :param filename: The name of the file to check.
    :return: True if the file exists, False otherwise.
    """
    return os.path.isfile(filename)

def check_files():
    """
    Check for the existence of prodinfo files
    """
    files_to_check = ['prodinfo.gen.bin', 'prodinfo.donor.bin']
    
    for filename in files_to_check:
        if check_for_prodinfo(filename):
            print(f"{filename} exists.")
        else:
            print(f"prodinfo.gen.bin and prodinfo.donor.bin do not exist!")
            input('Press enter or close the window to exit....')
            exit(1)


def read_bytes_from_file(filename, start, end):
    """
    Read a slice of bytes from a file.

    :param filename: The name of the file to read from.
    :param start: The starting byte offset.
    :param end: The ending byte offset.
    :return: The byte slice read from the file.
    """
    with open(filename, 'rb') as file:
        file.seek(start)
        return file.read(end - start)

def write_bytes_to_file(filename, start, data):
    """
    Write bytes to a specific location in a file.

    :param filename: The name of the file to write to.
    :param start: The starting byte offset.
    :param data: The byte data to write.
    """
    with open(filename, 'r+b') as file:
        file.seek(start)
        file.write(data)


def importSSLCert(prodinfo_gen, prodinfo_donor):




    pt1_start = oct_pt_1
    pt1_end = oct_pt_2
    pt2_start = oct_pt_3
    pt2_end = oct_pt_4
    pt3_start = oct_pt_5
    pt3_end = oct_pt_6
    pt4_start = oct_pt_7
    pt4_end = oct_pt_8
    pt5_start = dct_pt_1
    pt5_end = dct_pt_2

    # Read the byte ranges from prodinfo_donor
    donor_data_pt1 = read_bytes_from_file(prodinfo_donor, pt1_start, pt1_end)
    donor_data_pt2 = read_bytes_from_file(prodinfo_donor, pt2_start, pt2_end)
    donor_data_pt3 = read_bytes_from_file(prodinfo_donor, pt3_start, pt3_end)
    donor_data_pt4 = read_bytes_from_file(prodinfo_donor, pt4_start, pt4_end)
    donor_data_pt5 = read_bytes_from_file(prodinfo_donor, pt5_start, pt5_end)

    # Write the byte ranges to prodinfo_gen
    write_bytes_to_file(prodinfo_gen, pt1_start, donor_data_pt1)
    write_bytes_to_file(prodinfo_gen, pt2_start, donor_data_pt2)
    write_bytes_to_file(prodinfo_gen, pt3_start, donor_data_pt3)
    write_bytes_to_file(prodinfo_gen, pt4_start, donor_data_pt4)
    write_bytes_to_file(prodinfo_gen, pt5_start, donor_data_pt5)



def importSerial(prodinfo_gen, prodinfo_donor):



    pt1_start = s_pt_1
    pt1_end = s_pt_2
    

    # Read the byte ranges from prodinfo_donor
    donor_data_pt1 = read_bytes_from_file(prodinfo_donor, pt1_start, pt1_end)
    

    # Write the byte ranges to prodinfo_gen
    write_bytes_to_file(prodinfo_gen, pt1_start, donor_data_pt1)
    

def importOtherStuff(prodinfo_gen, prodinfo_donor):
 


    pt1_start = os_pt_1
    pt1_end = os_pt_2
    
    # Read the byte ranges from prodinfo_donor
    donor_data_pt1 = read_bytes_from_file(prodinfo_donor, pt1_start, pt1_end)
   
    # Write the byte ranges to prodinfo_gen
    write_bytes_to_file(prodinfo_gen, pt1_start, donor_data_pt1)

def importKeys(prodinfo_gen, prodinfo_donor):


    pt1_start = ks_pt_1
    pt1_end = ks_pt_2
    pt2_start = ks_pt_3
    pt2_end = ks_pt_4

    

    # Read the byte ranges from prodinfo_donor
    donor_data_pt1 = read_bytes_from_file(prodinfo_donor, pt1_start, pt1_end)
    donor_data_pt2 = read_bytes_from_file(prodinfo_donor, pt2_start, pt2_end)
   
    # Write the byte ranges to prodinfo_gen
    write_bytes_to_file(prodinfo_gen, pt1_start, donor_data_pt1)
    write_bytes_to_file(prodinfo_gen, pt2_start, donor_data_pt2)

def importNewDeviceID(prodinfo_gen, prodinfo_donor):



    pt1_start = di_pt_1
    pt1_end = di_pt_2


    

    # Read the byte ranges from prodinfo_donor
    donor_data_pt1 = read_bytes_from_file(prodinfo_donor, pt1_start, pt1_end)
   
    # Write the byte ranges to prodinfo_gen
    write_bytes_to_file(prodinfo_gen, pt1_start, donor_data_pt1)


def getDeviceID(prodinfo_donor):


    pt1_start = di_pt_1
    pt1_end = di_pt_2
    donor_data_pt1 = read_bytes_from_file(prodinfo_donor, pt1_start, pt1_end )
    donor_data_str = donor_data_pt1.decode('utf-8')

    # Find the position of "NX"
    start_index = donor_data_str.find("NX")

    if start_index != -1:
        # Calculate the start position of the data after "NX"
        start_index += len("NX")

        # Extract the data after "NX"
        deviceID = donor_data_str[start_index:]
    else:
        # "NX" not found, return the entire data or handle as needed
        deviceID = donor_data_str

    return deviceID