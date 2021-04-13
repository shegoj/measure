import json
import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server


class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        f = open ('../records/tt.json')
        data = json.load(f)
        length_ =  len (data [0])

        i = 0

        while i < length_:
            for k,v in enumerate(data [0][i]['payload']):
                record  = data [0][i]['payload'][v]
                field = ""
                value = ""
                if v not in ("InverterData", "EnergyData", "MiscData", "BatteryData", "InvAggrData"):
                    field = str(v).lower()
                    value = record
                    try:
                        x = float (value)
                        print ("%s : %f" % (field,x))
                        g = GaugeMetricFamily(field, '', labels=[])
                        g.add_metric([], x)
                        yield g
                    except:
                        pass
                else:
                    if v in  ( "EnergyData", "InverterData"):
                        record = record [0]
                        field = str(v).lower()
                        value = record
                        try:
                            x = float (value)
                            print ("%s : %f" % (field,x))
                            g = GaugeMetricFamily(field, '', labels=[])
                            g.add_metric([], x)
                            yield g
                        except:
                            pass

                    for m,n in enumerate(record):
                        field = n
                        field = str(n).lower()
                        value = record [n]
                        try:
                            x = float (value)
                            print ("%s : %f" % (field,x))
                            g = GaugeMetricFamily(field, '', labels=[])
                            g.add_metric([], x)
                            yield g
                        except:
                            pass
            i = i + 1
    


if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(10)

