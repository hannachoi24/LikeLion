$(function () {
  $('#myTab a:last').tab('show');
});

$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
  var target = $(e.target).attr("href");
  if ((target == '#messages')) {
      alert('ok');
  } else {
      alert('not ok');
  }
});