def paid_stairs(costs, step):
 	if len(costs) < step:
 	    return costs[-1]
 	else:
 		for i, v in enumerate(costs):
 			if i < step:
 				continue
 			else:
 				p = min(costs[i-step:i])
 				costs[i] += p
 	return costs[-1]

step = int(input())
print(paid_stairs(costs=costs, step=step))

