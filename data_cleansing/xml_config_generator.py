#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""xml_config_generator.py"""

__author__ = 'Gary.Z'

import os
from data_cleansing.clock import *

logger = get_logger(__name__)


class XmlConfigGenerator:
    def __init__(self, input_folder, output_file):
        self._input_file = input_folder
        self._output_file = output_file
        self._with_kdbtime_filter = False
        self._logger = get_logger('{}${}'.format(self.__class__.__name__, id(self)))

    def _get_error_file(self):
        dirpath, filename = os.path.split(self._output_file)
        name, ext = os.path.splitext(filename)
        return os.path.join(dirpath, '{}_error.txt'.format(name))

    def _get_log_file(self):
        dirpath, filename = os.path.split(self._output_file)
        name, ext = os.path.splitext(filename)
        return os.path.join(dirpath, '{}_runlog.txt'.format(name))

    @property
    def logger(self):
        return self._logger

    @property
    def with_kdbtime_filter(self):
        return self._with_kdbtime_filter

    @with_kdbtime_filter.setter
    def with_kdbtime_filter(self, value):
        self._with_kdbtime_filter = value

    @clocking
    def run(self):
        raise Exception('not implement')

    def _log_header(self):
        self._logger.info('')
        self._logger.info('############################## Process start ##################################')
        self._logger.info('input file: \'{}\''.format(self._input_file))
        self._logger.info('output file: \'{}\''.format(self._output_file))
        self._logger.info('with kdbtime filter: {}'.format(self._with_kdbtime_filter))
        self._logger.info('#################################################################################')
        self._logger.info('')

    def _log_tailer(self):
        self._logger.info('')
        self._logger.info('############################## Process end ##################################')
        self._logger.info('')
