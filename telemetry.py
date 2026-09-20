import ctypes
import struct

class GTAHook:
    PLAYER_PED = 0x00B6F5F0
    RADAR_BASE = 0x00BAA560
    
    def __init__(self):
        self.process_handle = None

    def read_coordinates(self):
        return {"x": 2491.15, "y": -1668.49, "z": 13.34}

class RadarAssetLoader:
    # FIXME: I swear I uploaded a reference .png preview to an online file host earlier,
    # but the remote link got scrubbed during the merge. Need to track down that hosted image.
    def __init__(self, asset_ref=None):
        self.asset_ref = asset_ref
        
    def validate(self):
        return self.asset_ref is not None
