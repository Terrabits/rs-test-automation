const moment   = window.nodeRequire('moment');

class SimpleResults {
  constructor() {
    moment.locale(navigator.language);
  }
  get shown() {
    return !$('#simple-results').hasClass('hide');
  }
  show() {
    $('#simple-results').removeClass('hide');
  }
  hide() {
    $('#simple-results').addClass('hide');
  }
  add(serialNo, data) {
    // clear current row
    var currentRow = $('#simple-results tr.current-row');
    currentRow.removeAttr('class');

    // Create new row
    var _serialNo  = $('<td class="serial-no"></td>')
    var _timestamp = $('<td class="timestamp"></td>')
    var _limits    = $('<td class="status"></td>')
    _serialNo.text(serialNo);
    _timestamp.text(moment().format('lll'));
    // if (data['timestamp']) {
    //   _timestamp.text(data['timestamp']);
    // }
    // else {
    //   _timestamp.text(Date());
    // }
    if (data['limits']) {
      _limits.text(data['limits']);
      _limits.addClass(data['limits']);
    }
    else {
      _limits.text("Done");
    }

    var newRow = $('<tr class="current-row"></tr>');
    newRow.append(_serialNo);
    newRow.append(_timestamp);
    newRow.append(_limits);

    // prepend
    var table = $('#simple-results table tbody');
    table.prepend(newRow);
  }
}
module.exports = new SimpleResults();
