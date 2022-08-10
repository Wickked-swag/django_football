$(document).ready(function () {
    $(".addbtn").click(function () {
        let id = $('#add').val();

        $.post("add/",{"id":id}, function (data) {
            data = JSON.parse(data);
            alert(data["notice"])
        })
    });
});

$(document).ready(function () {
    $(".debtn").click(function () {
        let id = $('#delete').val();

        $.post("delete/",{"id":id}, function (data) {
            data = JSON.parse(data);
            alert(data["notice"])
        })
    });
});

$(document).ready(function () {
    $(".select").click(function () {
        let id = $('#select').val();

        $.post("select/",{"id":id}, function (data) {
            data = JSON.parse(data);
            if (data["notice"] === "id输入错误")
                alert(data["notice"])
            else
                //TODO 将搜索出来的球员信息在用户信息下方进行显示
                player = JSON.parse(data["player"])
                player = player[0]
                player = player["fields"]
                console.log(player)
                // player = JSON.parse(data["player"])
                // player = player["fields"]
                // console.log(player)
                $("#name").html(player["player_name"])
                $("#nation").html(player["nationality"])
                $("#positon").html(player["position"])
                $("#overall").html(player["overall"])
                $("#age").html(player["age"])
                $("#hits").html(player["hits"])
                $("#potential").html(player["potential"])
                $("#team").html(player["team"])
        })
    });
});

$(document).ready(function () {
    $(".show").click(function () {
        $.post("show/",
            {"id":NaN},
            function (data) {
            data = JSON.parse(data);
            players = data["players"]
            players = JSON.parse(players)
            // player = players[0]
            // player = player["fields"]
            // console.log(players.length)
            for (let id = 0 ; id < players.length ; id++)
            {
                player = players[id]
                player = player["fields"]
                let a = "";
                a = '<div class="player border  border-dark mt-3" >';
                a += '<div>name: ';
                a += player["player_name"]
                a += '</div>';
                a += '<div>nationality: ' + player["nationality"] + '</div>';
                a += '<div>position: ' + player["position"] + '</div>';
                a += '<div>overall: ' + player['overall'] +'</div>';
                a += '<div>age: ' + player['age'] + '</div>';
                a += '<div>hits: ' + player['hits'] + '</div>';
                a += '<div>potential: ' + player['potential'] + '</div>';
                a += '</div>'
                if(id>=0 && id<=2)
                {
                    $(".out1").append(a);
                }
                else if(id>=3 && id<=5)
                {
                    $(".out2").append(a);
                }
                else if(id>=6 && id<=8)
                {
                    $(".out3").append(a);
                }
            }


        })
    })
})

