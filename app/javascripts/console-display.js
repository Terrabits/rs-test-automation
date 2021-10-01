class ConsoleDisplay {
  show() {
    $('#console').removeClass('hide')
  }
  hide() {
    $('#console').addClass('hide')
  }
  print(text) {
    var pre = $('#console-text');
    pre.text(pre.text() + text);
  }
  scrollDown() {
    $('#console').scrollTop($('#console-text').height());
  }
  clear() {
    $('#console-text').text('');
  }
}

module.exports = new ConsoleDisplay();
