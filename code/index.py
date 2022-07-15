# -*- coding: utf-8 -*-
import json
import subprocess

# To enable the initializer feature (https://help.aliyun.com/document_detail/158208.html)
# please implement the initializer function as below：
# def initializer(context):
#   logger = logging.getLogger()
#   logger.info('initializing')


def handler(event, context):
    evt = json.loads(event)
    for x in evt["payload"].split(","):
        print("执行指令 [" + x + "]")
        subprocess.call(["python", x + ".py"])
    return '执行完成'
