$(document).ready(function() {
  $('select').material_select();
  $(".button-collapse").sideNav();
  $('.modal').modal();
  $('.modal-trigger').leanModal();
});

$('.datepicker').pickadate({
  selectMonths: true,
  selectYears: 200,
  today: 'Today',
  clear: 'Clear',
  close: 'Ok',
  closeOnSelect: false
})
