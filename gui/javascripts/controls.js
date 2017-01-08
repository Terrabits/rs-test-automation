function clearAddress() {
  document.getElementById('ip-address').value = '';
}
function ipAddress() {
  return document.getElementById('ip-address').value;
}
function showConnect() {
  $('#connect-controls').removeClass('hide');
  $('#measure-controls').addClass('hide');
}
function disableConnect() {
  $('#ip-address').attr('disabled', 'disabled');
  $('#connect').attr('disabled', 'disabled');
}
function enableConnect() {
  $('#ip-address').removeAttr('disabled');
  $('#connect').removeAttr('disabled');
}

function clearSerialNumber() {
  document.getElementById('serial-no').value = '';
}
function serialNumber() {
  return document.getElementById('serial-no').value;
}
function showMeasure() {
  $('#connect-controls').addClass('hide');
  $('#measure-controls').removeClass('hide');
}
function disableMeasure() {
  $('#serial-no').attr('disabled', 'disabled');
  $('#measure').attr('disabled', 'disabled');
  $('#disconnect').attr('disabled', 'disabled');
}
function enableMeasure() {
  $('#serial-no').removeAttr('disabled');
  $('#measure').removeAttr('disabled');
  $('#disconnect').removeAttr('disabled');
}

module.exports = {
  clearAddress: clearAddress,
  ipAddress: ipAddress,
  showConnect: showConnect,
  enableConnect: enableConnect,
  disableConnect: disableConnect,
  clearSerialNumber: clearSerialNumber,
  serialNumber: serialNumber,
  showMeasure: showMeasure,
  enableMeasure: enableMeasure,
  disableMeasure: disableMeasure
}
