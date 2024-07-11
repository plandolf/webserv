#!/usr/bin/env python3

import os

def shutdown_server():
    print("Shutting down the server in 30 seconds...")
    os.system("shutdown -h +0.1")

if __name__ == "__main__":
    shutdown_server()

