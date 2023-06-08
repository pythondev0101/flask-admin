$(function() {
    // Add mm-active to the current page's <li>
    let activeUrlName = "/" + $(location).attr('href').split("/").splice(3, 4).join("/").split('?')[0];
    $(".nav-link").each(function() {
        console.log($(this).attr('href'));
        if(activeUrlName.includes($(this).attr('href'))){
            $(this).addClass('active');
        }
    });
}); // function
