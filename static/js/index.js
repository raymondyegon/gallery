// $(document).on('click', 'a[href^="#"]', function (event) {
//     event.preventDefault();

//     $('html, body').animate({
//         scrollTop: $($.attr(this, 'href')).offset().top - 50
//     }, 500);
// });
showinfo = (i) => {
    dict = eval(i)
    $('#imageimage').attr('src', dict.image);
    $('#imagedescription').text(dict.desc);
    $('#imagetitle').text(dict.name);
    $('#imagedirectlink').attr('href', window.location.origin + dict.image)
    $("#imagelink").val(window.location.origin + '/#' + dict.id);
    $("#ImageModal").modal('show');
}
copyaction = () => {
    document.getElementById("imagelink").select();
    document.execCommand("Copy");
}
// $('document').ready(() => {
//     if (window.location.href.match(/.*#\d+/)) {
//         id = window.location.href.match(/.*#(\d+)/)[1];
//         $('#pic' + id).trigger('click');
//     }
// })

$("#ImageModal").on('shown.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var id = button.data('whatever');

    var modal = $(this);
    modal.find('.modal-title').text(id)

})