import re

from operator import itemgetter
from datetime import datetime

with open('input.txt') as f:
    input_data = f.read().strip()
events = input_data.split('\n')

new_events = []
for event in events:
    regex_result = re.search('\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.+)', event)
    year, month, day, hour, minute, description = regex_result.groups()
    year, month, day, hour, minute = int(year), int(month), int(day), int(hour), int(minute)
    new_events.append({'datetime': datetime(year, month, day, hour, minute), 'description': description})
events = new_events

events.sort(key=itemgetter('datetime'))

guards = {}

current_guard = None
start_range = None
end_range = None
for event in events:
    regex_result = re.search('Guard #(\d+) begins shift', event['description'])
    if regex_result:
        current_guard = regex_result.group(1)
        if current_guard not in guards:
            guards[current_guard] = {}

    regex_result = re.search('falls asleep', event['description'])
    if regex_result:
        start_range = event['datetime'].minute

    regex_result = re.search('wakes up', event['description'])
    if regex_result:
        end_range = event['datetime'].minute
        for min in range(start_range, end_range):
            if min in guards[current_guard]:
                guards[current_guard][min] += 1
            else:
                guards[current_guard][min] = 1

times_slept_data = []
for guard, data in guards.items():
    total_times_slept = 0
    for min, times_slept in data.items():
        total_times_slept += times_slept
    times_slept_data.append([guard, total_times_slept])

results = []
for guard, data in guards.items():
    for min, times_slept in data.items():
        results.append([guard, min, times_slept])
highest = max(results, key=lambda x: x[2])
print int(highest[0]) * int(highest[1])
