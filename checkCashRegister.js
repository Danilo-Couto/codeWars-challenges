const obj = {
  "PENNY": 0.01, 
  "NICKEL": 0.05, 
  "DIME": 0.1, 
  "QUARTER": 0.25, 
  "ONE": 1 ,
  "FIVE": 5 ,
  "TEN": 10 ,
  "TWENTY": 20 ,
  "ONE HUNDRED": 100
};

function checkCashRegister(price, cash, cid) {
  let result = {status: "", change: []};
  let change = (cash - price);

  const inChasier = cid.reduce((acc, curr) => (acc + curr[1]), 0);

  if (change > inChasier) {
    result.status = "INSUFFICIENT_FUNDS";
    return result;
  } else if (change === inChasier) {
    result.status = "CLOSED";
    result.change = cid;
    return result;
  } else {
    result.status = "OPEN";
  }

  cid.forEach(el => obj[el[0]] = new Array(el[1], obj[el[0]]));

  for (let i = cid.length-1; i >= 0; i--) {
    const unit = cid[i][0];
    const bill = Object.entries(obj)[i][1][1];
    const amount = (Object.entries(obj)[i][1][0]).toFixed(2);

    if (amount > 0 && change >= bill) {
      if (change >= amount && amount > bill ){
        const module = (change % amount);
        result.change = [...result.change, (([unit, (change - module)]))];
        change = module.toFixed(2);
      } else if (change < amount) {
        const module = (change % bill);
        result.change = [...result.change, (([unit, (change - module)]))];
        change = module.toFixed(2);
      }      
    }
  }
  
  if (result.change.length === 0) result.status = "INSUFFICIENT_FUNDS";
  return result;
}

// checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]) 
// {status: "OPEN", change: [["TWENTY", 60], ["TEN", 20], ["FIVE", 15], ["ONE", 1], ["QUARTER", 0.5], ["DIME", 0.2], ["PENNY", 0.04]]}

// checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]])
// {status: "INSUFFICIENT_FUNDS", change: []}

// checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]])
// {status: "CLOSED", change: [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]}.