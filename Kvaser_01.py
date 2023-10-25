#Kvaser_01.py:
from canlib import canlib, Frame
data_array = [22, 17, 14, 0x22, 0x17, 0x14]

def runWriteCanPythonic(can_id):
    with canlib.openChannel(0) as ch_a, canlib.openChannel(1) as ch_b:
        for ch in [ch_a, ch_b]:
            ch.busOn()
        frame = Frame(can_id, data=[72, 69, 76, 76, 79, 33], flags=canlib.MessageFlag.EXT)
        ch_a.write(frame)
        msg = ch_b.read(timeout=500)
        print(msg)

def runWriteCanPythonicCh1(can_id):
    with canlib.openChannel(0) as ch_a:
        ch_a.busOn()
        frame = Frame(can_id, data=[72, 69, 76, 76, 79, 33], flags=canlib.MessageFlag.EXT)
        ch_a.write(frame)
        #msg = ch_a.read(timeout=500)
        #print(msg)
        
def testfunc(): 
    print("should this print?")   
    runWriteCanPythonicCh1(0x18FF0100)
    #runWriteCan()   
    #runWriteCan2chan()

def runWriteCan():
    ch_a = canlib.openChannel(channel=0)
    ch_a.setBusParams(canlib.canBITRATE_250K)
    ch_a.busOn()
    frame = Frame(id_=0x18FF0100, data=data_array, flags=canlib.MessageFlag.EXT)
    ch_a.write(frame)
    msg = frame.data
    print(msg)
    ch_a.busOff()
    ch_a.close()
    
def runWriteCan2chan():
    ch_a = canlib.openChannel(channel=0)
    ch_b = canlib.openChannel(channel=1)
    ch_a.setBusParams(canlib.canBITRATE_250K)
    ch_b.setBusParams(canlib.canBITRATE_250K)
    ch_a.busOn()
    ch_b.busOn()
    frame = Frame(id_=0x18FF0100, data=data_array, flags=canlib.MessageFlag.EXT)
    ch_a.write(frame)
    msg = ch_b.read(timeout=500)
    print(msg)
    ch_a.busOff()
    ch_b.busOff()
    ch_a.close()
    ch_b.close()          

if __name__ == "__main__":
    testfunc()