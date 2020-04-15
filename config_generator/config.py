#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""config.py"""

__author__ = 'Gary.Z'

from config_generator.logging import *
#
# EXCEL_INDEX_BASE = 1
# HEADER_ROW_INDEX = 0 + EXCEL_INDEX_BASE
#
# BASE_INFO_COLS_MIN = 23
#
# MAJOR_FILTER_LIST = ('测试专业',)
# NC_OPTION_FILTER_LIST = ('无法评价', '以上均不需要改进')
# G1_OPTION_FILTER_LIST = ('国际组织', '军队')
# SALARY_FILTER_LOWER_LIMIT = 1000
# SALARY_FILTER_HIGHER_LIMIT = 50000
# SALARY_FILTER_TOP_RATIO = 0.003
#
# RINSE_RULE_KEY_QUESTION = 'question_id'
# RINSE_RULE_KEY_ANSWER = 'answer'
# RINSE_RULE_KEY_OPERATOR = 'operator'
# RINSE_RULE_KEY_ACTION = 'rinse_ids'
# RINSE_RULE_OPERATOR_IN = 'IN'
# RINSE_RULE_OPERATOR_NOTIN = 'NOT_IN'
# # definition of irrelevant question rinse rule
# RINSE_RULE_IRRELEVANT_QUESTIONS = [
#     # IF A2 not in (在国内工作, 自由职业) then rinse
#     #   B1, B2, B3, B4, B5, B6, B7-1, B7-2, B7-3, B7-4, B8, B9-1, B9-2, B10-1, B10-2, D1, D2
#     {RINSE_RULE_KEY_QUESTION: 'A2',
#      RINSE_RULE_KEY_ANSWER: ('在国内工作', '自由职业'),
#      RINSE_RULE_KEY_OPERATOR: RINSE_RULE_OPERATOR_NOTIN,
#      RINSE_RULE_KEY_ACTION: ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7-1', 'B7-2', 'B7-3', 'B7-4', 'B8',
#                   'B9-1', 'B9-2', 'B10-1', 'B10-2', 'D1', 'D2']},
#     # IF A2 = 自由职业 then rinse B1,B2,B3,B4, B10-1
#     {RINSE_RULE_KEY_QUESTION: 'A2',
#      RINSE_RULE_KEY_ANSWER: ('自由职业',),
#      RINSE_RULE_KEY_OPERATOR: RINSE_RULE_OPERATOR_IN,
#      RINSE_RULE_KEY_ACTION: ['B1', 'B2', 'B3', 'B4', 'B10-1', 'B10-2']},
#     # IF B9-1 not in (比较不相关, 很不相关) then rinse B9-2
#     {RINSE_RULE_KEY_QUESTION: 'B9-1',
#      RINSE_RULE_KEY_ANSWER: ('比较不相关', '很不相关'),
#      RINSE_RULE_KEY_OPERATOR: RINSE_RULE_OPERATOR_NOTIN,
#      RINSE_RULE_KEY_ACTION: ['B9-2']},
# ]
#
# RINSE_RULE_IRRELEVANT_QUESTIONS_V6_COMPATIBLE = [
#     {RINSE_RULE_KEY_QUESTION: 'A2',
#      RINSE_RULE_KEY_ANSWER: ('自由职业',),
#      RINSE_RULE_KEY_OPERATOR: RINSE_RULE_OPERATOR_IN,
#      RINSE_RULE_KEY_ACTION: ['B5', 'B6', 'B7-1', 'B7-2', 'B7-3', 'B7-4', 'B8', 'B9-1', 'B9-2']},
# ]



