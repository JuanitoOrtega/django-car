class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'M':
                self.move_forward()

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

def main():
    upper_right = input().split()
    plateau_x = int(upper_right[0])
    plateau_y = int(upper_right[1])

    while True:
        try:
            rover_data = input().split()
            if len(rover_data) == 0:
                break

            x = int(rover_data[0])
            y = int(rover_data[1])
            direction = rover_data[2]
            instructions = input()

            rover = Rover(x, y, direction)
            rover.move(instructions)

            # Check if the rover is within the plateau boundaries
            x = max(0, min(rover.x, plateau_x))
            y = max(0, min(rover.y, plateau_y))

            print(f'{x} {y} {rover.direction}')

        except EOFError:
            break

if __name__ == "__main__":
    main()