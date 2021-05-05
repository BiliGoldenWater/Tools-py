# -*- coding: utf-8 -*-

# @File    : handshake.py
# @Date    : 2019-12-27
# @Author  : 王超逸
# @Brief   : 模拟握手

# 小写的类名有点难受
from socket import socket as Socket
from protocol.session import Session
from protocol.mcString import MCString
from protocol.packet import Packet
from protocol.varNum import VarInt, VarLong
from protocol.mcInt import Byte, UnsignedByte, Short, UnsignedShort, Integer, UnsignedInteger, Long, UnsignedLong

import time


def on_packet_recv(packet: Packet):
    if packet.id == 0:
        mcString, = packet.parse([MCString])
        try:
            print("0: ", mcString.get())
        except TypeError and UnicodeDecodeError:
            print("0: ", packet.data)
    elif packet.id == 0x02:
        print("2: ", packet.id)
    elif packet.id == 0x04:
        print("4: ", packet.data)
    elif packet.id == 0x0e:
        print("e: ", packet.data)
    else:
        print(packet.id, ": ", packet.parse([VarInt])[0].get())


def handshake(session, address, protocol_version, next_state):
    packet = Packet(id=0)
    # 协议号，-1表示获取协议号
    packet.addField(VarInt(protocol_version))
    # host
    packet.addField(MCString(address[0]))
    # port
    packet.addField(UnsignedShort(address[1]))
    # Next state
    packet.addField(VarInt(next_state))
    session.sendPacket(packet)


def login(name):
    packet = Packet(0)
    packet.addField(MCString(name))
    session.sendPacket(packet2)


if __name__ == "__main__":
    # server_address = ("cn-zz-bgp-2.sakurafrp.com", 64360)
    server_address = ("127.0.0.1", 25565)

    socket = Socket()
    socket.connect(server_address)
    session = Session(socket, on_packet_recv)

    handshake(session, server_address, 340, 2)

    packet2 = Packet(0)
    packet2.addField(MCString("randomName"))
    session.sendPacket(packet2)

    # time.sleep(5)

    # packet2 = Packet(id=0x03)
    # packet2.addField(MCString("test"))
    # session.sendPacket(packet2)
