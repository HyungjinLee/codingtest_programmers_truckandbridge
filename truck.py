from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque() # ť�� ����
    for i in range (bridge_length) :
        bridge.append(0) # �ٸ� ���̸�ŭ ��ĭ ����
    weightsum,k,step = 0,0,0
    
    while len(truck_weights)>k: # �ð� ���⵵�� ���̱� ���� �ε����� ����
        if weightsum <= weight: # Ʈ�� ���� �ʰ����� ���� ���
            nextweight = truck_weights[k] #������ �ǳ� Ʈ��
            if weightsum+nextweight  <= weight: # ����
                weightsum+=nextweight
                bridge.append(nextweight)
                k+=1
            else : # Ʈ�� ���� �ʰ��� ���
                if weightsum - bridge[0] + nextweight <= weight : # ���� Ʈ���� ������ �ٷ� �ǳ� �� �ִ� ���� ex ) [7,0] -> [0,4], bridge_length = 10
                    weightsum+=nextweight
                    bridge.append(nextweight)
                    k+=1
                else :
                    bridge.append(0)
            weightsum-=bridge.popleft()
            step+=1
    return bridge_length+step 