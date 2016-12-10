import unittest
from collections import defaultdict


_visited_coords = defaultdict(lambda: defaultdict(int))


def parse_input(input):
    return (input[0], int(input[1:]))



def polarity(direction):
    return {'north': 1, 'south': -1, 'east': 1, 'west': -1}[direction]



def _direction_to_vector(direction, distance):
    if direction in ['north', 'south']:
        return (0, (distance * polarity(direction)))
    if direction in ['east', 'west']:
        return (distance * polarity(direction), 0)



def visit_location(x, y):
    #XXX: _visited_coords should be a param.
    _visited_coords[x][y] += 1
    if _visited_coords[x][y] > 1:
        print "Visited location %s, %s more than once and is %s blocks away." % (x, y, (abs(x) + abs(y)))



def move(current_location, direction, distance):
    x1, y1 = current_location
    x2, y2 = _direction_to_vector(direction, distance)
    for distance in range(1, x2 + 1):
        visit_location(x1 + (distance * polarity(direction)), y1)
    for distance in range(1, y2 + 1):
        visit_location(x1, y1 + (distance * polarity(direction)))
    return tuple(map(sum, zip(current_location, (x2, y2))))



def compass(current, direction):
    if current == 'north':
        if direction == 'L':
            return 'west'
        elif direction == 'R':
            return 'east'

    if current == 'east':
        if direction == 'L':
            return 'north'
        elif direction == 'R':
            return 'south'

    if current == 'west':
        if direction == 'L':
            return 'south'
        elif direction == 'R':
            return 'north'

    if current == 'south':
        if direction == 'L':
            return 'east'
        elif direction == 'R':
            return 'west'
    raise ValueError('broken compass. current: %s, direction: %s' % (current, direction))



class DirectionToVectorTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual((0, 50), _direction_to_vector('north', 50))
        self.assertEqual((0, -50), _direction_to_vector('south', 50))
        self.assertEqual((25, 0), _direction_to_vector('east', 25))
        self.assertEqual((-25, 0), _direction_to_vector('west', 25))



class CompassTests(unittest.TestCase):
    def test_north_to_south(self):
        self.assertEqual('south', compass(compass('north', 'R'), 'R'))
        self.assertEqual('south', compass(compass('north', 'L'), 'L'))
        self.assertEqual('north', compass(compass('south', 'R'), 'R'))
        self.assertEqual('north', compass(compass('south', 'L'), 'L'))


    def test_east_to_west(self):
        self.assertEqual('east', compass(compass('west', 'R'), 'R'))
        self.assertEqual('east', compass(compass('west', 'L'), 'L'))
        self.assertEqual('west', compass(compass('east', 'R'), 'R'))
        self.assertEqual('west', compass(compass('east', 'L'), 'L'))


    def test_valueError(self):
        self.assertRaises(ValueError, compass, 'nodirection', 'L')
        self.assertRaises(ValueError, compass, 'north', 'B')



class ParseInputTests(unittest.TestCase):
    def test_test(self):
        self.assertEquals(('R', 1), parse_input('R1'))

    def test_significantNumbers(self):
        self.assertEquals(('R', 184), parse_input('R184'))



if __name__ == '__main__':
    inputs = ['R4', 'R3', 'R5', 'L3', 'L5', 'R2', 'L2', 'R5', 'L2', 'R5', 'R5', 'R5', 'R1', 'R3', 'L2', 'L2', 'L1', 'R5', 'L3', 'R1', 'L2', 'R1', 'L3', 'L5', 'L1', 'R3', 'L4', 'R2', 'R4', 'L3', 'L1', 'R4', 'L4', 'R3', 'L5', 'L3', 'R188', 'R4', 'L1', 'R48', 'L5', 'R4', 'R71', 'R3', 'L2', 'R188', 'L3', 'R2', 'L3', 'R3', 'L5', 'L1', 'R1', 'L2', 'L4', 'L2', 'R5', 'L3', 'R3', 'R3', 'R4', 'L3', 'L4', 'R5', 'L4', 'L4', 'R3', 'R4', 'L4', 'R1', 'L3', 'L1', 'L1', 'R4', 'R1', 'L4', 'R1', 'L1', 'L3', 'R2', 'L2', 'R2', 'L1', 'R5', 'R3', 'R4', 'L5', 'R2', 'R5', 'L5', 'R1', 'R2', 'L1', 'L3', 'R3', 'R1', 'R3', 'L4', 'R4', 'L4', 'L1', 'R1', 'L2', 'L2', 'L4', 'R1', 'L3', 'R4', 'L2', 'R3', 'L1', 'L5', 'R4', 'R5', 'R2', 'R5', 'R1', 'R5', 'R1', 'R3', 'L3', 'L2', 'L2', 'L5', 'R2', 'L2', 'R5', 'R5', 'L2', 'R3', 'L5', 'R5', 'L2', 'R4', 'R2', 'L1', 'R3', 'L5', 'R3', 'R2', 'R5', 'L1', 'R3', 'L2', 'R2', 'R1']
    direction = 'north'
    current_location = (0, 0)
    visit_location(0, 0)
    for input in inputs:
        turn, distance = parse_input(input)
        direction = compass(direction, turn)
        current_location = move(current_location, direction, distance)
    print sum(current_location)
