from heapq import *

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


def heuristic(start, end):
    # returns manhattan distance between two points
    return abs(start[0]-end[0])+abs(start[1]-end[1])

def astar(start, end, grid): #implementation with heapq

    # initialize open set for points that have yet to be checked and
    # closed set for points that have already been checked
    closedSet = set()
    openSet = []

    # dictionary to hold a node and the node it came from
    cameFrom = {}
    # dictionary to map the gScore of nodes
    gScore = {}
    # dictionary to map the fScore of nodes
    fScore = {}

    # initially map fScore and gScore of all nodes as infinity
    for i in grid.get_vertices():
        gScore[i] = float("inf")
        fScore[i] = float("inf")

    # initialize fScore and gScore of starting position
    # cost from start to start is 0 and
    # cost in beginning is just the heuristic
    gScore[start] = 0
    fScore[start] = heuristic(start,end)

    # put the starting point in the heap (priority queue)
    heappush(openSet, (start, fScore[start]))

    # keep looping as long as there is something in the open set
    while openSet:
        # current point is the first index from the top of heap
        current = heappop(openSet)[0]

        if current == end:
            # if we have reached the end of the path then return the shortest path
            return reconstruct_path(cameFrom, current)

        # add current point into closed set because we will have checked it by the end of this iteration
        closedSet.add(current)


        for neighbour in grid.neighbours(current):

            # if the neighbour is already in the closed set, don't need to to anything
            if neighbour in closedSet:
                continue

            # if the neighbour is not already in the openSet, put it into the openSet
            if neighbour not in [i[0] for i in openSet]:
                heappush(openSet,(neighbour, fScore[neighbour]))

            # calculates the distance from current position to neighbour
            # if the distance is worse than its current neighbour, move on to next neighbour
            tentative_gScore = gScore[current] + heuristic(current, neighbour)
            if tentative_gScore >= gScore[neighbour]:
                continue

            # record the best path
            cameFrom[neighbour] = current
            gScore[neighbour] = tentative_gScore
            fScore[neighbour] = gScore[neighbour] + heuristic(neighbour, end)


def reconstruct_path(cameFrom, current):
    total_path = [current]

    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)

    return total_path[::-1]


def bfs(start, end, grid):
    closedSet = set()
    openSet = Queue()

    # dictionary to hold a node and the node it came from
    cameFrom = [start]

    # put the starting point in the queue
    openSet.push((start, cameFrom))
    closedSet.add(start)

    # keep looping as long as there is something in the open set
    while not openSet.isEmpty():
        # current point is the first index from the top of heap
        current, cameFrom = openSet.pop()

        if current == end:
            # if we have reached the end of the path then return the shortest path
            return cameFrom + [current]

        for neighbour in grid.neighbours(current):

            # if the neighbour is already in the closed set, don't need to to anything
            if neighbour in closedSet:
                continue

            # add current point into closed set
            closedSet.add(neighbour)

            # put neighbour into openSet
            openSet.push((neighbour, cameFrom + [neighbour]))


# update path function
def update_path (next_point, deque):
    if len(deque) >= 2:
        # get the current point before the move
        first_pop = deque.pop()
        # get the previous point
        second_pop = deque.pop()
        # if the player backtracks (previous point == next point)
        if second_pop == next_point:
            # only append the previous point
            deque.append(second_pop)
        else:
            # add all the points back to the deque including the next point
            deque.append(second_pop)
            deque.append(first_pop)
            deque.append(next_point)
        # return the deque
        return deque
    else:
        # if the deque only has its initial point
        deque.append(next_point)
        # return the deque
        return deque


# astar update path function
def update_path_a (start_point, end_point, maze, deque):
    # get the shortest path using astar
    closest_path = astar(start_point, end_point, maze)
    # starting point is not needed
    closest_path.remove(start_point)
    # if the current path has more points than the closest path by astar,
    # load the deque with the new set of points from a_star
    if len(deque) + 1 > len(closest_path):
        # clear the existing deque
        deque.clear()
        # append the new edges
        for edge in closest_path:
            deque.append(edge)
        # return the new deque
        return deque
    # if not, update the path as usual
    else:
        # return the deque with the appended path, end_point acts as the next point
        return update_path(end_point, deque)

# bfs update path function
def update_path_bfs(start_point, end_point, maze, deque):
    # get the shortest path using bfs
    closest_path = bfs(start_point, end_point, maze)
    # starting point is not needed
    closest_path.remove(start_point)
    # if the current path has more points than the closest path by bfs,
    # load the deque with the new set of points from a_star
    if len(deque) + 1 > len(closest_path):
        # clear the existing deque
        deque.clear()
        # append the new edges
        for edge in closest_path:
            deque.append(edge)
        # return the new deque
        return deque
    # if not, update the path as usual
    else:
        # return the deque with the appended path, end_point acts as the next point
        return update_path(end_point, deque)

# break wall function
def break_wall (maze, current_point, next_point):
    # if there is no path from the current point to the next point, make one
    if not maze.is_edge((current_point, next_point)):
        maze.add_edge((current_point, next_point))
        maze.add_edge((next_point, current_point))
    # return the new maze
    return maze

