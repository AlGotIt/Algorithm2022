function solution(topping) {
    var answer = 0;
    var i = 0;
    var num_arr = new Array(10001).fill(0);
    var num_check = new Array(10001).fill(0);
    var max_num = new Set(topping);
    for (i = 0; i<topping.length; i++) {
        num_arr[topping[i]]++;
    }
    
    let[me, brother] = [0, max_num.size];
    for (i = 0; i<topping.length; i++) {
        if (num_arr[topping[i]] >= 1) {
            num_arr[topping[i]]--;
            if(!num_check[topping[i]]){
                me++;
            } 
            num_check[topping[i]] = 1;
        }
        if (num_arr[topping[i]] == 0 && num_check[topping[i]]) brother--;
        if (me == brother){
            answer++;
        }
    }
    
    return answer;
}
