#!/bin/bash

celery -A tasks -c 20 worker --loglevel=info
