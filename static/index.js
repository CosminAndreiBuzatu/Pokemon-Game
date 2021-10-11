function loadCard(pokemonName) {
  $.ajax({
      url: "/card?name="+pokemonName,
      type: "get",
      data: { },
      success: function(response) {
        $("#pokemonCard").html(response)
      },
      error: function(err) {}
  });
}

function loadCard2(pokemonName) {
  $.ajax({
      url: "/card?name="+pokemonName,
      type: "get",
      data: { },
      success: function(response) {
        $("#pokemonCard2").html(response)
      },
      error: function(err) {}
  });
}
