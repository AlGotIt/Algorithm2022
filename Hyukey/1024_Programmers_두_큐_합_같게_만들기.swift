//
//  main.swift
//  Algorithm
//
//  Created by Wonhyuk Choi on 2022/09/20.
//

import Foundation

func solution(_ queue1:[Int], _ queue2:[Int]) -> Int {
    var pointer1 = 0
    var pointer2 = queue2.count
    
    let totalArray = queue1 + queue2
    let totalSum = totalArray.reduce(0, +)
    
    // 1. 반으로 안나눠 지는 경우 에러
    guard totalSum % 2 == 0 else { return -1 }
    let targetSum = totalSum / 2
    
    var presentSum = queue1.reduce(0, +)
    var answer = 0
    
    // 2. 한 큐를 맞추면 다른 큐도 맞춰짐
    while presentSum != targetSum {
        // 두 포인터가 겹칠 경우 에러
        if pointer1 == pointer2 { return -1 }
        // 최대로 이동 할 수 있는 구간을 넘을 경우 에러
        if answer > totalArray.count * 2 { return -1 }
        
        // 부족하면 포인터2를 이동, 넘치면 포인터1을 이동
        if presentSum < targetSum {
            presentSum += totalArray[pointer2]
            pointer2 += 1
            answer += 1
        } else {
            presentSum -= totalArray[pointer1]
            pointer1 += 1
            answer += 1
        }
        
        if pointer1 == totalArray.count { pointer1 = 0 }
        if pointer2 == totalArray.count { pointer2 = 0 }
    }
    
    return answer
}

var queue1 = [1, 1]
var queue2 = [1, 5]

print(solution(queue1, queue2))
