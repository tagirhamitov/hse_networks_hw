import subprocess
import sys


def try_mtu(host, mtu):
    print(f"Trying MTU: {mtu}")
    result = subprocess.run(
        ['ping', host, '-M', 'do', '-s', str(mtu), '-c', '1'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def main():
    host = sys.argv[1]
    min_mtu = 1
    max_mtu = 1600
    while max_mtu - min_mtu > 1:
        mtu = (min_mtu + max_mtu) // 2
        if try_mtu(host, mtu):
            min_mtu = mtu
        else:
            max_mtu = mtu
    print(min_mtu)


if __name__ == "__main__":
    main()
