# Stack Canary Bypass Exploit Toolkit

## Overview
This toolkit is designed to demonstrate and educate on the exploitation of buffer overflow vulnerabilities while preserving stack canary values. The Python script provided automates the process of exploiting a simple C program (`vulnerable.c`) that contains deliberate vulnerabilities, including weak stack canary implementations. This educational tool is intended to provide insights into system vulnerabilities, memory layout, and the basics of stack canaries and buffer overflows.

## Features
- **Dynamic Binary Analysis**: Automatically extracts memory layout information such as buffer sizes and stack canary locations.
- **Interactive Exploit Crafting**: Allows users to manually adjust exploit parameters in real-time.
- **Automated GDB Integration**: Uses GDB to automate the debugging and exploit execution process.
- **Visualization Tools**: Offers a simple visualization of memory layout to aid understanding of the exploit process.
- **Automated Payload Testing**: Tests various payloads to find successful exploits against the buffer overflow vulnerability.

## Prerequisites
- GCC for compiling the C program.
- Python 3.x for running the exploit script.
- GDB installed on your Unix/Linux system for automated debugging.
- Basic knowledge of C programming, Python scripting, and debugging with GDB.

## Setup Instructions

### Compiling the Vulnerable Program
First, ensure GCC is installed on your system. You can compile the `vulnerable.c` file using the following command:
```bash
gcc -o vulnerable_binary vulnerable.c -fno-stack-protector -z execstack -no-pie
```
This command compiles the C program with stack protection disabled to facilitate testing of the exploit

### Setting up the Python Exploit Script
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/stack-canary-bypass.git
   cd stack-canary-bypass

2. Navigate to the directory containing the exploit script.

3. Run the Python script:
   ```bash
   sudo python3 stack_canary_bypass.py

## Usage
After setting up, you can run the Python script as described above. The script will:

- Analyze the binary to locate the canary and buffer addresses.
- Create and test various payloads based on the extracted addresses.
- Automatically run GDB to demonstrate how the exploit affects the program's execution.
