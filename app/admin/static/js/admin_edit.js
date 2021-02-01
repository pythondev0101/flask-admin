$(document).ready(function(){
    var table = $('.inline_table').DataTable({
        "dom": 'rtip',
        "scrollY": "200px",
        "scrollCollapse": true,
        "paging": false,
    });

});

(function() {
var fixed_footer = document.getElementById('chkbox_fixed_footer');
setTimeout(function() {
  fixed_footer.click();
}, 100);
})();