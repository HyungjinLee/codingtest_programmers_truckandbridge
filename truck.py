from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque() # 큐를 생성
    for i in range (bridge_length) :
        bridge.append(0) # 다리 길이만큼 빈칸 생성
    weightsum,k,step = 0,0,0
    
    while len(truck_weights)>k: # 시간 복잡도를 줄이기 위해 인덱스로 접근
        if weightsum <= weight: # 트럭 무게 초과하지 않은 경우
            nextweight = truck_weights[k] #다음에 건널 트럭
            if weightsum+nextweight  <= weight: # 조건
                weightsum+=nextweight
                bridge.append(nextweight)
                k+=1
            else : # 트럭 무게 초과한 경우
                if weightsum - bridge[0] + nextweight <= weight : # 끝에 트럭이 나가고 바로 건널 수 있는 조건 ex ) [7,0] -> [0,4], bridge_length = 10
                    weightsum+=nextweight
                    bridge.append(nextweight)
                    k+=1
                else :
                    bridge.append(0)
            weightsum-=bridge.popleft()
            step+=1
    return bridge_length+step 