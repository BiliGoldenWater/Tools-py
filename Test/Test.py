import socket


def package(pack_id, protocol_version, data):
    final_data = bytearray(pack_id)
    final_data.append(data)

    return final_data.hex()


#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("cn-zz-bgp-2.sakurafrp.com", 64360))
#
# s.send("test".encode())

print(package(bytes.fromhex("00"), bytes("test".encode())))
