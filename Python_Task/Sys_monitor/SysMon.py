import psutil
import time

# displaying the message
print("monitoring system... (Ctrl+C to stop)")

# opening the file to write the logs
with open("SysMon.log", "w") as file:
    try:
        while True:
            # getting cpu and memeory usage
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent

            # writing to file
            file.write("CPU USAGE: " + str(cpu) + "%\n")
            file.write("MEMORY USAGE:" + str(memory) + "%\n")
            file.write("\n")

            # wait 5 mins before checking again
            time.sleep(5)

    except KeyboardInterrupt:
        print("Monitoring stopped. check SysMon.log for logs")

    finally:
        file.close()
