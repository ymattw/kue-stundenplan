ACTIVATE := .env/bin/activate
LATEST := $(shell /bin/ls -1 -tr 20*.py | tail -1)

latest: dep
	source $(ACTIVATE) && python $(LATEST)

dep:
	[ -f $(ACTIVATE) ] || python3 -m venv .env
	ls -d .env/lib/python*/site-packages/icalendar || { source $(ACTIVATE) && pip install -r requirements.txt; }

