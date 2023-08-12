import time


def build_prometheus_metric(name: str, value: float, report_time: int = None) -> str:
    if report_time is None:
        report_time = int(time.time() * 1000)
    return "{} {} {}".format(name, value, report_time)
