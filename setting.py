import os
from tornado.options import define, options

define("port", default=80, help="run on the given port", type=int)

settings = {}
settings['token'] = "0cf21ca674ee11e3987122000afa135c"
settings['debug'] = True
settings['root_path'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "")
settings['template_path'] = os.path.join(settings['root_path'], "template")
settings['static_path'] = os.path.join(settings['root_path'], "static")

settings['xsrf_cookies'] = False
settings['cookie_secret'] = "EEB1C2AB05DDF04D35BADFDF776DD4B0"

settings['logname'] = 'dyf'
settings['logfilesize'] = 10*1024*1024
settings['backupCount'] = 0
settings['loglevels'] = {"NOTSET" : 0, "DEBUG" : 10, "INFO" : 20, "WARNING" : 30, "WARN" : 30, "ERROR" : 40, "CRITICAL" : 50, "FATAL" : 50}
settings['loglvl'] = settings['loglevels']['INFO']
settings['logformat'] = '%(asctime)s\t%(levelname)s\t%(message)s'
settings['logdatefmt'] = '%a, %d %b %Y %H:%M:%S'
settings['logfilemode'] = 'a'
settings['loginfopath'] = 'info/' + settings['logname'] + '.info.log'
settings['loginwarnpath'] = 'warn/' + settings['logname'] + '.warn.log'
settings['logerrorpath'] = 'error/' + settings['logname'] + '.error.log'