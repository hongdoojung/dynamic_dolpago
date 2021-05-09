# 뒤에서부터 dp로 계산. probability maximize.

MAX_PENALTY = 5
GAP_PER_MOVE = 10

def get_probability(targets, remains, probability, dp):
    print(targets, remains, probability)
    # probability = round(probability,2)
    if probability > 0.75:
        probability = 0.75
    if probability < 0.25:
        probability = 0.25
    
    if dp[probability].get(str([targets, remains])):
        result = dp[probability].get(str([targets, remains]))
  
    elif targets[0] <= 0 and targets[1] <= 0 and targets[2] >= 0:
        result = 1
    elif targets[2] < 0:
        result = 0
    elif targets[0] > remains[0] or targets[1] > remains[1]:
        result = 0
    elif remains == [0,0,0]:
        result = 0
    else:
        choice1 = (
            probability * get_probability([targets[0]-1, targets[1], targets[2]], [remains[0]-1, remains[1], remains[2]], probability-0.1, dp)[0]
            + (1-probability) * get_probability([targets[0], targets[1], targets[2]], [remains[0]-1, remains[1], remains[2]], probability+0.1, dp)[0]
            if remains[0] > 0 else -1
        )
        choice2 = (
            probability * get_probability([targets[0], targets[1]-1, targets[2]], [remains[0], remains[1]-1, remains[2]], probability-0.1, dp)[0]
            + (1-probability) * get_probability([targets[0], targets[1], targets[2]], [remains[0], remains[1]-1, remains[2]], probability+0.1, dp)[0]
            if remains[1] > 0 else -1
        ) 
        choice3 = (
            probability * get_probability([targets[0], targets[1], targets[2]-1], [remains[0], remains[1], remains[2]-1], probability-0.1, dp)[0]
            + (1-probability) * get_probability([targets[0], targets[1], targets[2]], [remains[0], remains[1], remains[2]-1], probability+0.1, dp)[0]
            if remains[2] > 0 else -1
        )
        result = max(choice1, choice2, choice3)
    dp[probability].update({str([targets, remains]):result})
    
    return result if result > 0 else 0, dp

def get_next_move(targets, remains, probability):
    probabilities = []
    for i in range(3):
        i_probability = 0
        i_remains = remains
        # while i_remains == [0,0,0]:
        #     if i_remains == [0,0,1]:

        #     i_remains
        probabilities.append(i_probability)
    achieve_probability = max(probabilities)
    return probabilities.index(achieve_probability), achieve_probability

def get_current_info():
    targets = []
    targets.append(int(input()))
    targets.append(int(input()))
    targets.append(int(input()))

    levels = []
    levels.append(int(input()))
    levels.append(int(input()))
    levels.append(int(input()))

    remains = []
    remains.append(int(input()))
    remains.append(int(input()))
    remains.append(int(input()))

    probability = int(input())/100
    return targets, levels, remains, probability

if __name__ == "__main__":
    targets, levels, remains, probability = [9,7,3],[6,6,1],[4,3,5],65/100
    # targets, levels, remains, probability = [1,1,1],[0,0,0],[2,2,2],65/100
    # targets, levels, remains, probability = get_current_info()
    dp = {
        0.75:{},
        0.65:{},
        0.55:{},
        0.45:{},
        0.35:{},
        0.25:{}
    }
    for i in range(3):
        targets[i] -= levels[i]
    probability, dp = get_probability(targets, remains, probability, dp)
    print(dp)
    print(probability)
