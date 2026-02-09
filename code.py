import sys

def main():
    class BessieTracker:
        def __init__(self, s):
            self.s = list(s)
            self.n = len(self.s)
            self.completions = self.compute_initial_completions()
            self.start_s_list = [c[0] for c in self.completions]
            self.end_e_list = [c[1] for c in self.completions]
            self.total = self.compute_total()

        def compute_initial_completions(self):
            m = 6
            target = ['b', 'e', 's', 's', 'i', 'e']
