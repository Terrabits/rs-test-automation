function showResults() {
  $('#results').removeClass('hide')
}
function setResultsUrl(url) {
  iframe = document.getElementById('results-frame')
  iframe.src = url
}
function hideResults() {
  $('#results').addClass('hide')
}

module.exports = {
  show: showResults,
  setUrl: setResultsUrl,
  hide: hideResults
}
