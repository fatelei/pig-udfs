# -*-coding: utf8-*-
"""
Data format converter tools.

Current support:

1. json -> csv
"""

import json

from pig_util import outputSchema

@outputSchema("line:chararray")
def json_to_csv(line):
    """Convert json format to csv format.

    Example:
        data = json.loads(line)
        values = data.values()
        values = map(unicode, values)
        return ','.join(values).encode('utf8')

    :param str line: json encoded string
    :return: A csv row.
    """
    pass
