# python 3.10

def solution(routes):
    """
    Args:
        routes : 고속도로를 이동하는 차량의 경로

    Returns:
        모든 차량이 한 번은 단속용 카메라를 만나도록 설치해야 하는 카메라의 최소 대수
    """
    answer = 0

    routes.sort(key=lambda x:x[1])

    curCam = -30001
    for r in routes:
        if curCam < r[0]:
            answer+=1
            curCam = r[1]

    return answer