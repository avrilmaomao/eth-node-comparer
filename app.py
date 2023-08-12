import os

from flask import Flask
import service.node_info as node_info
import service.MetricBuilder as MetricBuilder

app = Flask(__name__)


@app.route("/")
def say_hello():
    return "Hello"


@app.route("/metrics")
def print_metrics():
    local_node_url: str = os.getenv('LOCAL_NODE')
    nodes_to_compare: str = os.getenv('COMPARE_NODE')
    if local_node_url is None or nodes_to_compare is None:
        app.logger.error('local node or compare nodes empty')
        return "empty local nodes or compare nodes"
    # local first
    local_block_num: int = node_info.get_latest_block(local_node_url)
    compare_block_num: int = node_info.get_latest_block(nodes_to_compare)
    metrics: list[str] = list()
    metrics.append(MetricBuilder.build_prometheus_metric('local_node_behind_block_num', compare_block_num - local_block_num))
    metrics.append(MetricBuilder.build_prometheus_metric('local_node_block_num', local_block_num))
    return '\n'.join(metrics)

