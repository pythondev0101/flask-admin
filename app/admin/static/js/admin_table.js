$(document).ready(function(){

    var js_fields_array = JS_FIELDS.split(",");

    for (i=0; i < js_fields_array.length; i++){
        js_fields_array[i] = js_fields_array[i].replace('[', '');
        js_fields_array[i] = js_fields_array[i].replace(']', '');
        js_fields_array[i] = js_fields_array[i].replace('"', '');
        js_fields_array[i] = js_fields_array[i].replace('"', '');
        js_fields_array[i] = js_fields_array[i].replace(/\s/g, '');
    }


    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
            }
        }
    });


    var dtbl_table = $('#index_table').DataTable({
        "dom": 'rtip',
        "pageLength": 20,
        "order": [[ 1, 'asc' ]]
    });


    dtbl_table.on( 'order.dt search.dt', function () {
        dtbl_table.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();


    $('.search-input').on('keyup', function () {
        dtbl_table.search(this.value).draw();
    } );


    $("#index_table tbody").on('click','.row_object',function(){

        if (VIEW_MODAL != 'True'){
            return;
        }

        var id = '#param_' + $(this).attr('id');
        
        if($("#view_edit_button").length){
            const view_url = $(id).attr('value');
            document.getElementById("view_edit_button").setAttribute("href", view_url);
        }

        var ctr;
        var field;
        var field_id = $(this).attr('id');
        
        for (ctr=0; ctr < js_fields_array.length; ctr++){
            $.ajax({
                url: `/admin/_get_view_modal_data?table=${TABLE_NAME}&column=${js_fields_array[ctr]}&id=${field_id}`,
                type: "GET",
                contentType: "application/json; charset=utf-8",
                success: function(data) {
                    if (data.result){
                        field = "#view_" + data.column;
                        var input_type = $(field).attr('type');
                        if (input_type == 'checkbox'){
                            if (data.result == '1'){
                                $(field).attr('checked',true);
                            }else{
                                $(field).attr('checked', false);
                            }
                        }else{
                            $(field).val(data.result);
                        }
                    }
                }
            });
        }
        
    });


    $("#btndelete").click(function(){
        if($('#btndelete').text()=='Delete'){
            $('#nav_action_btns').after("<button id='btn_confirm_delete' type='button' tabindex='1' class='dropdown-item'>Confirm Delete</button>");
            $('#btndelete').html("Cancel");
            $("tr").removeAttr("data-toggle");
            $("tr").find("th:last").after('<th>DELETE</th>');
            $("tr").find("td:last").after("<td><input class='chkbox' type='checkbox'></td>");
            var ids = [];
            $("#btn_confirm_delete").click(function(){
                $("tr.item").each(function() {
                    var check = $(this).find("input.chkbox").is(':checked');
                    if(check){
                        ids.push(this.id)
                    }
                });

                $.ajax({
                    url: "/admin/delete-data",
                    type: "POST",
                    dataType: "json",
                    data: JSON.stringify({'ids': ids,'table':TABLE_NAME}),
                    contentType: "application/json; charset=utf-8",
                    success: function(data) {
                        if(data.result == 2){
                            alert("Must check some row!");
                        }else{
                            location.reload();
                        }
                    }
                });
            });
        }else{
            $("#btn_confirm_delete").remove();
            $('#btndelete').html("Delete");
            $("tr").attr("data-toggle","modal");
            $("tr").find("th:last").remove();
            $("tr").find("td:last").remove();
        }
    });


    $("#username").change(function(){
        var username = document.getElementById("username").value;
       
        $.ajax({
            url: "/auth/username_check",
            type: "POST",
            dataType: "json",
            data: JSON.stringify({'username': username}),
            contentType: "application/json; charset=utf-8",
            success: function(data) {
                if(data.result == 1){
                    $("#username-invalid-feedback").text("Please provide a valid Username");
                    document.getElementById("username-invalid-feedback").style.display = "none";
                    document.getElementById("username-valid-feedback").style.display = "block";
                }else{
                    $("#username-invalid-feedback").text("Username is already taken.");
                    document.getElementById("username-valid-feedback").style.display = "none";
                    document.getElementById("username-invalid-feedback").style.display = "block";
                }
            }
        });
    });
    $("#email").change(function(){
        var email = document.getElementById("email").value;

        $.ajax({
            url: "/auth/_email_check",
            type: "POST",
            dataType: "json",
            data: JSON.stringify({'email': email}),
            contentType: "application/json; charset=utf-8",
            success: function(data) {
                if(data.result == 1){
                    $("#email-invalid-feedback").text("Please provide a valid Email");
                    document.getElementById("email-invalid-feedback").style.display = "none";
                    document.getElementById("email-valid-feedback").style.display = "block";
                }else{
                    $("#email-invalid-feedback").text("Email is already taken.");
                    document.getElementById("email-valid-feedback").style.display = "none";
                    document.getElementById("email-invalid-feedback").style.display = "block";
                }
            }
        });
    });
});