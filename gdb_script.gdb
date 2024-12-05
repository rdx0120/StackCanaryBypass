set logging enabled on
set pagination off
set disable-randomization on
break vulnerable_function
commands
    printf "Memory Layout at Breakpoint:\\n"
    x/24wx $esp
    info registers
end
run
printf "Checking for deadcode execution...\\n"
continue
printf "Exploit Test Complete\\n"
