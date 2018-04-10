# coding: utf-8

import sys
import pathlib


# Set vendor path
vendor_path = str(pathlib.Path('./vendor').absolute())
sys.path.append(vendor_path)

import awsgi

from apex_wsgi_sample.app import app


def lambda_handler(event, context):
    return awsgi.response(app, event, context)

