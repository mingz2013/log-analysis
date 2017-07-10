#!/usr/bin/env bash

last_day=`date +"%Y_%m_%d" --date='1 days ago'`
echo "========================$last_day=====begin=========================="
cd /home/zhaojingming/apps/log_analysis/
find /home/log37/10.* -name GT712*$last_day | xargs grep '===analysis===' | awk -F '===analysis===' '{print $2}' > tmp/tmp_$last_day.json
find /home/log37/10.* -name GT711*$last_day | xargs grep '===analysis===' | awk -F '===analysis===' '{print $2}' >> tmp/tmp_$last_day.json
pypy src/analysis/setup.py
echo "========================$last_day=====end============================"