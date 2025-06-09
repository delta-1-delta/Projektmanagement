import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime

def plot_gantt(aufgabenliste):
    fig, ax = plt.subplots(figsize=(6,4))
    
    for idx, (name, start_str, dauer_str) in enumerate(aufgabenliste):
        try:
            start_date = datetime.strptime(start_str, "%Y-%m-%d")
            dauer = int(dauer_str)
        except:
            continue

        ax.barh(idx, dauer, left=start_date, height=0.4)
    
    ax.set_yticks(range(len(aufgabenliste)))
    ax.set_yticklabels([a[0]for a in aufgabenliste])
    ax.set_xlabel("Datum")
    ax.set_title("Gantt-Diagramm")
    fig.autofmt_xdate()

    return FigureCanvas(fig)