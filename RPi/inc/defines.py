# Generic "Defines"
FAIL							= -1
SUCCESS 						= 0

# Control Frame "Defines"
# Low Frame
PACKET_TYPE_BEACON 				= 0b00000000 # 0
PACKET_TYPE_DATA   				= 0b00000001 # BIT0
PACKET_TYPE_ACK         		= 0b00000010 # BIT1
PACKET_TYPE_COMMAND   			= 0b00000011 # BIT0 | BIT1
PACKET_TYPE			    		= 0b00000111 # BIT0 | BIT1 | BIT2
SECURITY_ENABLED				= 0b00001000 # BIT3
SECURITY_DISABLED				= 0b00000000 # 0
SECURITY_FIELD					= 0b00001000 # BIT3
ACK_REQUIRED_ENABLED			= 0b00100000 # BIT5
ACK_REQUIRED_DISABLED			= 0b00000000 # 0
ACK_REQUIRED_FIELD 				= 0b00100000 # BIT5
PAN_ID_COMP_ENABLED				= 0b01000000 # BIT6
PAN_ID_COMP_DISABLED			= 0b00000000 # 0
PAN_ID_COMP_FIELD				= 0b01000000 # BIT6	

# High Frame
SEQUENCE_NUM_SUP_ENABLED		= 0b00000001 # BIT0 
SEQUENCE_NUM_SUP_DISABLED		= 0b00000000 # 0
SEQUENCE_NUM_SUP_FIELD			= 0b00000001 # BIT0
DST_NO_ADDR						= 0b00000000 # 0
DST_SHORT_ADDR					= 0b00001000 # BIT3
DST_LONG_ADDR					= 0b00001100 # BIT2 | BIT3
DST_ADDR_MODE					= 0b00001100 # BIT2 | BIT3
SRC_NO_ADDR						= 0b00000000 # 0
SRC_SHORT_ADDR					= 0b10000000 # BIT7
SRC_LONG_ADDR					= 0b11000000 # BIT6 | BIT7
SRC_ADDR_MODE					= 0b11000000 # BIT6 | BIT7

short_addr_registers = {
"RXMCR": 0x00,
"PANIDL": 0x01,
"PANIDH": 0x02,
"SADRL": 0x03,
"SADRH": 0x04,
"EADR0": 0x05,
"EADR1": 0x06,
"EADR2": 0x07,
"EADR3": 0x08,
"EADR4": 0x09,
"EADR5": 0x0A,
"EADR6": 0x0B,
"EADR7": 0x0C,
"RXFLUSH": 0x0D,
"ORDER": 0x10,
"TXMCR": 0x11,
"ACKTMOUT": 0x12,
"ESLOTG1": 0x13,
"SYMTICKL": 0x14,
"SYMTICKH": 0x15,
"PACON0": 0x16,
"PACON1": 0x17,
"PACON2": 0x18,
"TXBCON0": 0x1A,
"TXNCON": 0x1B,
"TXG1CON": 0x1C,
"TXG2CON": 0x1D,
"ESLOTG23": 0x1E,
"ESLOTG45": 0x1F,
"ESLOTG67": 0x20,
"TXPEND": 0x21,
"WAKECON": 0x22,
"FRMOFFSET": 0x23,
"TXSTAT": 0x24,
"TXBCON1": 0x25,
"GATECLK": 0x26,
"TXTIME": 0x27,
"HSYMTMRL": 0x28,
"HSYMTMRH": 0x29,
"SOFTRST": 0x2A,
"SECCON0": 0x2C,
"SECCON1": 0x2D,
"TXSTBL": 0x2E,
"RXSR": 0x30,
"INTSTAT": 0x31,
"INTCON": 0x32,
"GPIO": 0x33,
"TRISGPIO": 0x34,
"SLPACK": 0x35,
"RFCTL": 0x36,
"SECCR2": 0x37,
"BBREG0": 0x38,
"BBREG1": 0x39,
"BBREG2": 0x3A,
"BBREG3": 0x3B,
"BBREG4": 0x3C,
"BBREG6": 0x3E,
"CCAEDTH": 0x3F}

long_addr_registers = {
"RFCON0": 0x200,
"RFCON1": 0x201,
"RFCON2": 0x202,
"RFCON3": 0x203,
"RFCON5": 0x205,
"RFCON6": 0x206,
"RFCON7": 0x207,
"RFCON8": 0x208,
"SLPCAL0": 0x209,
"SLPCAL1": 0x20A,
"SLPCAL2": 0x20B,
"RFSTATE": 0x20F,
"RSSI": 0x210,
"SLPCON0": 0x211,
"SLPCON1": 0x220,
"WAKETIMEL": 0x222,
"WAKETIMEH": 0x223,
"REMCNTL": 0x224,
"REMCNTH": 0x225,
"MAINCNT0": 0x226,
"MAINCNT1": 0x227,
"MAINCNT2": 0x228,
"MAINCNT3": 0x229,
"TESTMODE": 0x22F,
"ASSOEADR0": 0x230,
"ASSOEADR1": 0x231,
"ASSOEADR2": 0x232,
"ASSOEADR3": 0x233,
"ASSOEADR4": 0x234,
"ASSOEADR5": 0x235,
"ASSOEADR6": 0x236,
"ASSOEADR7": 0x237,
"ASSOSADR0": 0x238,
"ASSOSADR1": 0x239,
"UPNONCE0": 0x240,
"UPNONCE1": 0x241,
"UPNONCE2": 0x242,
"UPNONCE3": 0x243,
"UPNONCE4": 0x244,
"UPNONCE5": 0x245,
"UPNONCE6": 0x246,
"UPNONCE7": 0x247,
"UPNONCE8": 0x248,
"UPNONCE9": 0x249,
"UPNONCE10": 0x24A,
"UPNONCE11": 0x24B,
"UPNONCE12": 0x24C}
