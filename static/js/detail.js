// Your code starts here
$(document).ready(function() {
    $.ajax({
        method: "GET",
        url: "/api/pokemon/" + window.location.pathname,
        success: function(data) {
            $(".pokemon-name").html(data.name);
            $(".pokemon-image").attr("src", data.image_url);
            $(".pokemon-description").text(data.description);
            for (var i = 0; i < data.types.length; i++) {
                $(".pokemon-types").append(`<li>${data.types[i]}</li>`);
            }
            for (var j = 0; j < data.evolutions.length; j++) {
                var evolution = data.evolutions[j];
                $(".pokemon-evolutions").append(`
                    <tr>
                        <td><a class="pokemon-evolution" href="/${evolution.id}">${evolution.to}</a></td>
                        <td>${evolution.level}</td>
                        <td>${evolution.method}</td>
                    </tr>
                `)
            }
        }
    })
})