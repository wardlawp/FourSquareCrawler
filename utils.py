'''
@summary: Useful utilities to be shared amongst scripts
@author: Philip Wardlaw

Created on Dec 30, 2015
'''

import logging


def configureLogging(name, startTimeStamp):
    """ Configure logging to write debug, info, warning messages to file,
    and write info and warning messages to console.

    Code copied from Python docs.
    """
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s' +
                               ' %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='logs/' + name  + startTimeStamp + '.log',
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
