function calcFibo(n) {
    const fibSequence = [1];
    let curr = 1;
    let prev = 0;
  
    if (n === 1) {
      return fibSequence;
    }
    for (let i = 0 ; i < n ; i++ ) {
        curr += prev;
        prev = curr - prev;
        fibSequence.push(curr);
    }
  
    return fibSequence;
  }
