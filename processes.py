"""
In this task you have to code process planner.

You will be given initial thing, target thing and a set of processes to turn one thing into another
(in the form of [process_name, start_thing, end_thing]).
You must return names of shortest sequence of processes to turn initial thing into target thing,
or empty sequence if it's impossible.

If start already equals end, return [], since no path is required.

Example:

test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
];

processes('field', 'bread', test_processes) # should return ['gather', 'mill', 'bake']
processes('field', 'ferrari', test_processes) # should return []
processes('field', 'field', test_processes) # should return [], since no processes are needed
"""


def processes(start, end, processes_table):
    start_end_dict = {}
    process_name_dict = {}

    for process in processes_table:
        start_end_dict[process[1]] = process[2]
        process_name_dict[process[1]] = process[0]

    results = []
    current_start = start
    while True:
        if current_start not in start_end_dict:
            return []

        results.append(process_name_dict[current_start])

        end_thing = start_end_dict[current_start]
        if end_thing == end:
            break

        current_start = start_end_dict[current_start]

    return results

from unittest import TestCase


class TestProcesses(TestCase):
    def test_processes(self):
        test_processes = [
            ['gather', 'field', 'wheat'],
            ['bake', 'flour', 'bread'],
            ['mill', 'wheat', 'flour']
        ]
        
        self.assertEquals(
            processes('field', 'bread', test_processes), ['gather', 'mill', 'bake'])
        self.assertEquals(
            processes('field', 'ferrari', test_processes), [])
        self.assertEquals(
            processes('field', 'field', test_processes), [])