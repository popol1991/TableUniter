# TableUniter

## Introduction

TableUniter project has two components:
1. Identify as many as possible units of measurements from the Web and store them structurely for machine processing;
2. Given a table in XML format, recognize the unit of each cell in it;

## Example

Given a table as shown below, the ultimate goal of this project is, with the help of other contextual information of the table of
course, to recognize that the unit of the first column is millimeter, second kilo-electronvolt, third Kelvin, and forth constant.

| Distance (mm) | kT (keV) | T (K) | μ   |
| ------------- | -------- | ----- | --- |
| 5             | 0.04     | 100   | 0.1 |
| 10            | 0.05     | 200   | 0.4 |
| 15            | 0.05     | 300   | 0.7 |

Although sometimes people put combinatoin of units in tables, GeV^2/cm^-5 for a crazy example, in this version we only focus
on individual well defined units.
