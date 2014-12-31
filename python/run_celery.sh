#!/bin/bash

celery -A comp_match_task -c 35 worker --loglevel=info
