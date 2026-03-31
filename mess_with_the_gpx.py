import os
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import random

# Configuration
MORNING_TEMPLATE = '2026-03-31_2854652611_do intive.gpx'
EVENING_TEMPLATE = '2026-03-31_2854654009_z intive.gpx'
OUTPUT_DIR = 'generated_gpx'
TARGET_DISTANCE = 654.66
MORNING_START_TIME = "07:30:00"
EVENING_START_TIME = "16:15:00"
JITTER_MINUTES = 3

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

ET.register_namespace('', "http://www.topografix.com/GPX/1/1")

def get_template_data(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}
    trkpts = root.findall('.//gpx:trkpt', ns)
    
    # Get initial time to calculate offsets
    first_time_str = trkpts[0].find('gpx:time', ns).text
    # Handle both Z and +00:00 formats
    first_time_str = first_time_str.replace('Z', '+00:00')
    first_time = datetime.fromisoformat(first_time_str)
    
    offsets = []
    for pt in trkpts:
        t_str = pt.find('gpx:time', ns).text.replace('Z', '+00:00')
        t = datetime.fromisoformat(t_str)
        offsets.append(t - first_time)
        
    return tree, offsets

def generate_gpx(tree, offsets, start_datetime, output_path):
    root = tree.getroot()
    ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}
    trkpts = root.findall('.//gpx:trkpt', ns)
    
    for pt, offset in zip(trkpts, offsets):
        new_time = start_datetime + offset
        time_tag = pt.find('gpx:time', ns)
        time_tag.text = new_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        
    # Also update metadata time if exists
    metadata_time = root.find('.//gpx:metadata/gpx:time', ns)
    if metadata_time is not None:
        metadata_time.text = start_datetime.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        
    tree.write(output_path, encoding='UTF-8', xml_declaration=True)

# Main generation loop
current_date = datetime(2021, 7, 1)
total_dist = 0.0
morning_tree, morning_offsets = get_template_data(MORNING_TEMPLATE)
evening_tree, evening_offsets = get_template_data(EVENING_TEMPLATE)

# Distances from previous calculation
MORNING_DIST = 7.13
EVENING_DIST = 7.16

generated_files = 0

while total_dist < TARGET_DISTANCE:
    # Check if working day (Mon-Fri)
    if current_date.weekday() < 5:
        # Morning ride
        jitter = random.randint(-JITTER_MINUTES * 60, JITTER_MINUTES * 60)
        h, m, s = map(int, MORNING_START_TIME.split(':'))
        start_morning = current_date.replace(hour=h, minute=m, second=s) + timedelta(seconds=jitter)
        
        morning_filename = f"{start_morning.strftime('%Y-%m-%d')}_morning_commute.gpx"
        generate_gpx(morning_tree, morning_offsets, start_morning, os.path.join(OUTPUT_DIR, morning_filename))
        total_dist += MORNING_DIST
        generated_files += 1
        
        # Evening ride
        jitter = random.randint(-JITTER_MINUTES * 60, JITTER_MINUTES * 60)
        h, m, s = map(int, EVENING_START_TIME.split(':'))
        start_evening = current_date.replace(hour=h, minute=m, second=s) + timedelta(seconds=jitter)
        
        evening_filename = f"{start_evening.strftime('%Y-%m-%d')}_evening_commute.gpx"
        generate_gpx(evening_tree, evening_offsets, start_evening, os.path.join(OUTPUT_DIR, evening_filename))
        total_dist += EVENING_DIST
        generated_files += 1
        
    current_date += timedelta(days=1)

print(f"Generated {generated_files} files.")
print(f"Total distance: {total_dist:.2f} km")
