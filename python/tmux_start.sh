#!/bin/bash

echo Type Ctrl+B, o to switch panes
echo Type Ctrl+C to end program

DIRNAME=`dirname $0`
export TERM=ansi
tmux new-session -d -s celery "./run_celery.sh"
tmux split-window -p 33 -d "bash -i"
tmux split-window -p 50 -d "./run_flower.sh"
tmux select-pane -t 2
tmux attach-session -t celery
