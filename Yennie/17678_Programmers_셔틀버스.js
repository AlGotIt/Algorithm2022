function solution(n, t, m, timetable) {
    var answer = '';
    let i, answerMin;
    let sortedT = timetable.sort();
    let startMin = 9 * 60;
    let arrivedT, arrivedMin;

    for (i=0; i<n; i++) {
        let nm = m;
        while (nm > 0 && sortedT.length != 0) { // 자리 남아있고 줄 선 크루가 있을 경우
            arrivedT = sortedT[0].split(":");
            arrivedMin = arrivedT[0] * 60 + parseInt(arrivedT[1]);
            if (arrivedMin <= startMin) {
                sortedT.shift(); // 탑승
                nm--;
            } else { // 줄선 사람 중에 현재 차량 탈 수 있는 사람 없음
                break;
            }
        }
        if (i+1 == n){ // 막차인 경우 콘도 타야함.
            if (nm > 0) { // 자리 남았을 경우
                answerMin = startMin;
            } else { // 자리없음 => 마지막으로 탄 애보다 일찍와야 됨.
                answerMin = arrivedMin - 1;
            } 
        } else { // 배차 시켜주기
            startMin = startMin + t;
        }
    }
    
    let answerHours = parseInt(answerMin / 60);
    let answerMinutes = answerMin % 60;
    
    if (answerHours < 10) answerHours = "0" + answerHours;
    if (answerMinutes < 10) answerMinutes = "0" + answerMinutes;
    
    answer = answerHours + ":" + answerMinutes;

    return answer;
}