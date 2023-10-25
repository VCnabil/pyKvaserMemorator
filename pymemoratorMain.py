# check_ch
# Firstly import canlib so that it can be used in the script.
from canlib import canlib, Frame

# .getNumberOfChannels() is used to detect the number of channels and
# the number is saved in the variable num_channels.
num_channels = canlib.getNumberOfChannels()

# num_channels is printed out as text so that the user can see how many
# channels were found.
print(f"Found {num_channels} channels")

# Next a for loop is created. This loop will repeat the code within for each
# channel that was detected. 
for ch in range(num_channels):
# The data of each specific channel is saved in chd.
    chd = canlib.ChannelData(ch)
# Lastly the channel, channel name, product number, serial number, and local 
# channel number on the device are printed.
    print(f"{ch}. {chd.channel_name} ({chd.card_upc_no.product()}:{chd.card_serial_no}/{chd.chan_no_on_card})")
    
    
# Firstly, open two CAN channels, one to send the message and one to receive.
# Note that there needs to be a channel to receive, as otherwise the message
# can not be sent. In this example the channels are named ch_a and ch_b. To
# open the channels call on the openChannel method inside of canlib and, as an
# input put in channel=0 and channel=1. Where 0 and 1 represents the two
# CANlib channels 0 and 1.
ch_a = canlib.openChannel(channel=0)
ch_b = canlib.openChannel(channel=1)

# After opening the channel, we need to set the bus parameters. Some
# interfaces keep their params from previous programs. This can cause problems
# if the params are different between the interfaces/channels. For now we will
# use setBusParams() to set the canBitrate to 250K.
ch_a.setBusParams(canlib.canBITRATE_250K)
ch_b.setBusParams(canlib.canBITRATE_250K)

# The next step is to Activate the CAN chip for each channel (ch_a and ch_b in
# this example) use .busOn() to make them ready to receive and send messages.
ch_a.busOn()
ch_b.busOn()

# To transmit a message with (11-bit) CAN id = 123 and contents (decimal) 72,
# 69, 76, 76, 79, 33, first create the CANFrame (CANmessage) and name it. In
# this example, the CANFrame is named frame. Then send the message by calling on
# the channel that will act as the sender and use .write() with the CANFrame
# as input. In this example ch_a will act as sender.
frame = Frame(id_=0x18FF0100, data=[72, 69, 76, 76, 79, 33], flags=canlib.MessageFlag.EXT )
ch_a.write(frame)

# To make sure the message was sent we will attempt to read the message. Using
# timeout, only 500 ms will be spent waiting to receive the CANFrame. If it takes
# longer the program will encounter a timeout error. read the CANFrame by calling
# .read() on the channel that receives the message, ch_b in this example. To
# then read the message we will use print() and send msg as the input.
msg = ch_b.read(timeout=500)
print(msg)

# After the message has been sent, received and read it is time to inactivate
# the CAN chip. To do this call .busOff() on both channels that went .busOn()
ch_a.busOff()
ch_b.busOff()

# Lastly, close all channels with close() to finish up.
ch_a.close()
ch_b.close()

# Depending on the situation it is not always necessary or preferable to go of
# the bus with the channels and, instead only use close(). But this will be
# talked more about later.