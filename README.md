# GPX_modifier
A (probably) one-off swing at correcting my Strava history using Python.

## Project Memory

### 1. Goal
Generate synthetic, realistic GPX files representing ~654.66 km of bike commuting to log historical distance to Strava.
Bike to assign the rides to: https://www.strava.com/bikes/9515635.

### 2. Analysis of `mess_with_the_gpx.py`
- **Initial State:** Prototype with several logic and syntax issues.
- **Fixed State:** Rewritten to use templates, handle timestamps accurately, and generate individual files.

### 3. Data File Insights
- **Templates:** 
    - `2026-03-31_2854652611_do intive.gpx` (Morning, 7.13 km)
    - `2026-03-31_2854654009_z intive.gpx` (Evening, 7.16 km)

### 4. Generation Results
- **Status:** COMPLETED
- **Total Distance:** 657.34 km
- **Total Files:** 92 (46 days of commutes)
- **Period:** July 1, 2021 to September 2, 2021 (Working days only)
- **Morning Start:** ~07:30 AM (±3 min jitter)
- **Evening Start:** ~04:15 PM (±3 min jitter)
- **Output Directory:** `generated_gpx/`

### 5. Next Steps
- Import files from `generated_gpx/` to Strava.
- Assign activities to the correct gear/bike.
