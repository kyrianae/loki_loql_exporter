#!/bin/bash

while true; do sleep 1;  echo id1 $RANDOM >> $log_file ; echo id2 $RANDOM >> $log_file ; done

