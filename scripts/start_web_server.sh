#!/usr/bin/env bash
cd /home/zhaojingming/apps/log_analysis/analysis/result/
nohup pypy -m SimpleHTTPServer 8080 analysis/result/ &