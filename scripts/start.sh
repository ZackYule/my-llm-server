#!/bin/bash
#后台运行Chat_on_webchat执行脚本

cd `dirname $0`/..
export BASE_DIR=`pwd`
echo $BASE_DIR

nohup pipenv run uvicorn app.main:app --reload --timeout-keep-alive 60 --port 8080 & tail -f "${BASE_DIR}/nohup.out"

echo "my-llm-server is starting，you can check the ${BASE_DIR}/nohup.out"
