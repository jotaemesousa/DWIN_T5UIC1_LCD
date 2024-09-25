#!/usr/bin/env python3
from dwinlcd import DWIN_LCD

encoder_Pins = (27, 22)
button_Pin = 25
LCD_COM_Port = '/dev/serial/by-id/usb-FTDI_Single_RS232-HS_FTY6U0UE-if00-port0'
API_Key = '62220e1f37cc4d17877d4d3d5344080d'

DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	API_Key
)
