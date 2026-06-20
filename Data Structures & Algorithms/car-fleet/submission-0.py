class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse = True)

        stack = []

        for car_pos, car_speed in cars:
            time_to_target = (target - car_pos)/car_speed

            if stack and stack[-1] >= time_to_target:
                time_to_target = stack.pop()

            stack.append(time_to_target)

        return len(stack)