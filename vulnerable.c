#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

// Stack canary value
uint32_t canary;

// Function pointer to simulate return flow
void (*execute_payload)(void);

// Placeholder function for exploitation
void payload() {
    printf("Payload executed! You have bypassed the stack canary.\n");
    exit(0);
}

// Function to initialize the stack canary
void initialize_canary() {
    canary = rand();
    printf("Stack canary initialized to: 0x%x\n", canary);
}

// Function to check the stack canary
void check_canary(uint32_t user_canary) {
    if (user_canary != canary) {
        printf("Stack smashing detected! Exiting...\n");
        exit(1);
    }
}

// Vulnerable function
void vulnerable_function() {
    char buffer[64];  // Buffer vulnerable to overflow
    uint32_t local_canary = canary;

    printf("Enter some input:\n");
    gets(buffer);  // Vulnerable to overflow

    // Check if the stack canary was tampered with
    check_canary(local_canary);

    // If stack canary is intact, execute the function pointer
    if (execute_payload) {
        execute_payload();
    } else {
        printf("No payload executed.\n");
    }
}

int main() {
    // Seed randomness for canary
    srand(time(NULL));
    initialize_canary();

    // Set up a function pointer
    execute_payload = NULL;

    // Call the vulnerable function
    vulnerable_function();

    return 0;
}
