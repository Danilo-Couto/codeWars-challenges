function telephoneCheck(str) {
    const regex1 = /^[0-9]{3}[-][0-9]{3}[-][0-9]{4}$/;
    const regex2 = /^[(][0-9]{3}[)][0-9]{3}[-][0-9]{4}$/;
    const regex3 = /^[(][0-9]{3}[)][\s][0-9]{3}[-][0-9]{4}$/;
    const regex4 = /^[0-9]{3}[\s][0-9]{3}[\s][0-9]{4}$/;
    const regex5 = /^[0-9]{10}$/;
    const regex6 = /^[1]{1}[\s][0-9]{3}[\s][0-9]{3}[\s][0-9]{4}$/;
    const regex7 = /^[1]{1}[\s][0-9]{3}[-][0-9]{3}[-][0-9]{4}$/;
    const regex8 = /^[1]{1}[\s][(][0-9]{3}[)][\s][0-9]{3}[-][0-9]{4}$/;
    const regex9 = /^[1]{1}[(][0-9]{3}[)][0-9]{3}[-][0-9]{4}$/;
      
    if (!(str.match(regex1) || (str.match(regex2)) || (str.match(regex3)) || (str.match(regex4)) || (str.match(regex5)) || (str.match(regex6)) || (str.match(regex7)) || (str.match(regex8)) || (str.match(regex9)))) {
      return false;
    }
    return true;
  };


