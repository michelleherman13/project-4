$(document).ready(function() {
    console.log("Page Loaded", $("#game").val());

    $("#gameSubmit").click(function() {
        get_recommended();
        console.log(game)
    });

    $("#other").click(function() {
        get_recommended();
        console.log(game)
    });
});

function get_recommended() {
    var game = $("#game").val();
    // var platform = $("#platform").val();
    // var score = $("#score").val();

    var input_dict = {
        "game": game,
        // "platform": platform,
        // "score": score
    }

    $.ajax({
        type: "POST",
        url: "./get_recommended",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": input_dict }),
        success: function(returnedData) {

            console.log(returnedData);

            var game = JSON.parse(returnedData)

            console.log(game)

            $.each(game , function(index, item) { 
                console.log("Game: " + item["game"]);
                console.log("Critic_Score: " + item["Critic_Score"]);
            });

            let table = '<thead><tr><th style="background-color:#efefef">Name</th><th style="background-color:#FAD52D">Genre</th><th style="background-color:#FAD52D">Critic Score</th><th style="background-color:#FAD52D">Platform</th></tr></thead><tbody>';

            $.each(game, function(index, item) { 
                table += '<tr><td style="background-color:#efefef">'+item["game"]+'</td>';
                table += '<td style="background-color:#efefef">'+item["Critic_Score"]+'</td>';
                // table += '<td style="background-color:#efefef">'+item["Score"]+'</td>';
                // table += '<td style="background-color:#efefef">'+item["Genres"]+'</td></tr>';
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