# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_names(targets):
    for key in targets:
        print(key)
print_names(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_names_and_spectral_type(targets):
    for star_name in targets:
        spectral_type = targets[star_name]["Spectral Type"]
        print(f"{star_name}: {spectral_type}")

print_names_and_spectral_type(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_magnitude(targets):
    greater_magnitude = []
    for star_name, star_data in targets.items():
        if star_data ["Magnitude"] > 0.1:
            greater_magnitude.append(star_name)
    print(greater_magnitude)
find_magnitude(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Alpha Centuari"] = {
    "RA" : "14h 39m 36.5s",
    "Dec" : "-60° 50′ 02″",
    "Magnitude" : -0.27,
    "Spectral Type" : "G2V"
}
print(targets)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def find_brightest_star_closest_to_declination(targets, target_declination=20.0):
    closest_star = None
    min_declination_diff = float('inf')
    min_magnitude = float('inf')

    for star_name, star_data in targets.items():
        try:
            # Parse magnitude
            magnitude = float(star_data["Magnitude"])

            # Parse declination (assumes "Dec" like "20° 30'" or "20")
            dec_str = star_data["Dec"].split()[0]
            dec_clean = dec_str.replace('°', '').replace("'", '').replace('"', '')
            dec_degrees = float(dec_clean)

            # Calculate how close the declination is to 20°
            declination_diff = abs(dec_degrees - target_declination)

            # Priority: closest to 20°, then brightest
            if (declination_diff < min_declination_diff) or (
                declination_diff == min_declination_diff and magnitude < min_magnitude):
                min_declination_diff = declination_diff
                min_magnitude = magnitude
                closest_star = star_name

        except (ValueError, KeyError) as e:
            # Skip malformed entries
            continue

    return closest_star

print(find_brightest_star_closest_to_declination(targets))

# 6) What is your favorite constellation?
# My favorite constellation is Ursa Minor because I think the small bear is cute!


