from typing import List

max_1 = 0


def run(ll):
    for params in ll:
        print(solve(params[0], params[1], params[2]))


def solve(claw_pos: int, boxes: List[int], box_in_claw: bool) -> str:
    """
    You work in an automated factory. The factory uses a simple robotic arm to move boxes around.
    The arm is capable of picking a box from a stack, and placing it on another stack.

    @type claw_pos: int - the index of the stack the arm is currently above
    @type boxes: List[int] - an array of integers for the size of each stack
    @type box_in_claw: bool - true if the arm is carrying a box, false otherwise
    @rtype: String - com
    """
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    global max_1
    if max_1 > 200:
        return -1

    l_boxex = len(boxes)
    sum_boxes = sum(boxes)
    avg_boxes = round(sum_boxes / l_boxex)

    for idx, box in enumerate(boxes):
        if idx == claw_pos:
            if box > avg_boxes:
                if not box_in_claw:
                    return 'PICK'
                else:
                    left_boxes = [box for box in boxes[0:idx] if box < avg_boxes]
                    direction = 'LEFT' if len(left_boxes) > 0 else 'RIGHT'
                    return direction
            elif box < avg_boxes:
                if box_in_claw:
                    return 'PLACE'
                else:
                    left_boxes = [box for box in boxes[0:idx] if box < avg_boxes]
                    direction = 'LEFT' if len(left_boxes) > 0 else 'RIGHT'
                    return direction
            elif box == avg_boxes:
                left_boxes = [box for box in boxes[0:idx] if box < avg_boxes]
                direction = 'LEFT' if len(left_boxes) > 0 else 'RIGHT'
                return direction

    max_1 += 1
    return box_in_claw


if __name__ == '__main__':
    ll = [
        [0, [1, 0, 3, 0, 0, 1, 2], False],  # RIGHT
        [1, [1, 0, 3, 0, 0, 1, 2], False],  # RIGHT
        [2, [1, 0, 3, 0, 0, 1, 2], False],  # PICK
        [2, [1, 0, 2, 0, 0, 1, 2], True],  # LEFT
        [1, [1, 0, 2, 0, 0, 1, 2], True],  # PLACE
        [1, [1, 1, 2, 0, 0, 1, 2], False],  # RIGHT
        [2, [1, 1, 2, 0, 0, 1, 2], False],  # PICK
        [2, [1, 1, 1, 0, 0, 1, 2], True],  # RIGHT
        [3, [1, 1, 1, 0, 0, 1, 2], True],  # PLACE
        [3, [1, 1, 1, 0, 0, 1, 2], True],  # PLACE
        [5, [1, 1, 1, 1, 0, 1, 2], False],  # LEFT
        [4, [1, 1, 1, 1, 0, 1, 2], False],  # RIGHT
        [5, [1, 1, 1, 1, 0, 1, 2], False],  # RIGHT
        # [0, [3, 1, 2, 2], False], # PICK
        # [0, [2, 1, 2, 2], True],  # RIGHT
        # [1, [2, 1, 2, 2], True],  # PLACE
        # [2, [2, 1, 2, 2], True],  # LEFT
        # [3, [2, 1, 2, 2], True]   # LEFT
    ]
    run(ll)
