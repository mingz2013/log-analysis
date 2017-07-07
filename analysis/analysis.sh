#!/usr/bin/env bash


cd /home/zhaojingming/apps/log_analysis/analysis/
find /home/log37/10.* -name GT712*`date +"%Y_%m_%d" --date='1 days ago'` | xargs grep '===analysis===' | awk -F '===analysis===' '{print $2}' > tmp/tmp_`date +"%Y_%m_%d" --date='1 days ago'`.json
pypy src/analysis.py
