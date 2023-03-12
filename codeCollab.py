
class Tetris:

    """Assumptions:
        - <a> (+<return>): move piece left and move one row down
        - <d> (+<return>): move piece right and move one row down
        - <w> (+<return>): rotate piece counter clockwise and move one row down
        - <s> (+<return>): rotate piece clockwise and move one row down
        - <space>: no action and the piece moves one row down
        """

    def __init__(self):
        pass

    def move(self):
        while True:
                choice = input("Where you what to move :")
                Input = choice.lower()
                if Input=="a":
                    return self.left()
                elif Input == "d":
                    return self.right()
                elif Input == "w":
                    return self.anticlock_rotate()
                elif Input == "s":
                    return self.clock_rotate()
                elif Input == " ":
                    return self.do_nothing()
                
                if Input not in ["a", "d", "w", "s", " "]:
                    print("Invalid Move Please Enter make a valid Move")
                    continue

    def left(self):
            return "move piece left and move one row down"

    def right(self):
            return "move piece right and move one row down"

    def clock_rotate(self):
        return "rotate piece clockwise and move one row down"

    def anticlock_rotate(self):
        return "rotate piece counter clockwise and move one row down"

    def do_nothing(self):
        return "no action and the piece moves one row down"



print(Tetris().move())