"""Simulate a computer assembly line."""
from random import random

class AssemblyLine:

    def __init__(self):
        self.line_running = False

    def check_success(self):
        """Randomly decide if a step was successful."""
        if random() < 0.99:
            return True
        return False

    def add_hard_drive(self):
        if self.check_success():
            print("  Added hard drive.")
        else:
            print("  Failed to add hard drive.")
            self.line_running = False

    def add_ram(self):
        if self.check_success():
            print("  Added RAM.")
        else:
            print("  Failed to add RAM.")
            self.line_running = False

    def add_gpu(self):
        if self.check_success():
            print("  Added GPU.")
        else:
            print("  Failed to add GPU.")
            self.line_running = False

    def start_line(self):
        """Start the line, and keep building
        until something fails.
        """
        self.line_running = True
        num_started = 0
        while self.line_running:
            num_started += 1
            print(f"Building computer number {num_started}:")

            self.add_hard_drive()
            self.add_ram()
            self.add_gpu()

        # If the loop ended, the line must have stopped.
        print("\nThe line has stopped due to a failure.")
        print(f"Built {num_started-1} computers.")

assembly_line = AssemblyLine()
assembly_line.start_line()