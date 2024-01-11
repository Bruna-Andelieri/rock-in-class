/* script to block calendar dates 
TODO: verificar se isso funciona
*/
$(document).ready(function () {
  $("#datePicker").datepicker({
    todayHighlight: true,
    autoclose: true,
    beforeShowDay: function (date) {
      // Array containing blocked dates in 'yyyy-mm-dd' format
      var blockedDates = ["2023-12-25", "2023-12-31"]; // Add more dates if needed

      var formattedDate = moment(date).format("YYYY-MM-DD"); // Format the date

      // Check if the date is in the array of blocked dates
      if (blockedDates.indexOf(formattedDate) !== -1) {
        return {
          enabled: false,
        };
      }
      return;
    },
  });
});
