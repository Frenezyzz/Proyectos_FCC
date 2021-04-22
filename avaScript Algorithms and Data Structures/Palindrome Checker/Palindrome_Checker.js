function palindrome(str) {
  let polishedString = str.replace(/\W+|_/g,"").toLowerCase();
  let reversedString = polishedString.split("").reverse().join("");
  if (polishedString != reversedString){
    return false;
  }
  return true;
}



palindrome("eye");