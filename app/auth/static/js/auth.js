$(document).ready(function () {

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
            }
        }
    });

    var table = $('.inline-table').DataTable({
        "dom": 'rtip',
        "bInfo": false,
        "scrollY": "200px",
        "scrollCollapse": true,
        "paging": false,
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


function role_edit_chk(permission_id) {
    var input_read = document.getElementById("edit_chk_read_".concat(permission_id)).checked;
    var input_create = document.getElementById("edit_chk_create_".concat(permission_id)).checked;
    var input_write = document.getElementById("edit_chk_write_".concat(permission_id)).checked;
    var input_delete = document.getElementById("edit_chk_delete_".concat(permission_id)).checked;
    var csrf_token = "{{ csrf_token() }}";
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("post", "/auth/role_edit_permission", true);
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            if (xmlHttp.responseText.trim() == 1) {
                console.log("Saved");
            } else if (xmlHttp.responseText.trim() == 0) {
                console.log("Not Saved");
            }
        }
    }
    xmlHttp.setRequestHeader("X-CSRFToken", csrf_token);
    var data = JSON.stringify({
        "permission_id": permission_id, "read": input_read, "create": input_create,
        "write": input_write, "delete": input_delete
    });
    xmlHttp.send(data);
}
