$(document).ready(function() {
    console.log("Page Loaded", $("#game").val());

    $("#gameSubmit").click(function() {
        get_recommended();
        console.log(game)
    });

    $("#other").click(function() {
        get_recommended();
    });
});

function get_recommended() {
    var game = $("#game").val();
    var platform = $("#platform").val();
    var score = $("#score").val();

    var input_dict = {
        "game": game,
        "platform": platform,
        "score": score
    }

    $.ajax({
        type: "POST",
        url: "./get_recommended",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": input_dict }),
        success: function(returnedData) {

            var game = JSON.parse(returnedData)

            console.log(game)

            $.each(game , function(index, item) { 
                console.log("Game: " + item["game"]);
                console.log("Critic_Score: " + item["Critic_Score"]);
            });
            $('#results').remove();
            let table = '<thead id="results"><tr><th style="color: #fff;background-color:#7166d4">Name</th><th style="color: #fff;background-color:#7166d4">Critic Score</th><th style="color: #fff;background-color:#7166d4">Platform</th><th style="color: #fff;background-color:#7166d4">ESRB Rating</th></tr></thead><tbody>';

            $.each(game, function(index, item) { 
                table += '<tr><td style="background-color:#efefef">'+item["game"]+'</td>';
                table += '<td style="background-color:#efefef">'+item["Critic_Score"]+'</td>';
                table += '<td style="background-color:#efefef">'+item["Platform"]+'</td>';
                table += '<td style="background-color:#efefef">'+item["ESRB_Rating"]+'</td></tr>';
            });

            table += '</tbody>';

            $('#output').empty().html(table);
            
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}