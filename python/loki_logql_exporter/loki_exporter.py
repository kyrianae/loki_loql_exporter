from prometheus_client import start_http_server, Gauge
from grafana_loki.loki_api import loki
import time
import json
import datetime

from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

class Loki_exporter():
    def __init__(self,loki_exporter_configuration) -> None:
        self.configuration = loki_exporter_configuration
        self.client = loki(self.configuration['loki']['url'])
        # self.prometheus_exporter =
        REGISTRY.register(self)

    def collect(self):
        now_stamp = datetime.datetime.now()
        print(str(now_stamp)+' '+'collect data')
        for metric in self.configuration['metrics']:

            res = self.client.query(
                metric['time_window'],
                metric['query'],
                metric['limit'],
                metric['step']
            )

            j = json.loads(res.content)

            for r in j['data']['result']:
                labels_keys = []
                labels_values = []

                for l in r['metric']:
                    labels_keys.append(l)
                    labels_values.append(r['metric'][l])

                c = CounterMetricFamily(metric['field'], metric['description'], labels=labels_keys)
                for step in r['values']:
                    c.add_metric(labels_values, step[1], timestamp=step[0])
                yield c

    def listen(self):
        start_http_server(self.configuration['exporter']['port'])
        while True:
            time.sleep(1)



