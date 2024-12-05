# Stack Canary Bypass without Stack Smashing

## Overview
This project demonstrates techniques in exploiting buffer overflow vulnerabilities by bypassing stack canary protections and redirecting execution flow to normally non executable or rarely executed sections of code (`deadcode`). The provided Python script automates the exploitation process of a deliberately vulnerable C program, showcasing how to manipulate execution flow in a controlled manner.

## Features
- **Buffer Overflow Exploit**: Demonstrates how to overflow a buffer and manipulate the stack to bypass stack protections and execute arbitrary code.
- **Deadcode Execution**: Exploits include triggering execution of `deadcode()`, a function normally not executed during standard program operations.
- **Dynamic Memory Analysis**: Automatically extracts critical information such as stack canary values and function addresses from the binary for precise payload crafting.
- **Automated GDB Integration**: Uses GDB to automate the debugging and execution process, providing real-time feedback on exploit effectiveness.
- **Memory Layout Visualization**: Offers a simple visualization of critical memory layout points like canary locations and the address of `deadcode()` to aid understanding.

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
   git clone https://github.com/yourusername/StackCanaryBypass.git
   cd StackCanaryBypass

2. Navigate to the directory containing the exploit script.

3. Run the Python script:
   ```bash
   sudo python3 stack_canary_bypass.py

## Usage
Execute the following steps to use the exploit script effectively:

1. **Run the Script**: Launch `python3 stack_canary_bypass.py` from your command line to start the automated exploitation process.

2. **Observe Automated Analysis**: Monitor as the script analyzes the binary, identifying crucial memory addresses such as the canary and `deadcode()` function locations.

3. **Payload Execution**: The script will create and apply a payload via GDB, demonstrating how the execution flow is redirected to `deadcode()`.

4. **Review Results**
