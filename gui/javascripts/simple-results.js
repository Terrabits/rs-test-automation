
class SimpleResults {
  show() {
    $('#simple-results').removeClass('hide');
  }
  hide() {
    $('#simple-results').addClass('hide');
  }
  add(serialNo, data) {
    var currentRow = $('#simple-results tr.current-row');
    var newRow = $(currentRow[0].cloneNode(true));
    newRow.find('td.timestamp').text(data['timestamp']);
    newRow.find('td.serial-no').text(serialNo);
    var tdStatus = newRow.find('td.status');
    tdStatus.removeClass('passed');
    tdStatus.removeClass('failed');
    if (data['limits']) {
      tdStatus.text(data['limits']);
      tdStatus.addClass(data['limits']);
    }
    else {
      tdStatus.text("Done");
    }
    var table = $('#simple-results table');
    table.prepend(newRow);
    currentRow.removeAttr('class');
  }
}
module.exports = new SimpleResults();
