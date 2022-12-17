const alphabet = 'abcdefghijklmnopqrstuvwxyz'.toUpperCase().split('');

function rot13(str) {
    const arrStr = str.split('');  
    let arr = [];
    for (let i = 0; i < arrStr.length; i++) {
        const index = alphabet.findIndex(el => arrStr[i]===el);
        if (index >= 0) {
            const newIndex = (index + 13) % 26;
            const newChar = alphabet[newIndex];
            arr.push(newChar);
        } else {
            arr.push(arrStr[i]);
        }
    }
    const newStr = arr.join('');
    return newStr;
  }
  
  rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.");
