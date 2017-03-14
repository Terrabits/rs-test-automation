class ConnectControls {
  show() {
    $('#connect-controls').removeClass('hide');
  }
  hide() {
    $('#connect-controls').addClass('hide');
  }
  enable() {
    $('#address').removeAttr('disabled');
    $('#connect-button').removeAttr('disabled');
  }
  disable() {
    $('#address').attr('disabled', 'disabled');
    $('#connect-button').attr('disabled', 'disabled');
  }
}

module.exports = new ConnectControls();
