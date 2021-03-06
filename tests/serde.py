"""
Tests serialization and deserialization of an audiosegment.
"""
import audiosegment as asg
import read_from_file
import sys

def test(seg):
    print("Serializing segment...")
    ser = seg.serialize()
    print("Deserializing...")
    des = asg.deserialize(ser)
    print("Name:", des.name)
    return des

if __name__ == "__main__":
    seg = read_from_file.test(sys.argv[1])
    test(seg)
