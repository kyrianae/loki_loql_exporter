import yaml
from loki_exporter import Loki_exporter
import json

# stream = open("translation.yml", encoding='utf-8')
stream = open("loki_exporter.yml", encoding='utf-8')
loki_exporter_configuration= yaml.load(stream, Loader=yaml.Loader)

exporter = Loki_exporter(loki_exporter_configuration)

# res = exporter.client.query(
#     60,
# 'max_over_time({filename="/var/log/test_extract.log"}| regexp "(?P<id>.+) (?P<value>.+)"| unwrap value | __error__="" [5s])'
# # '{filename="/var/log/test_extract.log"}| regexp "(?P<id>^\S+) "'
#     ,1000)
#
# j = json.loads(res.content)
# # print(j['data']['result'])

exporter.listen()