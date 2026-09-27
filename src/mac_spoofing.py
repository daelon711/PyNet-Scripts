import subprocess
import random

# LINUX ONLY
# get active device


def interface():
    # makes output savable and turns b"" into text
    res = subprocess.run("ip route show", shell=True,
                         capture_output=True, text=True)

    result = res.stdout  # saves output
    for line in result.split("\n"):
        # get the line where its :default via" ( interface name comes right after)
        if "default via" in line:
            interface = line.split("dev")[1]  # [1] picks index 1 in list
            # to grep right after dev cuz thats what cur network is then split by “ ” and grab first word which is interface
            return interface.split()[0]
    return None


def randomize_mac():  # makes random MAC addr
    mac = ""
    for _ in range(6):
        mac += random.choice('0123456789ABCDEF') + \
            random.choice('0123456789ABCDEF') + ":"

    mac = mac[:-1]  # removes last :
    return mac


def spoof():  # actual spoofing action
    network = interface()
    if network == None:
        return

    mac = randomize_mac()

    # put interface down
    # its like turning the light off and then on until u change the lightbulb
    # ensures that the operating system does not try to use the interface while you're modifying its settings, which could cause errors

    subprocess.call(f"ip link set dev {network} down", shell=True)
    subprocess.call(f"ip link set dev {network} address {mac}", shell=True)
    subprocess.call(f"ip link set dev {network} up", shell=True)
    subprocess.call("ip a", shell=True)  # confirm change by outputting


if __name__ == "__main__":
    spoof()
