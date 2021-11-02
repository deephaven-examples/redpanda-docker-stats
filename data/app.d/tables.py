from deephaven import ConsumeKafka as ck
from deephaven import Types as dht

docker_stats = ck.consumeToTable({'bootstrap.servers': 'redpanda:29092'} , 'docker_stats', key=ck.IGNORE, value=ck.json([
    ('container', dht.string),
    ('name',   dht.string),
    ('cpuPercent',  dht.double),
    ('memoryUsage',   dht.int64),
    ('memoryLimit', dht.int64),
    ('memoryPercent',   dht.double),
    ('networkInput',  dht.int64),
    ('networkOutput',    dht.int64),
    ('blockInput',  dht.int64),
    ('blockOutput',    dht.int64),
    ('pids',    dht.int32)
    ]),table_type = 'append')

latest_results = docker_stats.lastBy("name")


from deephaven import Plot

memoryUsage = Plot.plot("envoy", docker-stats.where("name = 'redpanda-docker-stats_envoy_1'"), "KafkaTimestamp", "memoryUsage").plot("web", docker-stats.where("name = 'redpanda-docker-stats_web_1'"), "KafkaTimestamp", "memoryUsage").plot("redpanda", docker-stats.where("name = 'redpanda-docker-stats_repanda_1'"), "KafkaTimestamp", "memoryUsage").plot("registry", docker-stats.where("name = 'redpanda-docker-stats_registry_1'"), "KafkaTimestamp", "memoryUsage").plot("grpc-api", docker-stats.where("name = 'redpanda-docker-stats_grpc-api_1'"), "KafkaTimestamp", "memoryUsage").plot("grpc-proxy", docker-stats.where("name = 'redpanda-docker-stats_grpc-proxy_1'"), "KafkaTimestamp", "memoryUsage").show()
