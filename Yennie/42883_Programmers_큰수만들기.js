function solution(number, k) {
    const numberStack = []; // answer을 저장할 스택 배열
    var answer;
    for (let i = 0; i < number.length; i++) {
      // 스택 마지막 숫자와 현재 숫자를 비교하며 현재 숫자가 더 스택의 가장 마지막 숫자를 pop
      while (numberStack.length > 0 && numberStack[numberStack.length - 1] < number[i] && k > 0) {
        numberStack.pop();
        k--; // 현재 숫자보다 큰 수가 나올때까지 최대 k번 반복함
      }
      numberStack.push(number[i]);
    }

    // 모든 숫자를 비교한 후 k가 0보다 크면 남은 k만큼 뒤에서 제거함
    numberStack.splice(number.length - k, k); 
    answer = numberStack.join("");
    return answer;
  }