from ssg import hooks
import time

start_time = None
total_written = 0

@start_build
def start_build():
    global start_time
    start_time = time.time()

@written
def written():
    global total_written
    total_written += 1

@stats
def stats():
    final_time = start_time - time.time()
    if total_written != 0:
        average = final_time / total_written
    report = "Converted: {} · Time: {:.2f} sec · Ave: {:.4f} sec/file"
    print(report.format(total_written, final_time, average))
