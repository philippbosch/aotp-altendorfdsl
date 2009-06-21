$(document).ready(function() {
    $("#content img").each(function() {
        var float;
        if ((float = $(this).css('float')) && ((float=='left') || (float=='right'))) {
            $(this).wrap('<div class="image ' + float + '"></div>');
            $(this).css('float', 'none');
            var title;
            if (title = $(this).attr('title')) {
                $(this).after('<div class="image-caption" style="width: ' + $(this).width() + 'px;">' + title + '</div>')
            }
        }
    });
});