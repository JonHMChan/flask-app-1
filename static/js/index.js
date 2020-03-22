// Your code starts here
$(document).ready(function() {
    $.ajax({
        method: "GET",
        url: "/api/pokemon",
        success: function(data) {
            for (var i = 0; i < data.length; i++) {
                var pokemon = data[i];
                var $pokemon = $(`<a href="/${pokemon.id}"></a>`).addClass("pokemon");
                var html = `
                    <h2>${pokemon.name}</h2>
                    <img class="pokemon-image" src=${pokemon.image_url} />
                `;
                $pokemon.append(html);
                $(".pokemon-container").append($pokemon);
            }
        }
    })
})