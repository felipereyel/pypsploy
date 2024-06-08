import psutil
import time


def main(pid: str, interval: int = 1):
    p = psutil.Process(pid)

    while True:
        mem = int(p.memory_info().rss / 1024 / 1024)
        cpu = p.cpu_percent()
        with open(f'psplot.{pid}.dat', 'a') as f:
            f.write(f'{mem} {cpu}')
            f.write('\n')
            time.sleep(interval)

if __name__ == "__main__":
    main()

