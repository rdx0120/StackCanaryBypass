set logging enabled on
set pagination off
set disable-randomization on
break vulnerable_function
commands
    printf "Memory Layout at Breakpoint:\\n"
    x/gx $esp
    info registers
    info stack
end
run
printf "Checking for deadcode execution...\\n"
continue
printf "Exploit Test Complete\\n"
