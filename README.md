# Information-based Distance Limited Exploration (IDLE) heuristic

A novel heuristics function for evaluating and selecting intermediate points in an autonomous exploration and mapping system where navigation is performed by a learned neural network. The heuristics function calculates the fitness score of each given point in a partially observed map. The function calculation takes into consideration the training setting of a deep reinforcement learning-based network and combines it with distance information towards the global goal and the map information. The point with the minimum score is assumed to be the best solution.

The paper is available at:
https://ieeexplore.ieee.org/abstract/document/9494668

**Resulting score surfaces in a partially known map:**

Goal: [15, 0]  Origin: [0, 0]
<p align="left">
    <img width=50% src="https://github.com/reiniscimurs/IDLE-heuristic/blob/main/IDLE_score.png">
</p>

Goal: [10, -5]  Origin: [-5, 2]
<p align="left">
    <img width=50% src="https://github.com/reiniscimurs/IDLE-heuristic/blob/main/IDLE_score2.png">
</p>

Goal: [20, 10]  Origin: [-10, -10]
<p align="left">
    <img width=50% src="https://github.com/reiniscimurs/IDLE-heuristic/blob/main/IDLE_score3.png">
</p>
