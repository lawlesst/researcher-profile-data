# research-profiles-data

Scripts to harvest research profiles from the [NIH Intramural Research Program](https://irp.nih.gov/our-research/principal-investigators).

The goal is to have real, usable researcher profile information for testing and evaluating software tools that aggregate information about scholars and their activities, such as [VIVO](http://vivoweb.org). See a slightly longer explanation in this [blog post](http://lawlesst.github.io/notebook/researcher-profile-data.html).

This code requires Python 3. Install required packages with pip, `$ pip install -r requirements`

## harvesters

* `harvest_pis.py` - harvests principal investigators and outputs JSON to terminal. Pipe to file, e.g. `$ python harvest_pis.py > people.json`.

* `harvest_divisions.py` - harvests divisions of the program and outputs JSON to terminal. Run as: `$ python harvest_divisions.py > divisions.json`.


## sample output

Each researcher profile is outputted as a JSON object:

```
    {
        "url": "https://irp.nih.gov/pi/veronica-alvarez",
        "name": "Veronica Alicia Alvarez, Ph.D.",
        "label": "Veronica Alicia Alvarez, Ph.D.",
        "first": "Veronica",
        "last": "Alvarez",
        "middle": "Alicia",
        "honors": "Ph.D.",
        "email": "xxx@mail.nih.gov",
        "title": "Senior Investigator",
        "position_title": "Senior Investigator",
        "photo": "https://irp.nih.gov/sites/default/files/pi/0013626077.jpg",
        "bio": "Dr. Alvarez earned a Ph.D. degree in Neuroscience in 1997 from University of Buenos Aires, Argentina. She trained as a postdoctoral fellow with Dr. John Williams at the Vollum Institute, OHSU from 1998 to 2001 studying the firing properties of locus coerulues neurons and its modulation by opioids. She then trained with Dr. Bernardo Sabatini at Harvard Medical School from 2001-2007 where she studied mechanisms of functional and morphological plasticity at glutamatergic synapses using electrophysiology and two-photon imaging. In 2008, she established an independent research program at NIAAA where she is investigator and acting chief of the Section on Neuronal Structure.",
        "research_interests": [],
        "pmids": [
            "25547712",
            "21743470",
            "21289199",
            "26080439"
        ],
        "website": "http://youtu.be/N9aFVrLVa7A"
    }
```
