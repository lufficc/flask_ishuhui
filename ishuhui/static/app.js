function messge(msg, type) {
    var snackbar = $("#snackbar");
    snackbar.text(msg);
    if (type === 'error') {
        snackbar.css("background-color", "#e15e35");
    } else {
        snackbar.css("background-color", "#333");
    }
    snackbar.attr('class', 'show');
    setTimeout(function () {
        snackbar.attr('class', '');
    }, 3000);
}