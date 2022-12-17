const obj = {
    '1': 'I',
    '4': 'IV',
    '5': 'V',
    '9': 'IX',
    '10': 'X',
    '40': 'XL',
    '50': 'L',
    '90': 'XC',
    '100': 'C',
    '400': 'CD',
    '500': 'D',
    '900': 'CM',
    '1000': 'M'
}

function convertToRoman(num) {
    let arr = []
    while (num > 0) {
        let indexObj = Object.keys(obj).findIndex(o => o > num) - 1;
        if (indexObj < 0) indexObj = Object.keys(obj).length -1;
        const entries = Object.entries(obj)[indexObj];

        let times = Math.floor(num/ entries[0]);
        let newNumber = entries[1];
        const factor = times;

        while (times > 1){
            newNumber += entries[1];
            times -= 1;
        }
        arr.push(newNumber)
        num = num -(factor * entries[0])
    }   
    const roman = arr.join('')
    return roman;
   }
   
convertToRoman(2);