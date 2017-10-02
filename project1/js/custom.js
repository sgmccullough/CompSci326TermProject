$(document).ready(function() {
  $(".button-collapse").sideNav();
  $('.modal').modal();
  $('.modal-trigger').leanModal();
  $('select').material_select();
});

$('.datepicker').pickadate({
  selectMonths: true,
  selectYears: 200,
  today: 'Today',
  clear: 'Clear',
  close: 'Ok',
  closeOnSelect: false
})
