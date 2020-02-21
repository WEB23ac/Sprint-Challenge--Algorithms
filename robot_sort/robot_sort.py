class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out

# * start a loop which doesn't depend on any index or value
        while True:
            # * use light to control loop -- light turns on when sort is complete
            # * assume list undsorted and turn off light
            self.set_light_off()

            # * Starting at 0, try to move right after robot picks up 0th item, then move right and compare items, if held item is larger, swap it and move left and swap it again. This is moving the smaller item to the left on each move to the right
            while self.can_move_right():
                # print(f'loop instance starting item is {self._item}')
                self.swap_item()
                print(
                    f'robot can move right and has pickued up item {self._item}')
                self.move_right()

                # * now that robot is one to the right, compare held item to item at current location
                # ! Compare returns 1 if item held is greater than item at current location, returns -1 otherwise
                # * if the item robot possesses is larger, swap it with current list item
                if self.compare_item() == 1:
                    self.swap_item()
                # * assume item is not greater, so move back to the left and
                # * move back left and swap current item for it, then move back to the right and run the loop again
                self.move_left()
                self.swap_item()

                self.move_right()

        # * at the end of the list, invert actions above. Here as robot move left it's comparing the items and moving the larger items to the right this happens until the robot has an item that is *less than* an item to the left.
            while self.can_move_left():
                # * pick up the last item and move left to compare
                self.swap_item()
                print(
                    f'robot can move left and has pickued up item {self._item}')
                self.move_left()

                # * if you move left and the item in possession is smaller than the current list item, swap it and turn on light
                if self.compare_item() == -1:
                    self.swap_item()
                    self.set_light_on()
                    print(f'light on = {self.light_is_on()}')

                self.move_right()
                self.swap_item()

                self.move_left()
        # * the light is turned on at some point during the loop
            print(f'looping while light is {self.light_is_on()}')
            if self.light_is_on() is False:
                return


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
