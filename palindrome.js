function palindrome(str) {
    const replacedStr = str.toLowerCase().replace(/[^a-z0-9]/gi, ''); // replace all non-numeric chars and also _

    const splitedStr = replacedStr.split('');
    const reversedStr = splitedStr.reverse();
    const joinedStr = reversedStr.join('')

    if (joinedStr === replacedStr) return true;
    return false
}
  
palindrome("A man, a plan, a canal. Panama");
