# python 3.8

def solution(routes:list) -> int :
    """"
    Args:
        routes (list): n대의 차량의 진입 / 진출 지점이 포함된 2차원 리스트

    Returns:
        int: 모든 차량이 단속카메라에 한 번은 촬영되도록 하는 최소 카메라 개수 
    """
    sorted_routes = sorted(routes, key=lambda x:x[1])       # 진출 지점에 따라 정렬
    answer = 1                                              # 1개의 단속카메라로 시작
    camera = sorted_routes[0][1]                            # 가장 뒤에 있는 단속 카메라의 위치
    for i in range(1, len(sorted_routes)):                  
        if sorted_routes[i][0] <= camera: continue          # 다음 차량의 진입 지점이 단속카메라 위치보다 앞이라면 촬영된 것으로 간주
        else: 
            camera = sorted_routes[i][1]                    # 다음 차량의 진입 지점이 단속카메라 위치보다 뒤라면 카메라 추가 설치
            answer += 1                                     
    return answer


routes = [[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]
print(solution(routes))