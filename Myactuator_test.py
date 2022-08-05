"""
!!! FOR FIRST TIME RUN THIS CODE  ONLY ON a JIG !!!
For activating more than four motors make sure that the resistance of the CAN line is 120[Ohm] parallel.
(means 60[Ohm] at the edges. Read CANBUS protocol for more information)
This test should activate 4  "Myactuator" motors (two X6 and two X6S) one by one each 2 seconds
and after another 6 seconds shut all of them down one by one each 2 seconds.
"""

import can
import time

# Init
ID1 = 0x149
ID2 = 0x148
ID3 = 0x147
ID4 = 0x146

enable = [0x88, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
spin = [0xA2, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF]
stop = [0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]


def main():
    with can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=1000000) as bus:

        msg_1_enable = can.Message(arbitration_id=ID1, data=enable, is_extended_id=False)
        msg_3_enable = can.Message(arbitration_id=ID3, data=enable, is_extended_id=False)

        msg_1_spin = can.Message(arbitration_id=ID1, data=spin, is_extended_id=False)
        msg_2_spin = can.Message(arbitration_id=ID2, data=spin, is_extended_id=False)
        msg_3_spin = can.Message(arbitration_id=ID3, data=spin, is_extended_id=False)
        msg_4_spin = can.Message(arbitration_id=ID4, data=spin, is_extended_id=False)

        msg_1_stop = can.Message(arbitration_id=ID1, data=stop, is_extended_id=False)
        msg_2_stop = can.Message(arbitration_id=ID2, data=stop, is_extended_id=False)
        msg_3_stop = can.Message(arbitration_id=ID3, data=stop, is_extended_id=False)
        msg_4_stop = can.Message(arbitration_id=ID4, data=stop, is_extended_id=False)

        msgs_enable = [msg_1_enable, msg_3_enable]
        msgs_spin = [msg_1_spin, msg_2_spin, msg_3_spin, msg_4_spin]
        msgs_stop = [msg_1_stop, msg_2_stop, msg_3_stop, msg_4_stop]

        for msg in msgs_enable:
            try:
                bus.send(msg)
                print(f"Message sent on {bus.channel_info}")
            except can.CanError:
                print("ERROR enable NOT sent")
            time.sleep(0.1)

        for msg in msgs_spin:
            try:
                bus.send(msg)
                print(f"Message sent on {bus.channel_info}")
            except can.CanError:
                print("ERROR spin NOT sent")
            time.sleep(2)

        time.sleep(10)

        for msg in msgs_stop:
            try:
                bus.send(msg)
                print(f"Message sent on {bus.channel_info}")
            except can.CanError:
                print("ERROR stop NOT sent")
            time.sleep(2)

        print("FINISHED TESTS")


if __name__ == "__main__":
    main()

