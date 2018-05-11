# research-profiles-data

Scripts to harvest research profiles from the [NIH Intramural Research Program](https://irp.nih.gov/our-research/principal-investigators).

The goal is to have real, usable researcher profile information that can be used for testing software tools that aggregate information about scholars and researchers, such as [VIVO](http://vivoweb.org).

This code is written for Python 3.

## harvesters

* `harvest_pis.py` - harvests prinicipal investigators and outputs JSON to terminal. Pipe to file, e.g. $ python harvest_pis.py > people.json.

* `harvest_divisions.py` - harvests divisions of the program and outputs JSON to terminal. Run as: `$ python harvest_divisions.pyt > people.json`.
