import unittest
from gol import parse_life, evolve

class TestParseLife(unittest.TestCase):
    def test_parse(self):
        lines = ['#Life 1.06', '1 2', '-3 4']
        self.assertEqual(parse_life(lines), {(1, 2), (-3, 4)})

class TestEvolve(unittest.TestCase):
    def test_blinker_oscillator(self):
        first = {(0, 0), (1, 0), (2, 0)}
        second = evolve(first)
        self.assertEqual(second, {(1, -1), (1, 0), (1, 1)})
        self.assertEqual(evolve(second), first)

    def test_glider_translation(self):
        initial = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}
        live = initial
        for _ in range(4):
            live = evolve(live)
        expected = {(x + 1, y + 1) for x, y in initial}
        self.assertEqual(live, expected)

if __name__ == '__main__':
    unittest.main()
