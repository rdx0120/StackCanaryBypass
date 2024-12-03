# Stack Canary Bypassing without Stack Smashing

## Overview
This project demonstrates a stack canary bypass exploit using a Python script that integrates with GDB. It showcases advanced techniques such as overwriting the return address, leveraging dead code, and performing x86 assembly-level manipulation on Unix/Linux systems.

---

## Features
- **Interactive Exploit Script**: Automates interaction with GDB to exploit stack canary mechanisms.
- **Payload Generation**: Creates payloads preserving canary values while overwriting return addresses.
- **GDB Integration**: Facilitates memory analysis and debugging in real-time.
- **x86 Assembly Exploitation**: Demonstrates assembly-level hacking concepts for educational purposes.

---

## Prerequisites
- Python 3.x
- GDB installed on the system
- A vulnerable binary file to test the exploit

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stack-canary-bypass.git
   cd stack-canary-bypass
2. Compile a vulnerable binary for testing
   ```bash
   gcc -fno-stack-protector -z execstack -o vulnerable_binary vulnerable.c
3. Run the Python script:
   ```bash
   sudo python stack_canary_bypass.py
4. Analyze the GDB output to validate the exploit.
