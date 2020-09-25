$(document).ready(function () {
    $("#runCode").click(function () {
        //get values
        var code = editor.getValue();
        $.ajax({
            type: 'POST',
            url: "{{ url_for('home') }}",
            data: {'code': code},
            success: function (response) {
                var error = response["error"];
                var result = response["output"];

                if (result) {
                    $("#output").val(result);
                } else {
                    $("#error").html(error);
                }

            }
        })
    })

    $("#clearOutput").click(function () {
        $("#output").val("");
    })

});
