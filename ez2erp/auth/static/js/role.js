$(document).ready(function () {

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
            }
        }
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
