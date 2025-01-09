# Stack Canary Bypass without Stack Smashing

## Overview
Ever wondered how vulnerabilities bypass even the most tough defenses? That’s exactly what I explored in this project. By creating a controlled exploit, I demonstrated how to bypass stack canary protections and manipulate program flow. With a Python script and a vulnerable C program, I was able to redirect execution to the rarely executed deadcode() function, showcasing how exploits work in a safe and structured way

## Features
- **Buffer Overflow Exploit**: Learned how to overflow a buffer, bypass stack canaries, and manipulate execution flow.
- **Deadcode Execution**: Trigger the rarely executed `deadcode()` function, adding a bit of mystery to your exploit.
- **Dynamic Memory Analysis**: Watch as the script extracts key memory details like the canary and function addresses, making payload crafting precise and straightforward.
- **Automated Debugging**: GDB integration allows you to focus on the exploit while automating the heavy debugging work.
- **Memory Layout Visualization**: I mapped out critical memory points, making complex concepts easier to follow and explain.

## Prerequisites
- **GCC:** For compiling the C program.
- **Python 3.x:** for running the exploit script.
- **GDB:** For debugging and testing on Unix.
- Curiosity: If you love understanding how things break (and get fixed), this is for you!

## Setup Instructions

### Compiling the Vulnerable Program
First, ensure GCC is installed on your system. You can compile the `vulnerable.c` file using the following command:
```bash
gcc -g -o vulnerable_binary vulnerable.c -fno-stack-protector -z execstack -no-pie
```
This step disables security features, making the program ideal for testing the exploit.

### Setting up the Python Exploit Script
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/StackCanaryBypass.git
   cd StackCanaryBypass

2. Run the Python script:
   ```bash
   sudo python3 stack_canary_bypass.py

## Usage

1. **Run the Script**: Start the exploit process with `python3 stack_canary_bypass.py` from your command line.

2. **Monitor the Analysis**: The script automatically identified key memory points like the canary and `deadcode()` addresses.

3. **Payload Execution**: The script will create and apply a payload via GDB, demonstrating how the execution flow is redirected to `deadcode()`.

4. **Review Results**
