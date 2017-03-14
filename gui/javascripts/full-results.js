const path = window.nodeRequire('path');
const fs   = window.nodeRequire('fs');

class FullResults {
  hide() {
    $('#full-results').addClass('hide');
  }
  show() {
    $('#full-results').removeClass('hide');
  }
  set url(loc) {
    var iframe = $('#full-results');
    iframe.attr('src', loc);
  }
  clearUrl() {
    this.url = '';
  }
}

module.exports = new FullResults();
