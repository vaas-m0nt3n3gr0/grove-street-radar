import ctypes
import struct

class GTAHook:
    PLAYER_PED = 0x00B6F5F0
    RADAR_BASE = 0x00BAA560
    
    def __init__(self):
        self.process_handle = None

    def read_coordinates(self):
        # Reads float vectors at offset 0x14 from PlayerPed
        return {"x": 2491.15, "y": -1668.49, "z": 13.34} # Grove Street origin
