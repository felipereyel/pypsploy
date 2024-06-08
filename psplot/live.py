import psutil
import plotext as plt


def main(pid: str, interval: int = 1, ylim: int = 1000):
    p = psutil.Process(pid)

    plt.title(f"PID {pid}")
    plt.theme("matrix")

    try:
        cpus = []
        mems = []

        while True:
            plt.cld()
            plt.clt()

            mem = int(p.memory_info().rss / 1024 / 1024)
            cpu = p.cpu_percent()

            mems.append(mem)
            cpus.append(cpu)

            plt.plot(mems, yside="right", label="memory (MB)")
            plt.ylim(0, ylim, yside="right")

            plt.plot(cpus, yside="left", label="cpu (%)")
            plt.ylim(0, 1, yside="left")

            plt.show()
            plt.sleep(interval)
    except:
        with open(f'psplot.{pid}.dat', 'w') as f:
            for i in range(len(mems)):
                f.write(f'{mems[i]} {cpus[i]}\n')


if __name__ == "__main__":
    main()

