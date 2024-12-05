#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h> 

uint32_t canary;

// To simulate return flow
void (*execute_payload)(void);

// For exploitation
void payload() {
    printf("Payload executed! You have bypassed the stack canary.\n");
    exit(0);
}

void deadcode() {
    printf("Dead code executed!\n");
    FILE *fp = fopen("deadcode_execution.txt", "a+");
    fprintf(fp, "Dead code was executed at %s\n", __TIME__);
    fclose(fp);
}

void initialize_canary() {
    canary = rand();
    printf("Stack canary initialized to: 0x%x\n", canary);
}

void check_canary(uint32_t user_canary) {
    if (user_canary != canary) {
        printf("Stack smashing detected! Exiting...\n");
        exit(1);
    }
}

void vulnerable_function() {
    char buffer[64];  
    uint32_t local_canary = canary;

    printf("Enter some input:\n");
    gets(buffer);  

    // if the stack canary was tampered with
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

    // Optionally set up a function pointer to deadcode for demonstration
    execute_payload = deadcode;  // Change to NULL or payload() as needed for testing

    vulnerable_function();

    return 0;
}
