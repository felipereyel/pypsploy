import plotext as plt


def main(fname: str, interval: int = 1, ylim: int = 1000, tail: int = -1):
    with open(fname) as f:
        cpus = []
        mems = []

        for line in f.readlines():
            mem, cpu = line.split()
            mems.append(int(mem))
            cpus.append(float(cpu))

        if tail > 0:
            tail_idx = -1 * int(tail/interval)
            print(tail_idx)
            cpus = cpus[tail_idx:]
            mems = mems[tail_idx:]

        plt.title(f"PID {fname}")
        plt.theme("matrix")

        plt.plot(mems, yside="right", label="memory (MB)")
        plt.ylim(0, ylim, yside="right")

        plt.plot(cpus, yside="left", label="cpu (%)")
        plt.ylim(0, 1, yside="left")

        plt.show()


if __name__ == "__main__":
    main()

