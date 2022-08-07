import ulogging

import config

_level_dict = {
  'CRITICAL': ulogging.CRITICAL,
  'ERROR': ulogging.ERROR,
  'WARNING': ulogging.WARNING,
  'INFO': ulogging.INFO,
  'DEBUG': ulogging.DEBUG,
}

_logger = ulogging.getLogger(config.LOG_NAME)
_logger.setLevel(_level_dict[config.LOG_LEVEL])

def log(level, msg, *args):
  _logger.log(level, msg, *args)

def debug(msg, *args):
  _logger.debug(msg, *args)

def info(msg, *args):
  _logger.info(msg, *args)

def warning(msg, *args):
  _logger.warning(msg, *args)

def error(msg, *args):
  _logger.error(msg, *args)

def critical(msg, *args):
  _logger.critical(msg, *args)

def exc(e, msg, *args):
  _logger.exc(e, msg, *args)

def exception(msg, *args):
  _logger.exception(msg, *args)
