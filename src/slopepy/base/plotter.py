import matplotlib.pyplot as plt


def plot_slope_protocol(x, y, results, x_label, y_label):
    pw_fit = results["pw_fit"]

    plt.figure()
    plt.scatter(x, y, s=6, color="red", label=y_label)

    pw_fit.plot_fit(color="blue", linewidth=2)
    pw_fit.plot_breakpoints()
    pw_fit.plot_breakpoint_confidence_intervals()

    plt.axvline(results["breakpoint1"], color="magenta", label="Breakpoint 1")
    plt.axvline(results["breakpoint2"], color="orange", label="Breakpoint 2")

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()