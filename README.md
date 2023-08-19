# GPX TimeShift

GPX TimeShift is a Python script that allows you to modify the timestamps in GPX (GPS Exchange Format) files. It provides a simple way to shift the time values in the GPX file, either forward or backward, by a specified duration.

## Motivation

The purpose of this script is to provide a convenient tool for users who want to obfuscate or modify the timestamp information in their GPX files. This can be useful when submitting GPS data to OSM (OpenStreetMap) may be considered illegal mapping in certain regions, such as China, or privacy concerns.

## Installation

1. Clone the repository or download the `gpx-timeshift.py` script.
2. Install the required dependencies by running the following command:
```
pip install gpxpy
or
pip install -r requirements.txt
```

## Usage

python gpx.py filename (-)[DAYS]d[HOURS]h[MINUTES]m[SECONDS]s
- `filename`: The name of the GPX file to be modified.
- `(-)[DAYS]d[HOURS]h[MINUTES]m[SECONDS]s`: The duration by which the timestamps should be shifted. Use a negative sign (-) to shift the timestamps backward.

### Examples

Shift the timestamps in `20230801-102355.gpx` file by 1 day, 1 hour, 2 minutes, and 1 second:
```
python gpx.py 20230801-102355.gpx 1d1h2m1s
```
Shift the timestamps in `20230801-102355.gpx` file by 2 hours backward:
```
python gpx.py 20230801-102355.gpx -2h
```
