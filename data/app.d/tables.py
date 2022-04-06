from deephaven import kafka_consumer as ck
from deephaven.stream.kafka.consumer import TableType, KeyValueSpec
from deephaven import dtypes as dht

docker_stats = ck.consume({'bootstrap.servers': 'redpanda:29092'} , 'docker_stats', key_spec=KeyValueSpec.IGNORE, value_spec=ck.json_spec([
    ('container', dht.string),
    ('name', dht.string),
    ('cpuPercent', dht.double),
    ('memoryUsage', dht.int64),
    ('memoryLimit', dht.int64),
    ('memoryPercent', dht.double),
    ('networkInput',  dht.int64),
    ('networkOutput', dht.int64),
    ('blockInput',  dht.int64),
    ('blockOutput', dht.int64),
    ('pids', dht.int32)
    ]), table_type = TableType.Append)

latest_results = docker_stats.last_by(["name"])

from deephaven.plot.figure import Figure
figure = Figure()

memoryUsage = figure.plot_xy(series_name ="envoy", t=docker_stats.where(["name = 'redpanda-docker-stats_envoy_1'"]), x="KafkaTimestamp", y="memoryUsage")\
    .plot_xy(series_name ="web", t=docker_stats.where(["name = 'redpanda-docker-stats_web_1'"]), x="KafkaTimestamp", y="memoryUsage")\
    .plot_xy(series_name ="redpanda", t=docker_stats.where(["name = 'redpanda-docker-stats_redpanda_1'"]), x="KafkaTimestamp", y="memoryUsage")\
    .plot_xy(series_name ="registry", t=docker_stats.where(["name = 'redpanda-docker-stats_envoy_1'"]), x="KafkaTimestamp", y="memoryUsage")\
    .plot_xy(series_name ="server", t=docker_stats.where(["name = 'redpanda-docker-stats_server_1 '"]), x="KafkaTimestamp", y="memoryUsage")\
    .plot_xy(series_name ="grpc-proxy", t=docker_stats.where(["name = 'redpanda-docker-stats_grpc-proxy_1'"]), x="KafkaTimestamp", y="memoryUsage")\
    .show()
