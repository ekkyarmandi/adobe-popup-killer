import psutil
import datetime as dt
import argparse
import time


def kill_process_by_pid(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()  # Send a termination signal
        process.wait(timeout=5)  # Wait for the process to terminate gracefully
        return True
    except psutil.NoSuchProcess:
        print(f"Error: Process with PID {pid} not found.")
    except psutil.AccessDenied:
        print(f"Error: Permission denied to terminate process with PID {pid}.")
    except Exception as e:
        print(f"Error: {e}")

    return False


def get_all_process():
    processes = []
    for process in psutil.process_iter(["pid", "name", "status"]):
        if process.info["status"] == psutil.STATUS_RUNNING:
            processes.append(
                {
                    "pid": process.info["pid"],
                    "name": process.info["name"],
                    "status": process.info["status"],
                }
            )
    return processes


target = [
    "AdobeGCClient",
    "Adobe_CCXProcess.node",
    "Adobe Genuine Software Monitor Service",
    "Adobe Desktop Service",
]

parser = argparse.ArgumentParser(
    prog="Adobe Killer",
    description="Kill any adobe popup ",
)

parser.add_argument("-d", "--debug", action="store_true", default=False)
parser.add_argument("-t", "--time", type=int, default=5)

args = parser.parse_args()

is_debug = args.debug

# query the list every 3 sec
while True:
    now = dt.datetime.now().strftime(r"%Y-%m-%d_%T")
    if args.debug:
        print(now)
        print("=" * 30, end="")
        print("START", end="")
        print("=" * 30)
    processes = get_all_process()
    for service in processes:
        name = service["name"]
        if "adobe" in name.lower():
            if is_debug:
                print(service)
            if name in target:
                kill_process_by_pid(service["pid"])
    if is_debug:
        print("=" * 31, end="")
        print("END", end="")
        print("=" * 31)
    time.sleep(args.time)
