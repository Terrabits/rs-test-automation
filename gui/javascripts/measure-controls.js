class MeasureControls {
  show() {
    $('#measure-controls').removeClass('hide');
  }
  hide() {
    $('#measure-controls').addClass('hide');
  }
  enable() {
    $('#serial-no').removeAttr('disabled');
    $('#measure-button').removeAttr('disabled');
    $('#disconnect-button').removeAttr('disabled');
  }
  disable() {
    $('#serial-no').attr('disabled', 'disabled');
    $('#measure-button').attr('disabled', 'disabled');
    $('#disconnect-button').attr('disabled', 'disabled');
  }
}

module.exports = new MeasureControls();
