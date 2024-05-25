import heapq

cables = [4,3,7,10,20,6,9] 

def minimize_cables_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first_cable = heapq.heappop(cables)
        second_cable = heapq.heappop(cables)

        whole_cable = first_cable + second_cable

        total_cost += whole_cable

        heapq.heappush(cables, whole_cable)
    
    return total_cost    


print(f"Мінімальні витрати = {minimize_cables_cost(cables)}")





