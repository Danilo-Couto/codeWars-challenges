function fatoracao(n) {
    if (n === 0 || n === 1)
      return;
    for (let i = n - 1; i >= 1; i--) {
      n *= i;
    }
    return n;
  }

function fatoracao(n) {
  let result = 1;
  for (let i = 2; i <= n; i += 1) {
    result *= i;
  } 
  return result;
}

function fatoracao(n) {
  return [0, 1].includes(n) ? 1 : n * realizaFatoracao(n - 1);}
