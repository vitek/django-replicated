#!/bin/sh

PYTHONPATH=$PWD python ./test_replicated/manage.py test $*
