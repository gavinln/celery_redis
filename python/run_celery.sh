#!/bin/bash

celery -A tasks -c 2 worker --loglevel=info
