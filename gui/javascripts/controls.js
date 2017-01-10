function clearAddress() {
  document.getElementById('ip-address').value = '';
}
function ipAddress() {
  return document.getElementById('ip-address').value;
}
function setIpAddress(address) {
  document.getElementById('ip-address').value = address;
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

function showAlert() {
  $('.alert').removeClass('invisible');
}
function setAlert(message) {
  $('.alert').text(message);
}
function hideAlert() {
  $('.alert').addClass('invisible');
}

module.exports = {
  clearAddress: clearAddress,
  ipAddress: ipAddress,
  setIpAddress: setIpAddress,
  showConnect: showConnect,
  enableConnect: enableConnect,
  disableConnect: disableConnect,
  clearSerialNumber: clearSerialNumber,
  serialNumber: serialNumber,
  showMeasure: showMeasure,
  enableMeasure: enableMeasure,
  disableMeasure: disableMeasure,
  showAlert: showAlert,
  setAlert: setAlert,
  hideAlert: hideAlert
}
