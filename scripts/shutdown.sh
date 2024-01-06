#!/bin/bash
# 关闭服务

cd `dirname $0`/..
export BASE_DIR=`pwd`
pid=$(ps ax | grep -i 'uvicorn app.main:app' | grep -v grep | awk '{print $1}')

if [ -z "$pid" ] ; then
    echo "No my-llm-server running."
    exit -1
fi

echo "The my-llm-server (${pid}) is running..."

kill ${pid}

echo "Send shutdown request to my-llm-server (${pid}) OK"
