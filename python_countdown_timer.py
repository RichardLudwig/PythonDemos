# Imports
import time

# Main loop function
def main():
    # User input for countdown in seconds
    seconds = int(input("Enter countdown (in seconds): "))

    # Countdown loop
    # Range counts backwards with steps of -1, from the seconds input to 0
    for i in range(seconds, 0, -1):
        # If i is greater than 0 (if the countdown is still occurring)
        if i > 0:
            # Print the countdown on the same line
            print(str(i) + "... ", end="")
            # Pause the program 1 seconds between counts
            time.sleep(1)

    # Print when countdown done
    print("Countdown Done")

    # User input to reset program 
    reset = int(input("Enter 1 to reset and 0 to exit the program: "))

    # Reset program by re-generating main loop function
    if (reset == 1):
        main()
    # Exit program
    if (reset == 0):
        exit()

# Generate main loop function
main()
