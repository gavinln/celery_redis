#!/bin/bash

celery flower -A tasks --address=0.0.0.0 --broker=redis://localhost:6379/0
