

$(document).ready(function () {
    $(".btn").click(function () {
        let num1 = $('#num1').val();
        let num2 = $('#num2').val();

        $.post("add/",{"a":num1, "b":num2},
            function (data) {
             data = JSON.parse(data);
             console.log(data["res"]);
             $("#result").append(data["res"]);
        })
    });
});
