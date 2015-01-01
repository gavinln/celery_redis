#!/bin/bash

celery -A tasks -c 5 worker --loglevel=info
