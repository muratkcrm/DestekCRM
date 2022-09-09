$(document).ready(function () {
    $("#id_ONMhesapTutar").on("click",function () {
        var sayi1 = Number($(#ONMMiktar).val());
        var sayi2 = Number($(#ONMFiyat).val());
        var toplam=sayi1+sayi2;
        $(#ONMhesapTutar).val(toplam);

    });
});