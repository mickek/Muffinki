#!/bin/sh

date >> logfile

echo "git pull" >> logfile
git pull

echo "git reset --hard" >> logfile
git reset --hard

echo "git push" >> logfile
git push

echo "***" >> logfile
