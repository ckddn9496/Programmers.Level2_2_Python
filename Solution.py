prices = [1,2,3,2,3]

def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        price = prices[i]
        for j in range(i+1, len(prices)):
            if prices[j] < price:
                answer.append(j-i)
                break
            if j == len(prices)-1:
                answer.append(j-i)
    answer.append(0)
    return answer

print(solution(prices))
