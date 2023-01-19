function solution(fees, records) {
    let answer = [];
    let carMap = new Map(); // 입-출차 시간맵
    let parkTime = new Map(); // 주차시간 기록 맵
    
    for (let r of records) {
        let info = r.split(" ");
        if (info[2] == 'IN') { //입차인 경우 carMap에 기록
            carMap.set(info[1], info[0]); // carNum => inputTime
        } else { // 출차인 경우 주차시간 계산 후 carMap에서 삭제
            let inTime = carMap.get(info[1]);
            let inHourMin = inTime.split(":");
            let outHourMin = info[0].split(":");
            let inMin = inHourMin[0] * 60 + parseInt(inHourMin[1]);
            let outMin = outHourMin[0] * 60 + parseInt(outHourMin[1]);
            const elapsedMin = outMin - inMin; // 주차시간(분)

            if (parkTime.has(info[1])) {
                parkTime.set(info[1], parkTime.get(info[1]) + elapsedMin);
            } else {
                parkTime.set(info[1], elapsedMin);
            }
            carMap.delete(info[1]);
        }
    }
    
    for (let [carNum, inTime] of carMap) { // 출차 기록 없는 차량 체크
        let inHourMin = inTime.split(":");
        let inMin = inHourMin[0] * 60 + parseInt(inHourMin[1]);
        let outMin = 23 * 60 + 59;
        const elapsedMin = outMin - inMin;
            
        if (parkTime.has(carNum)) {
            parkTime.set(carNum, parkTime.get(carNum) + elapsedMin);
        } else {
            parkTime.set(carNum, elapsedMin);
        }
    }
    
    const sortParkMap = new Map([...parkTime.entries()].sort());

    for (let value of sortParkMap.values()) { // 주차요금 계산
        let stdTime = fees[0];
        let stdFee = fees[1];
        let unitTime = fees[2];
        let unitMoney = fees[3];
        
        if (value <= stdTime) {
            answer.push(stdFee);
        } else {
            let amount = stdFee + Math.ceil((value - stdTime) / unitTime) * unitMoney;
            answer.push(amount);
        }
    }
    
    return answer;
}