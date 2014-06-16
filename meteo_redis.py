from datetime import date,timedelta
import numpy
import random

# creamos datos fake
variables = ['temp','hum','u','v','precip','haines','t850']
modelos = ['gfs','ecmwf_ens','ecmfw_det','arpege','rap','ruc']
fechas = [(date.today() - timedelta(x)).strftime("%Y%m%d")  for x in xrange(20000)]
valores = numpy.random.normal(0,1,10000)


def dame_key():
    return     "_".join([random.choice(variables),random.choice(modelos),random.choice(fechas)])


def dame_valor():
    return random.choice(valores)
