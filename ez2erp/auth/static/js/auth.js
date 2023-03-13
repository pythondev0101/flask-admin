$(document).ready(function () {

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
            }
        }
    });


    if (!($('#role_id').val() == 1)) {
        $('.inlines-card').hide();
    }


    $('#role_id').on('change', function () {
        if (!(this.value == 1)) {
            $('.inlines-card').hide();
        } else {
            $('.inlines-card').show();
        }
    });


    $("#username").change(function () {

        var username = document.getElementById("username").value;

        $.ajax({
            url: "/auth/username_check",
            type: "POST",
            dataType: "json",
            data: JSON.stringify({ 'username': username }),
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                if (data.result == 1) {
                    $("#username-invalid-feedback").text("Please provide a valid Username");
                    document.getElementById("username-invalid-feedback").style.display = "none";
                    document.getElementById("username-valid-feedback").style.display = "block";
                } else {
                    $("#username-invalid-feedback").text("Username is already taken.");
                    document.getElementById("username-valid-feedback").style.display = "none";
                    document.getElementById("username-invalid-feedback").style.display = "block";
                }
            }
        });
    });


    $("#email").change(function () {
        var email = document.getElementById("email").value;

        $.ajax({
            url: "/auth/_email_check",
            type: "POST",
            dataType: "json",
            data: JSON.stringify({ 'email': email }),
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                if (data.result == 1) {
                    $("#email-invalid-feedback").text("Please provide a valid Email");
                    document.getElementById("email-invalid-feedback").style.display = "none";
                    document.getElementById("email-valid-feedback").style.display = "block";
                } else {
                    $("#email-invalid-feedback").text("Email is already taken.");
                    document.getElementById("email-valid-feedback").style.display = "none";
                    document.getElementById("email-invalid-feedback").style.display = "block";
                }
            }
        });
    });


    $(".permission-read").click(function(){
        const permission_id = $(this).val();
        const value = $(this).is(":checked");
        const url = "permissions/" + permission_id + "/edit";

        $.ajax({
            url: url,
            type: "POST",
            dataType: "json",
            data: JSON.stringify({
                "permission_type": "read",
                "value": value
            }),
            contentType: "application/json; charset=utf-8",
            success: function(data){
                // TODO: make toast information
                if(data){
                    console.log("Saved!");
                }else{
                    console.log("Not saved!");
                }
            }
        });
    });


    $(".permission-create").click(function(){
        const permission_id = $(this).val();
        const value = $(this).is(":checked");
        const url = "permissions/" + permission_id + "/edit";

        $.ajax({
            url: url,
            type: "POST",
            dataType: "json",
            data: JSON.stringify({
                "permission_type": "create",
                "value": value
            }),
            contentType: "application/json; charset=utf-8",
            success: function(data){
                // TODO: make toast information
                if(data){
                    console.log("Saved!");
                }else{
                    console.log("Not saved!");
                }
            }
        });
    });


    $(".permission-write").click(function(){
        const permission_id = $(this).val();
        const value = $(this).is(":checked");
        const url = "permissions/" + permission_id + "/edit";

        $.ajax({
            url: url,
            type: "POST",
            dataType: "json",
            data: JSON.stringify({
                "permission_type": "write",
                "value": value
            }),
            contentType: "application/json; charset=utf-8",
            success: function(data){
                // TODO: make toast information
                if(data){
                    console.log("Saved!");
                }else{
                    console.log("Not saved!");
                }
            }
        });
    });


    $(".permission-delete").click(function(){
        const permission_id = $(this).val();
        const value = $(this).is(":checked");
        const url = "permissions/" + permission_id + "/edit";

        $.ajax({
            url: url,
            type: "POST",
            dataType: "json",
            data: JSON.stringify({
                "permission_type": "delete",
                "value": value
            }),
            contentType: "application/json; charset=utf-8",
            success: function(data){
                // TODO: make toast information
                if(data){
                    console.log("Saved!");
                }else{
                    console.log("Not saved!");
                }
            }
        });
    });

});
