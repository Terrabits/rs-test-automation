function showConsole() {
  $('#console').removeClass('hide')
}
function clearConsole() {
  var console = document.getElementById('console-text')
  console.textContent = ""
}
function printToConsole(data) {
  var pre = document.getElementById('console-text');
  pre.textContent = pre.textContent + data;
  var div = document.getElementById('console');
}
function printToConsoleAndScroll(data) {
  printToConsole(data);
  $('#console').scrollTop($('#console-text').height());
}
function hideConsole() {
  $('#console').addClass('hide')
}

module.exports = {
  show: showConsole,
  clear: clearConsole,
  print: printToConsole,
  printAndScroll: printToConsoleAndScroll,
  hide: hideConsole
}
