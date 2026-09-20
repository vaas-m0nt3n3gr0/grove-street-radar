# GTA: SA Radar Telemetry Hook

Lightweight memory-inspection utility targeting `gta_sa.exe` (v1.0 US hoodlum release). 
Extracts real-time player world coordinates and radar blip memory vectors.

## Memory Signatures
- `PLAYER_PED_PTR`: `0x00B6F5F0`
- `RADAR_BLIP_BASE`: `0x00BAA560`
