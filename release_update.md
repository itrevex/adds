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
4. `offset`: This is the offset of the shear reinforcement from the near edge (column edge before the shear reinforcement) of the column. Value is in `metres`. A default value of `0.05m` is used if no offset is provided
5. `spacing`: Shear reinforcement centre to centre spacing specified in `mm`.
6. `length`: Length specifies how far shear reinforcement should go. This is an **optional** parameter and if specified the offset is considered from the **left support** of the span. If this value is not specified, the offset is considered from both ends of the span. Length is input in m.

#### links specification sample, see sample1.trad file

```json
        "link_types": {
            "link_type_1":{
                "diameter": "R8", //bar strength and diameter
                "bar_mark": "03",
                "shape_code": 51, //BS 8666:2005
                "spacing": 200, //in mm
                "offset": 0.2, //from edge of column in m; if not provided, 0.05m is used as default
                "length": 2.36 //optional in m
            }
    },
```

### 4. Specifying shear links for each beam

Shear links specified inside the spans. See sample snipet below. This is extracted from sample1.trad file