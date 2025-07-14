import unittest
from gol import evolve

class TestGameOfLife(unittest.TestCase):
    def test_block_still_life(self):
        initial = {(0, 0), (0, 1), (1, 0), (1, 1)}
        next_gen = evolve(initial)
        self.assertEqual(next_gen, initial)

    def test_blinker_oscillator(self):
        phase1 = {(1, 0), (1, 1), (1, 2)}
        phase2 = {(0, 1), (1, 1), (2, 1)}
        self.assertEqual(evolve(phase1), phase2)
        self.assertEqual(evolve(phase2), phase1)

    def test_single_cell_dies(self):
        self.assertEqual(evolve({(0, 0)}), set())

    def test_glider_moves(self):
        g0 = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        g1 = {(1, 0), (1, 2), (2, 1), (2, 2), (3, 1)}
        g2 = {(1, 2), (2, 0), (2, 2), (3, 1), (3, 2)}
        self.assertEqual(evolve(g0), g1)
        self.assertEqual(evolve(g1), g2)

    def test_empty_input(self):
        self.assertEqual(evolve(set()), set())

if __name__ == '__main__':
    unittest.main()
    
