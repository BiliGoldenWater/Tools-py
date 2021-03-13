import asyncio
import websocket
import socket

async def main():
    socket.create_connection("")
    async with websocket.WebSocket() as ws:
        ws