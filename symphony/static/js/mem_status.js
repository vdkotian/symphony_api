$(function () {
        $("#sys_monitor_form").submit(function (event) {
        event.preventDefault();

        var $inputs = $('#sys_monitor_form :input');
        var values = {};
            $inputs.each(function() {
            values[this.name] = $(this).val();
    });
        $.ajax({
            type: "POST",
            url: '/memory_status/status/',
            data: values,
            success: function (data) {
                data_rows = data['data'].split("\n");
                data_html = "";
                table_heading = '<tr><th>Values and Variables</th></tr>'
                for (var i = 0; i < data_rows.length; i++) {

                    data+='<tr><td scope="col">'+data_rows[i]+'</td></tr>'
                }
                $("#data").html(table_heading + data)
            },
            error: function () {
                $("#connect_btn").html('Connect');
            }
        });
    });
});