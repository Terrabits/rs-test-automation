class FullResults {
  get shown() {
    return !$('#full-results').hasClass('hide');
  }
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
