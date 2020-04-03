#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""app.py"""

__author__ = 'Gary.Z'

import time
import click

from data_cleansing.xml_config_generator import *

logger = get_logger(__name__)


@click.command()
# @click.argument('file', nargs=1)
@click.option('--input-folder', '-i', required=True, help='Input file folder')
@click.option('--output-file', '-o', help='Output file path')
@click.option('--date-filter', '-f', is_flag=True, type=bool, help='Incremental export filter, e.g. 31/01/2020, -1d')
def main(input_folder, output_file, date_filter):
    """This script ..."""

    if not os.path.exists(input_folder):
        logger.error('input folder [{}] not exist, quit'.format(input_folder))
        exit(0)

    generator = XmlConfigGenerator(input_folder, output_file)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(e, exc_info=True)
        # logger.error(e)
    finally:
        pass
