# Information-based Distance Limited Exploration (IDLE) heuristic

A novel heuristics function for evaluating and selecting intermediate points in an autonomous exploration and mapping system where navigation is performed by a learned neural network. The heuristics function calculates the fitness score of each given point in a partially observed map. The function calculation takes into consideration the training setting of a deep reinforcement learning-based network and combines it with distance information towards the global goal and the map information. The point with the minimum score is assumed to be the best solution.

**Resulting score surface in a partially known map:**

Goal: [15, 0]

Origin: [0, 0]
<p align="left">
    <img width=60% src="https://github.com/reiniscimurs/IDLE-heuristic/blob/main/IDLE_score.png">
</p>
