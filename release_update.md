# RELEASE UPDATES

**Release Date:** Saturday 02 March, 2019

*Catch possible mistakes while inputing data

## 1002. Build 1002 Release updates

**Release Date:** Monday 18 February, 2019

This update changes the program entirely and there is no support for input files created using earlier versions.
1. 
Each part of the input file starts with the `PART` name and ends with `END PART`. Values that have to be changed are indicated in _italics_. The commands that tell the program what to do have been `highlighted`.  The order of how these parts are added to the input file does not matter.

`COMMAND` _value1_ _value2_. Items are separated using spaces. The case of the commands and values is ignored, commands are only entered as upper case for clarity.

_X_ means the parameter is not applicable

A line starting with an asterisk (`*`) is ignored. This is to all addition of **comments** to the input file

### 1002.1 Input File

### 1002.1.1. Build Number

The build number tells program what version of the program we are working with;

`BUILD` _build_number_  

Example  

`BUILD` _1002_  

### 1002.1.2. Start Point

Start point is where the drawing the beam starts. The `x, y, z` coordinates are provided in that order as shown below

`START POINT` _x_ _y_ _z_

Example

`START POINT` _0_ _0_ _0_

### 1002.1.2. Beam Sections

The sections commands are used in specifying the beam(s) sections as illustrated below  

`SECTIONS`  
`SECTION` _section_1_name_ _bw_ _d_ _bf_top_ _df_ _w_offset_  
`SECTION` _section_2_name_ _bw_ _d_ _bf_top_ _df_ _w_offset_  
`END SECTIONS`  

Example

`SECTIONS`  
`SECTION` _1_ _200_ _450_ _500_ _150_ _150_  
`SECTION` _2_ _250_ _450_ _350_ _250_ _X_  
`SECTION` _3_ _200_ _450_ _350_ _200_ _150_  
`SECTION` _4_ _300_ _800_  
`END SECTIONS`  

In this example, section _4_ is a square section. The inapplicable parameters could have also been passed as _X_'s but not passing them at all works the same.
Refer to _read_me.pdf_ for explanation of the parameters used after the commands

### 1002.1.3. Beam Links (Shear reinforcement)

The section specifies shear reinforcement to be added to the different beams within the input

To add Links to your input, follow the format below

`LINKS`  
`LINK` _link_1_name_ _diameter_ _bar_mark_ _shape_code_ _spacing_ _offset_ _length_  
`LINK` _link_2_name_ _diameter_ _bar_mark_ _shape_code_ _spacing_ _offset_ _length_  
`END LINKS`  

**Note:** Refer to shear/links section of _Build 1001 Release update_ notes for explanation of the parameters. These will be better explained when the docs are combined.

Example

`LINKS`  
`LINK` _1_ _T8_ _03_ _51_ _200_ _0.05_ _X_  
`LINK` _2_ _T8_ _03_ _51_ _200_ _0.05_ _X_  
`LINK` _3_ _T8_ _03_ _51_ _150_ _X_ _1.3_  
`END LINKS`  

### 1002.1.4. Beam Supports

Beam supports are basically to guide program on the type of columns at each point. Below is an illustration of how to input supports data.

`SUPPORTS`  
`SUPPORT` _support_1_name_ `TOP` _section_d_ _section_b_ _column_h_m_ `BOTTOM` _section_d_ _section_b_ _column_h_m_  
`SUPPORT` _support_2_name_ `TOP` _section_d_ _section_b_ _column_h_m_ `BOTTOM` _section_d_ _section_b_ _column_h_m_  
`SUPPORT` _support_3_name_ `TOP` _section_d_ _section_b_ _column_h_m_  
`SUPPORT` _support_4_name_ `BOTTOM` _section_d_ _section_b_ _column_h_m_  
`END SUPPORTS`  

**Note:** Not specifying either `TOP` or `BOTTOM` commands means support does not have columns that are not specified. In example below, support _2_ has no top column and support _3_ has no bottom column

Example

`SUPPORTS`  
`SUPPORT` _1_ `TOP` _200_ _200_ _3_ `BOTTOM` _200_ _200_ _3_  
`SUPPORT` _2_ `TOP` _200_ _300_ _3_  
`SUPPORT` _3_ `BOTTOM` _200_ _300_ _3_  
`END SUPPORTS`  

**Note:** Refer to _read_me.pdf_ for an explanation of the parameters. The explanation will be added directly to this section when the documentation is unified.

### 1002.1.5. Beams

This is section is used to specify beams using the parameters that have been explained above (or rather added to the input file).
Below is how beams should be specified.

`BEAMS`  
`BEAM` _name_ _beam_depth_  
`SPAN` _span_name_ _length_m_ _section_ _link_1_name_ _link_2_name_ _. . ._  
`SUPPORT` _name_ _beam_support_name_ _grid_label_  
`END BEAM`  
`END BEAMS`

**Note:** As many as possible link types can be added to the end the span. "But not so many that would otherwise abuse the program."

Example

`BEAMS`  
`BEAM` _1_ _450_  
`SPAN` _1_ _4.15_ _2_ _1_  
`SPAN` _2_ _3_ _4_ _1_  
`SPAN` _3_ _3.2_ _1_ _2_  
`SPAN` _4_ _2_ _3_ _3_  
`SUPPORT` _1_ _2_ _2_  
`SUPPORT` _2_ _1_ _3_  
`SUPPORT` _3_ _1_ _4_  
`SUPPORT` _4_ _3_ _5_  
`SUPPORT` _5_ _2_ _6_  
`END BEAM`  
`BEAM` _2_ _600_  
`SPAN` _1_ _4.15_ _2_ _1_ _2_ _3_  
`SPAN` _2_ _3_ _4_ _1_  
`SPAN` _3_ _3.2_ _1_ _2_  
`SPAN` _4_ _2_ _3_ _3_  
`SUPPORT` _1_ _1_ _2_  
`SUPPORT` _2_ _3_ _3_  
`SUPPORT` _3_ _1_ _4_  
`SUPPORT` _4_ _2_ _5_  
`SUPPORT` _5_ _1_ _6_  
`END BEAM`  
`END BEAMS`  

Beam _2_ span _1_ has multiple (3) shear link types specified for it

See _sample1.trad_ file for a fully working example. All the examples used in the explanations have been picked from that very sample file

## Build 1001 Release updates

**Release Date:** Monday 11 February, 2019

### 1. Build Number

The build number tells the software which version of the program the input file was made for. This enables backward compatibility of new software versions with files made for older versions.
**Please do not tamper with the build number unless you are sure of what you are doing**

### 2. Specifying a single section per span

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

#### Multiple Links Per Span Specification

* If no length is provided in the case of multiple links, the span length is shared equally among the multiple links
* If one of many links with no lengths has a length specified, its length will be maintained and rest of the span length shared among the remaining link types
* Multiple links are added to the span in the order they are specified in a a particular span inside the beam data. For example `links: ["link_type_2", "link_type_1", "link_type_2"]"]` would add type2 links to spans then type1 and finally type2

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