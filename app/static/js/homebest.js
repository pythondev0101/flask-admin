//$(function(){
//    $('#userModal').modal({
//        keyboard: true,
//        backdrop: "static",
//        show:false,
//
//    }).on('show', function(){ //subscribe to show method
//       var getIdFromRow = $(event.target).closest('tr').data('id'); //get the id from tr
//        //make your ajax call populate items or what even you need
//       //$(this).find('#useredit').html($('<b> Order Id selected: ' + getIdFromRow  + '</b>'))
//       document.getElementById("user_edit_button").setAttribute("href", "https://www.w3schools.com");
//
//    });
//});


function row_click(row_obj){
    var url = document.getElementById(row_obj.id).name;
    document.getElementById("user_edit_button").setAttribute("href", url);

}

function close_toast(){
    Element.prototype.remove = function() {
    this.parentElement.removeChild(this);
    }
    NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
    for(var i = this.length - 1; i >= 0; i--) {
        if(this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
}
    document.getElementById("toast-container").remove();
}

