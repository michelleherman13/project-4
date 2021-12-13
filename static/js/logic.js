$(document).ready(function() {
    $("#gameSubmit").click(function() {
        $('#results').remove();
        get_recommended();
    });

    $("#other").click(function() {
        $('#results').remove();
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
    document.getElementById("userForms").reset();
}