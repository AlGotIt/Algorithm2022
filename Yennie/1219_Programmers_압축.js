function solution(msg) {
    var ind, answer = [];
    let alphaMap = new Map();

    // 기본 알파벳맵 만들기 (아스키코드 사용)
    for (var i = 65; i<91; i++){
        ind = i-64;
        alphaMap.set(String.fromCharCode(i), ind);
    }
    ind++;
    
    // 인덱스 추가 & LZW 압축 시작
    for (var x = 0; x<msg.length; x++) {
        var i, temp='';

        for (i = x; i < msg.length; i++){
            temp += msg[i];
            
            if (alphaMap.has(temp)) {
                if ((msg.length - (i + 1)) > 0) { // 체크할 알파벳이 더 있는 경우
                    continue;
                } else {
                    answer.push(alphaMap.get(temp)); 
                    x += temp.length -1
               }
            }  else { //인덱스가 존재하지 않는경우
                alphaMap.set(temp, ind); // 인덱스 추가
                ind++;

                var res = temp.slice(0, -1); // 마지막으로 추가한 단어 제거
                answer.push(alphaMap.get(res));
                x += res.length -1 // for문 간격 증가
                break;
            }
        }
    }
    return answer;
}