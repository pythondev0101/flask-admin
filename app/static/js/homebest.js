window.addEventListener('load', function () {

})

function row_click(row_obj,model){
    if (model == "Users"){
    var url = document.getElementById(row_obj.id).name;
    document.getElementById("user_edit_button").setAttribute("href", url);
    document.getElementById("view_fname").value = row_obj.cells[1].innerHTML;
    document.getElementById("view_lname").value = row_obj.cells[2].innerHTML;
    document.getElementById("view_username").value = row_obj.cells[0].innerHTML;
    document.getElementById("view_email").value = row_obj.cells[3].innerHTML;
    }

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

