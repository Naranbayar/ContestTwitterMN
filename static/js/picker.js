var dateAndTimePickers = function () {
    var initPickers = function () {
        if (jQuery().datepicker) {
            $('.date-picker').datepicker({
                rtl: Metronic.isRTL(),
                orientation: "left",
                format: 'yyyy-mm-dd',
                autoclose: true
            });
            $('.timepicker').timepicker({
                autoclose: true,
                showSeconds: false,
                minuteStep: 1,
                showMeridian: false
            });
        }
    };
    return {
        init: function () {
            initPickers();
        }
    };
}();