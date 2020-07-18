#!/bin/sh

# reset the habitpi db for testing

echo "Removing the database"
rm habitpi.db
echo "Reinitializing"
python hp_sqlite_init.py
while getopts t option
do
case "${option}"
in
t)
	echo "Creating test data"
	python habitpitestentry.py
	;;
esac
done

