function change(objName, min, max, step) {

    var obj = document.getElementById(objName);
    var tmp = +obj.value + step;
    if (tmp<min) tmp=min;
    if (tmp>max) tmp=max;
    obj.value = tmp;
    }

//document.getElementById("quantity").innerHTML = quantity;
// document.getElementById("number").innerHTML = number;


$(document).ready(function(){

    var form = $('#form_buying_product');
    console.log(form);

    form.on('submit',  function(event){
        event.preventDefault();

       var  quantity = $('#number').val();

        var submit_btn = $('#submit-btn');

        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data("product_name");

        var product_price = submit_btn.data("price");
//         document.getElementById("quantity").innerHTML = quantity;
        console.log(quantity);
        console.log(product_id);
        console.log(product_name);

        var data = {};
        data.product_id = product_id;
        data.quantity = quantity;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

        $.ajax({
            type: 'POST',
            url: url,

            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");

            },
            error: function(){
                console.log("error")

            },

        });

           })
});


$(document).ready(function(){
    var form = $('#form_buying_product_2');
    console.log(form);

    form.on('submit',  function(event){
        event.preventDefault();

       var quantity = $('#number').val();

        var submit_btn = $('#submit-btn');

var product_ids = submit_btn.data('product_ids');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data("product_name");

        var product_price = submit_btn.data("price");

//console.log(item);
//console.log(product_ids);
        console.log(quantity);

        console.log(product_id);
        console.log(product_name);

        var data = {};
        data.product_id = product_id;
        data.quantity = quantity;


        var csrf_token = $('#form_buying_product_2 [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

        $.ajax({
            type: 'POST',
            url: url,

            data: data,
            cache: true,
            success: function (data) {
// Перезавантаження сторінки
//            location.reload();

                console.log("OK");

            },
            error: function(){
                console.log("error")

            },

        });

           })
});



