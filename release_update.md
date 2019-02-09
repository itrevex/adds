# RELEASE UPDATES

## Build 1001 Release updates

### 1. Build Number

The build number tells the software which version of the program the input file was made for. This enables backward compatibility of new software versions with files made for older versions.
**Please do not tumper with the build number**

### 2. Specifying a single sectoin per span

* Two or one section(s) can be specified for a span. If the beam requires two sections for a single span, represent them as shown in the main document. If the beam only requires a single section, simply specify either of the sections, left or right or specify a section parameter as shown below.

#### For single section span

```json
        "span_x":{
                "length_m": "4.15",
                "section": "section_2",
        },
```

### 3. Stirrups / Links Input

Links represent share reinforcement in the beam. This section in the input file is dedicated to entering shear reinforcement data.
At this point, only the parameters below are required.

1. The `bar diameter` entered as `diameter`. Since no mathematics is done using this value, it is entered as a string literal (text). For example `H8` means an 8mm high strength bar.
2. The `shape code` of the bar entered as `shape_code`. Refer to `BS 8666: 2005` for standard shape codes used in detailing.
3. The `bar mark`; This is important for dimensioning, the bar bending schedule and when making the sections
4. `offset`: This is the offset of the shear reinforcement from the near edge (column edge before the shear reinforcement) of the column. Value is in `metres`. A default value of `0.05m` is used if no offset is provided. When using multiple shear link types per span. Offset is considered from the end of the previous shear_link_type
5. `spacing`: Shear reinforcement centre to centre spacing specified in `mm`.
6. `length`: Length specifies how far shear reinforcement should go. This is an **optional** parameter and if specified the offset is considered from the **left support** of the span. If this value is not specified, the offset is considered from both ends of the span. Length is input in m.

Length is import if you want to specify multiple shear reinforcement in a single span.

#### links specification sample, see sample1.trad file

```json
        "link_types": {
            "link_type_1":{
                "diameter": "R8", //bar strength and diameter
                "bar_mark": "03",
                "shape_code": 51, //BS 8666:2005
                "spacing": 200, //in mm
                "offset": 0.2, //from edge of column in m; if not provided, 0.05m is used as default
                "length": 2.36 //optional in m, important if you to specify multiple shear link types
            }
    },
```

### 4. Specifying shear links for each beam

Shear links specified inside the spans. See sample snipet below. This is extracted from sample1.trad file

```json
        "beam_x": {

                //other beam parameters

                "span_1":{
                        "length_m": "4.15",
                        "section_left": "section_2",
                        "links": ["link_type_3"] //links are specified inside square brackets to allow for multiple types input
                },
                "span_x":{
                        "length_m": "3.15",
                        "section_left": "section_2",
                        "links": ["link_type_3", "link_type_1"] //two link types specified for a single span, it would make to specify the length inside link_types to let the program where each link_type stops and where the other starts
                }

        }
```

### 5. Specifying grid number

The grid number appears on top of the centre line, if no grid numbers are provided, this value would left empty for example if you run the program with a version 1 input file.
Grid numbers are specified together with the supports, each support with its grid number. This is done inside the beams sections

In this update, beam supports data is entered inside square brackets to allow for entering of the grids labels

Look at sample1.trad file to view how this is done as demonstrated below


```json
        "beam2": {

                // ... other beam parameters

                "supports":{
                        "support_1": ["support_type_1", "2"],
                        "support_2": ["support_type_2", "3"],
                        "support_3": ["support_type_1", "4"],
                        "support_4": ["support_type_2", "5"],
                        "support_5": ["support_type_1", "6"]
                }

                //the numbers represent the grid labels and can be specified as a letter or number or anything else that is used to specify grids
        }
```