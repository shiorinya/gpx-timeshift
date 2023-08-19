from datetime import timedelta, datetime
import re
import sys
import gpxpy
import gpxpy.gpx


def parse_time(time_str):
    regex = re.compile(
        r"((?P<days>\d+?)d)?((?P<hours>\d+?)[h])?((?P<minutes>\d+?)m)?((?P<seconds>\d+?)s)?"
    )
    parts: regex.Match = regex.match(time_str)
    if parts.span() == (0, 0):
        raise ValueError(f"Invalid time: {time_str}")
    parts = parts.groupdict()
    time_params = {}
    for name, param in parts.items():
        if param:
            time_params[name] = int(param)
    return timedelta(**time_params)


def rename_with_time_delta(name, time_delta):
    patterns = {
        "GPS Logger": (r"(\d{8}-\d{6})", "%Y%m%d-%H%M%S"),
        "OSM Track": (r"(\d+-){2}\d+_(\d+-){2}\d+", "%Y-%m-%d_%H-%M-%S"),
    }
    for pattern, time_format in patterns.values():
        match = re.search(pattern, name)
        if match:
            time_part = match.group()
            shifted_time = datetime.strptime(time_part, time_format) + time_delta
            new_name = name.replace(
                time_part, datetime.strftime(shifted_time, time_format)
            )
            return new_name
    return name


help = """Usage: python gpx.py filename (-)[DAYS]d[HOURS]h[MINUTES]m[SECONDS]s
python gpx.py 20230801-102355.gpx 1d1h2m1s
python gpx.py 20230801-102355.gpx -2h
"""

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print(help)
        exit(1)
    filename = args[1]
    time_str = args[2]

    with open(filename, "r") as f:
        gpx = gpxpy.parse(f)

    if time_str.startswith("-"):
        time_delta = parse_time(time_str[1:])
        time_delta = -time_delta
    else:
        time_delta = parse_time(time_str)

    if gpx.time:
        gpx.time += time_delta

    gpx.name = rename_with_time_delta(gpx.name, time_delta)

    for track in gpx.tracks:
        track.name = rename_with_time_delta(track.name, time_delta)
        track.adjust_time(time_delta)

    with open("shifted-" + gpx.name + ".gpx", "w") as f:
        f.write(gpx.to_xml())
